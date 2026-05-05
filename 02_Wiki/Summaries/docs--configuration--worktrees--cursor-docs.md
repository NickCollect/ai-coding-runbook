---
type: summary
source: 01_Raw/docs.cursor.com/docs--configuration--worktrees.md
source_url: https://cursor.com/docs/configuration/worktrees
title: "Worktrees（隔离 Git 检出）"
summarized_at: 2026-05-06
entities_referenced: []
concepts_referenced: []
---

Worktrees 让 Agent 在独立的 Git checkout 中工作，每个任务拥有独立的文件、依赖和变更，不影响主 checkout，适合并行运行多个 Agent 于同一仓库。

**配置**：在 `.cursor/worktrees.json` 中定义 setup 命令（命令数组或脚本路径），支持 `setup-worktree-unix`（macOS/Linux 优先）、`setup-worktree-windows`（Windows 优先）、`setup-worktree`（通用回退）。环境变量 `$ROOT_WORKTREE_PATH` 指向主 worktree 路径。

**CLI 使用**：`agent --worktree "任务描述"` 在新 worktree 中运行 Agent，worktree 存放在 `~/.cursor/worktrees/`。

**编辑器 Slash Commands**（Editor Window）：
- `/worktree <任务>`：在独立 checkout 中执行，结束后可 `/apply-worktree` 合并或 `/delete-worktree` 删除
- `/best-of-n model1,model2 <任务>`：同一任务在多个模型的独立 worktree 中并行运行，对比选择最优结果

**自动清理**：`cursor.worktreeCleanupIntervalHours`（检查间隔）和 `cursor.worktreeMaxCount`（最大保留数）控制磁盘用量。

**注意**：不推荐用 symlink 共享依赖，应使用快速包管理器（bun/pnpm/uv）重新安装。UI 原生 Worktrees 功能仅在 Agents Window 可用。
