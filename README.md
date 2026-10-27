# north-america-web-seo-compliance · 北美网站 SEO 与合规

A Claude Code / Codex skill that researches and operationalizes North American website SEO, content-quality, privacy, subscriptions, accessibility, content-safety, and legal-compliance requirements — for English-market content, creator, AI, or mixed Web products.

一个 Claude Code / Codex skill，用于调研并落地北美网站的 SEO、内容质量、隐私、订阅、无障碍、内容安全与法律合规要求——面向英文市场的内容、创作者、AI 或混合型 Web 产品。

## What it does · 功能

- Four-role gated workflow: competitor shortlisting → evidence-backed audits → master compliance checklist + original copy → UI/ops backlog.
  四角色门控流程：竞品筛选 → 证据化审计 → 主合规清单 + 原创文案 → UI/运营 backlog。
- Final deliverable is a **PDF** (an HTML page styled for print, rendered to PDF). `.xlsx` is an intermediate format.
  最终交付为 **PDF**（HTML 排版转 PDF）；`.xlsx` 只是中间格式。
- Bundled Python tool `scripts/compliance_workflow.py` generates the checklist (XLSX) and report (PDF) — `pip install -r requirements.txt`.
  内置 Python 工具 `scripts/compliance_workflow.py` 生成清单（XLSX）与报告（PDF）——`pip install -r requirements.txt`。
- Evidence-class separation, official-source verification, counsel-review gating, and launch-QA coverage.
  证据分级、官方源核验、律师审查门、上线 QA 覆盖。
- Data retention / storage location / cross-border transfer principles (minimize retention, clear disclosure, lawful transfer, don't break Googlebot).
  数据留存 / 存储地区 / 跨境传输原则（最小化保存、清晰告知、合法跨境、不破坏 Googlebot）。

## Disclaimer · 免责声明

This skill prepares issue lists, structured drafts, operational copy, and implementation requirements. It is **not a substitute for licensed legal advice**.

本 skill 只产出问题清单、结构化草稿、运营文案与实施要求，**不构成持牌法律意见**。

## Install · 安装

Copy this directory into `~/.claude/skills/` (Claude Code) or your agent's skills directory, then restart the agent.

把本目录复制到 `~/.claude/skills/`（Claude Code）或你的 agent skills 目录，然后重启 agent。

## Structure · 结构

- `SKILL.md` — entry instructions and the gated workflow / 入口说明与门控流程
- `references/workflow.md` — stage gates and required inputs / 阶段门与输入
- `references/schemas.md` — deliverable schemas / 交付物 schema
- `references/role-modules.md` — the four roles and handoffs / 四角色与交接
- `references/coverage-matrix.md` — final self-review matrix / 终检矩阵
- `agents/openai.yaml` — Codex/OpenAI interface metadata / Codex/OpenAI 接口元数据
- `scripts/compliance_workflow.py` — deliverable generator (XLSX + PDF) / 交付物生成器（XLSX + PDF）
- `requirements.txt` — Python dependencies / Python 依赖
