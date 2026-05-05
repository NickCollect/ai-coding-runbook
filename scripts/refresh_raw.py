#!/usr/bin/env python3
"""
Refresh 01_Raw/ from sources defined in scripts/sources.yaml.

Usage:
    python3 scripts/refresh_raw.py --source <name>     # crawl one source
    python3 scripts/refresh_raw.py --all               # crawl every source sequentially
    python3 scripts/refresh_raw.py --list              # print all source names
    python3 scripts/refresh_raw.py --source <name> --dry-run

Source naming:
    docs_sites   →  the 'name' field, e.g. code.claude.com / platform.claude.com
    github       →  github.<owner>, e.g. github.anthropics / github.modelcontextprotocol

Inside one source the crawler uses ThreadPoolExecutor (5 workers) over HTTP.
Github clones use the same pool: clone shallow → strip .git → tracked as plain files.

Exit codes:
    0 = source completed (may include skipped 404s, no real errors)
    1 = real failure (sitemap fetch error, network errors, etc.)
"""
from __future__ import annotations
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, urljoin
from xml.etree import ElementTree as ET

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "01_Raw"
META = RAW / "_meta"
SOURCES_FILE = ROOT / "scripts" / "sources.yaml"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)
HTTP_TIMEOUT = 30
HTTP_WORKERS = 5  # concurrent HTTP fetches per source

# Per-thread session reused across requests (connection pooling).
_session_local = None


def make_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*;q=0.8"})
    retry = Retry(
        total=4,
        backoff_factor=2,            # 2s, 4s, 8s, 16s
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"],
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=HTTP_WORKERS, pool_maxsize=HTTP_WORKERS)
    s.mount("https://", adapter)
    s.mount("http://", adapter)
    return s


def get_session() -> requests.Session:
    global _session_local
    import threading
    if _session_local is None:
        _session_local = threading.local()
    if not hasattr(_session_local, "s"):
        _session_local.s = make_session()
    return _session_local.s


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def load_sources() -> dict:
    with open(SOURCES_FILE) as f:
        return yaml.safe_load(f)


def url_to_path(url: str, target_dir: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path.endswith(".md"):
        if path.endswith("/") or "." not in path.rsplit("/", 1)[-1]:
            path = path.rstrip("/") + ".md"
    return RAW / target_dir / path


def fetch_url(url: str) -> requests.Response | None:
    try:
        r = get_session().get(url, timeout=HTTP_TIMEOUT, allow_redirects=True)
    except requests.RequestException as e:
        return None
    if r.status_code != 200:
        return None
    return r


def html_to_markdown(html: str, source_url: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    main = (
        soup.select_one("main")
        or soup.select_one("article")
        or soup.select_one("[role=main]")
        or soup.select_one(".content, .docs-content, #content, #main-content")
        or soup.body
    )
    if main is None:
        return ""
    # Strip Next.js image proxy tags before converting — their /_next/image?url=... relative
    # paths survive as markdown image links and Obsidian misidentifies them as internal links,
    # creating hundreds of ghost nodes in the graph.
    for img in main.find_all("img", src=re.compile(r"/_next/image")):
        # Try to recover the actual CDN URL from the `url` query param
        src = img.get("src", "")
        m_url = re.search(r"url=([^&]+)", src)
        if m_url:
            from urllib.parse import unquote
            real_url = unquote(m_url.group(1))
            img["src"] = real_url
        else:
            img.decompose()

    # Resolve all relative links/images to absolute URLs before markdownifying.
    # Obsidian interprets relative markdown links as internal vault links, creating
    # ghost nodes in the graph. Making all links absolute prevents this.
    from urllib.parse import urljoin, urlparse
    base = source_url
    for tag in main.find_all(["a", "img"]):
        attr = "href" if tag.name == "a" else "src"
        val = tag.get(attr, "")
        if not val or val.startswith(("#", "mailto:", "javascript:")):
            continue
        if not val.startswith(("http://", "https://")):
            tag[attr] = urljoin(base, val)

    md = markdownify(str(main), heading_style="ATX", bullets="-")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    header = f"---\nsource_url: {source_url}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n"
    if title:
        header += f"title: {json.dumps(title)}\n"
    header += "---\n\n"
    return header + md + "\n"


def fetch_doc_page(url: str, try_md_first: bool = True) -> str | None:
    """Try Mintlify-style .md endpoint first; fall back to HTML extraction."""
    if try_md_first:
        md_url = url.rstrip("/") + ".md"
        r = fetch_url(md_url)
        if r is not None and r.headers.get("content-type", "").startswith(("text/markdown", "text/plain")):
            body = r.text
            header = (
                f"---\nsource_url: {url}\n"
                f"fetched_at: {datetime.now(timezone.utc).isoformat()}\n"
                f"fetch_method: mintlify_md\n---\n\n"
            )
            return header + body + ("\n" if not body.endswith("\n") else "")
    r = fetch_url(url)
    if r is None:
        return None
    return html_to_markdown(r.text, url)


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        old = path.read_text(encoding="utf-8")
        old_norm = re.sub(r"^fetched_at:.*$", "", old, count=1, flags=re.MULTILINE)
        new_norm = re.sub(r"^fetched_at:.*$", "", content, count=1, flags=re.MULTILINE)
        if old_norm == new_norm:
            return False
    path.write_text(content, encoding="utf-8")
    return True


def fetch_sitemap_urls(sitemap_url: str) -> list[str]:
    r = fetch_url(sitemap_url)
    if r is None:
        return []
    xml_str = re.sub(r'xmlns="[^"]+"', "", r.text, count=1)
    try:
        root = ET.fromstring(xml_str)
    except ET.ParseError:
        return []
    urls: list[str] = []
    for loc in root.iter("loc"):
        u = (loc.text or "").strip()
        if not u:
            continue
        if u.endswith(".xml"):
            urls.extend(fetch_sitemap_urls(u))  # recurse one level for sitemap index
        else:
            urls.append(u)
    return urls


# ---------- per-source crawlers ----------


def crawl_docs_site(site: dict, dry_run: bool) -> tuple[int, int, int]:
    name = site["name"]
    target_dir = site["target_dir"]
    prefixes = site.get("include_prefixes", [])
    # Anthropic main site (anthropic.com/news, /research, /engineering) is NOT Mintlify;
    # .md fetches always 404 and waste time. Skip the .md probe for known non-Mintlify hosts.
    skip_md = site.get("skip_md_probe", False) or name == "anthropic.com"

    log(f"docs_site: {name} — fetching sitemap")
    urls = fetch_sitemap_urls(site["sitemap"])
    if not urls:
        log(f"  ✗ sitemap fetch/parse failed for {name}")
        return 0, 0, 1

    if prefixes:
        urls = [u for u in urls if any(urlparse(u).path.startswith(p) for p in prefixes)]

    exclude_patterns = site.get("exclude_patterns", [])
    if exclude_patterns:
        urls = [u for u in urls if not any(urlparse(u).path.startswith(p) for p in exclude_patterns)]

    log(f"  → {len(urls)} URLs match prefixes (concurrent={HTTP_WORKERS}, skip_md={skip_md})")
    if dry_run:
        for u in urls[:5]:
            print(f"    {u}")
        if len(urls) > 5:
            print(f"    ... ({len(urls) - 5} more)")
        return len(urls), 0, 0

    fetched = errors = written = 0
    completed = 0

    def work(url: str) -> tuple[str, str | None]:
        return url, fetch_doc_page(url, try_md_first=not skip_md)

    with ThreadPoolExecutor(max_workers=HTTP_WORKERS) as ex:
        futures = [ex.submit(work, u) for u in urls]
        for fut in as_completed(futures):
            url, content = fut.result()
            completed += 1
            if completed % 100 == 0 or completed == len(urls):
                log(f"  progress: {completed}/{len(urls)}")
            if content is None:
                errors += 1
                continue
            fetched += 1
            path = url_to_path(url, target_dir)
            if write_if_changed(path, content):
                written += 1

    log(f"  ✓ {name}: {fetched} fetched, {written} written/changed, {errors} errors")
    return fetched, written, errors


# ---------- github crawler ----------


def clone_repo(spec: dict) -> tuple[str, int, int, int]:
    """Clone one repo. Returns (label, fetched, written, errors).
    Strips .git after clone so files are tracked as plain content by parent repo."""
    owner = spec["owner"]
    repo = spec["repo"]
    label = f"{owner}/{repo}"
    target = RAW / "github" / owner / repo
    url = f"https://github.com/{owner}/{repo}.git"
    web_url = f"https://github.com/{owner}/{repo}"

    # HEAD probe — skip 404 silently (renamed/removed repo)
    try:
        probe = get_session().head(web_url, timeout=10, allow_redirects=False)
        if probe.status_code == 404:
            log(f"  ⚠ {label} returns 404 (renamed/removed) — skipping")
            return label, 0, 0, 0
        if probe.status_code in (301, 302):
            new_loc = probe.headers.get("location", "(unknown)")
            log(f"  ⚠ {label} redirects to {new_loc} — sources.yaml needs update")
    except requests.RequestException as e:
        log(f"  probe failed for {label}: {e} (continuing)")

    # Always clone fresh: simpler than incremental pull, only ~1-3 min total for all repos.
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", url, str(target)],
            check=True, capture_output=True, text=True,
            env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
        )
    except subprocess.CalledProcessError as e:
        log(f"  ✗ clone failed for {label}: {e.stderr.strip()[:200]}")
        return label, 0, 0, 1

    # Strip .git so parent repo tracks files (not gitlink). Lose history, keep content.
    git_dir = target / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)

    file_count = sum(1 for _ in target.rglob("*") if _.is_file())
    log(f"  ✓ {label}: cloned ({file_count} files)")
    return label, 1, 1, 0


def crawl_github_owner(owner_filter: str, sources: dict, dry_run: bool) -> tuple[int, int, int]:
    """Clone all repos under one owner (e.g. anthropics or modelcontextprotocol)."""
    repos = [s for s in sources.get("github_repos", []) if s["owner"] == owner_filter]
    log(f"github.{owner_filter}: {len(repos)} repos (concurrent={HTTP_WORKERS})")
    if dry_run:
        for s in repos:
            print(f"    {s['owner']}/{s['repo']}")
        return len(repos), 0, 0

    fetched = written = errors = 0
    with ThreadPoolExecutor(max_workers=HTTP_WORKERS) as ex:
        futures = [ex.submit(clone_repo, s) for s in repos]
        for fut in as_completed(futures):
            _label, f, w, e = fut.result()
            fetched += f
            written += w
            errors += e
    return fetched, written, errors


# ---------- meta + dispatch ----------


def write_meta(source_label: str, stats: dict) -> None:
    META.mkdir(parents=True, exist_ok=True)
    fragment = META / f"refresh_{source_label.replace('.', '_').replace('/', '_')}.json"
    payload = {
        "source": source_label,
        "completed_at": datetime.now(timezone.utc).isoformat(),
        **stats,
    }
    fragment.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def list_sources() -> list[str]:
    s = load_sources()
    names = [d["name"] for d in s.get("docs_sites", [])]
    owners = sorted({r["owner"] for r in s.get("github_repos", [])})
    names += [f"github.{o}" for o in owners]
    return names


def crawl_one(source_name: str, dry_run: bool) -> int:
    sources = load_sources()
    if source_name.startswith("github."):
        owner = source_name.split(".", 1)[1]
        f, w, e = crawl_github_owner(owner, sources, dry_run)
    else:
        site = next((s for s in sources.get("docs_sites", []) if s["name"] == source_name), None)
        if site is None:
            log(f"unknown source: {source_name}")
            log(f"available: {', '.join(list_sources())}")
            return 1
        f, w, e = crawl_docs_site(site, dry_run)

    if not dry_run:
        write_meta(source_name, {"fetched": f, "written": w, "errors": e})
    log(f"DONE {source_name}: fetched={f} written={w} errors={e}")
    return 0 if e == 0 else 1


def crawl_all(dry_run: bool) -> int:
    total_errors = 0
    for name in list_sources():
        rc = crawl_one(name, dry_run)
        if rc != 0:
            total_errors += 1
    return 0 if total_errors == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="One source name from --list")
    ap.add_argument("--all", action="store_true", help="Crawl all sources sequentially")
    ap.add_argument("--list", action="store_true", help="Print source names and exit")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.list:
        for n in list_sources():
            print(n)
        return 0
    if args.source:
        return crawl_one(args.source, args.dry_run)
    if args.all:
        return crawl_all(args.dry_run)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
