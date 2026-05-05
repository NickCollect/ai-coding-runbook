---
type: summary
source: 01_Raw/anthropic.com/engineering/infrastructure-noise.md
source_url: https://www.anthropic.com/engineering/infrastructure-noise
title: "Quantifying infrastructure noise in agentic coding evals"
summarized_at: 2026-05-05
entities_referenced: []
concepts_referenced: []
---

Anthropic post (Feb 05, 2026) by Gian Segato showing that infrastructure configuration alone can swing agentic-coding-benchmark scores by several percentage points — sometimes more than the leaderboard gap between top models.

**Headline finding.** On Terminal-Bench 2.0, the gap between most- and least-resourced setups was **6 percentage points (p < 0.01)**. Static benchmarks score model output directly; agentic evals are different — the runtime environment is integral to problem-solving (write programs, run tests, install deps, iterate). Two agents with different resource budgets aren't taking the same test.

**How it surfaced.** Anthropic ran Terminal-Bench 2.0 on a Google Kubernetes Engine cluster. Scores didn't match the official leaderboard; infra error rates were 6%. Cause: Kubernetes treats per-task resource specs as both floor *and* hard ceiling — a momentary memory spike OOM-kills a container that would otherwise have succeeded. Container runtimes have two separate parameters (guaranteed allocation vs. hard kill threshold); when set equal, zero headroom. Terminal-Bench's official leaderboard uses a more lenient sandbox provider that allows temporary overallocation.

**Experiment: 6 resource configurations** from strict (1×) to uncapped, same model + harness + task set.
- *Infra error rate*: 5.8% at 1× → 0.5% at uncapped, monotonic decrease. Drop from 1× to 3× (5.8% → 2.1%) significant at p < 0.001.
- *Success rate*: 1× to 3× fluctuates within noise (p = 0.40) — most tasks crashing at 1× were doomed anyway. Above 3×, success climbs faster than infra-error decline. From 3× to uncapped, infra errors drop 1.6 pp while success jumps ~4 pp.
- *Total lift 1× → uncapped*: +6 pp (p < 0.01). Tasks like `rstan-to-pystan` and `compile-compcert` significantly improve with memory headroom.

**What the limits change.** Up to ~3×, extra resources fix infra reliability without making the test easier. Above 3×, resources actively help solve more problems — agents can pull large dependencies, spawn expensive subprocesses, run memory-intensive test suites. *Tight limits reward lean code; generous limits reward heavyweight brute-force.* Both legitimate, but collapsing them into a single score without specifying resources makes results uninterpretable.

**Concrete example** — `bn-fit-modify` (Bayesian network fitting). Some models default to installing the full data-science stack (`pandas`, `networkx`, `scikit-learn`); under tight limits the pod OOMs during install before any solution code is written. A leaner stdlib-only strategy exists; some models default to it. Resource configuration determines which approach succeeds.

**Cross-eval check on SWE-bench.** Same direction, smaller magnitude: only 1.54 pp at 5× over 1× across 227 problems × 10 samples. SWE-bench tasks are less resource-intensive.

**Other confounders.** Time limits, cluster health, hardware specs, concurrency level, egress bandwidth all in scope. Anecdotal evidence of pass-rate fluctuation by time of day (API latency varies with traffic). The "model capability vs. infrastructure behavior" boundary is blurrier than benchmark scores suggest.

**Recommendations.**
1. Specify both *guaranteed allocation* and *hard ceiling* per task — single pinned values cause spurious OOMs.
2. Calibrate the band so floor and ceiling scores fall within noise of each other (Terminal-Bench: 3× ceiling cut infra errors 2/3 with score lift within noise — reasonable tradeoff).
3. For public benchmarks, run at multiple times/days to average out time-of-day noise.
4. Treat resource configuration as a first-class experimental variable (like prompt format or sampling temperature).
5. **Skepticism rule of thumb**: leaderboard differences below 3 pp deserve skepticism until eval configuration is documented and matched. "A few-point lead might signal a real capability gap — or it might just be a bigger VM."
