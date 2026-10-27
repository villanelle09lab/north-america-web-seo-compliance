---
name: north-america-web-seo-compliance
description: Research and operationalize North American website SEO, content-quality, privacy, subscriptions, accessibility, content-safety, and legal-compliance requirements. Use for competitor shortlisting or audits, official-source verification, compliance copy, gap checklists, UI/frontend backlogs, operations copy packs, or launch QA for English-market content, creator, AI, or mixed Web products. Do not use as a substitute for licensed legal advice. 中英双语：调研并落地北美网站 SEO 与合规要求（英文市场内容 / 创作者 / AI / 混合 Web 产品），不替代持牌法律意见。
---

# North America Web SEO and Compliance · 北美网站 SEO 与合规

Run the work as a gated sequence. Do not jump from a competitor list directly to final legal copy or product requirements.
按门控流程逐步执行：不要从竞品清单直接跳到最终法律文案或产品需求。

## 中文概览 · Chinese overview

本 skill 用四个专家角色串行完成北美网站 SEO 与合规：

1. **Role 1 技术型 SEO 专家**：发现并分类 5+5+5 竞品样本（AI 内容 / 创作者 / 视频或混合平台）。
2. **Role 2 合规审计师**：基于公开证据逐站审计，每家提取 3–5 条英文披露样例。
3. **Role 3 UX 文案 + 法务合规专员**：把核实发现与现行官方要求转成主清单和原创英文文案。
4. **Role 4 Web 产品经理**：把清单转成 UI/前端 backlog 和运营文案包。

流程分 8 个阶段（Stage 0–7）：范围摄入 → 竞品筛选 → 逐站取证 → 官方源基线 → 主清单与文案 → UI backlog → 运营文案 → 上线 QA。最终交付为 PDF；法律结论一律留律师，不编造事实。

## Output format · 输出格式

The final deliverable — master checklist, compliance copy pack, UI/operations views, and launch QA record — is produced as a **PDF**: an HTML page styled for print, then rendered to PDF. Spreadsheets (`.xlsx`) and Markdown are intermediate working formats, not the final deliverable.
最终交付（主清单、合规文案包、UI/运营视图、上线 QA 记录）统一输出为 **PDF**（HTML 排版后转 PDF）；`.xlsx` 与 Markdown 只是中间工作格式。

Generate these artifacts with the bundled Python tool `scripts/compliance_workflow.py` (`checklist` → XLSX master checklist; `report` → HTML/PDF from a JSON row list). Install its dependency with `pip install -r requirements.txt`.
用内置 Python 工具 `scripts/compliance_workflow.py` 生成这些交付物（`checklist` 生成 XLSX 主清单；`report` 从 JSON 行数据生成 HTML/PDF）；依赖用 `pip install -r requirements.txt` 安装。

## Operating principles · 工作原则

- Maintain one master execution checklist as the source of truth. Competitor profiles, source snapshots, and comparison matrices are supporting evidence; UI/development and operations deliverables are filtered views or exports from the master checklist.
- Separate five evidence classes: `verified competitor fact`, `official legal/regulatory source`, `platform/technical guidance`, `analysis/inference`, and `unconfirmed`.
- Record the source URL, page title, jurisdiction, publication/effective date when available, and access date for every material claim.
- Treat competitor implementations as examples, never as proof of legal sufficiency. Treat Google, Schema.org, and WCAG guidance according to their actual status; do not relabel them as statutes.
- Use current official primary sources for laws, regulator guidance, Google/Search documentation, WCAG, and payment or platform rules. Re-check anything time-sensitive at delivery time.
- Say `not found in the reviewed evidence`, not `does not exist`, unless absence is independently established.
- Draft original wording. Do not reproduce long competitor policy passages. Short excerpts are evidence only.
- Never invent a legal entity, address, contact, author, reviewer, expert credential, consent record, certification, vendor, retention period, or jurisdictional fact. Use explicit placeholders and mark them as launch blockers.
- Legal policies and conclusions require qualified counsel approval. AI may prepare issue lists, structured drafts, operational copy, and implementation requirements.
- Mock data must be labeled `SAMPLE`, `PLACEHOLDER`, or `TEST ONLY` and kept out of production.
- For data retention, storage location, and cross-border transfers: minimize retention (per-data-type periods enforced in code), disclose clearly, transfer lawfully (GDPR SCC/adequacy for the EU; CCPA/CPRA for the US; PIPL for China-involved processing; other rules per jurisdiction), and never break Googlebot crawling (access and consent overlays are client-side; crawlers receive the same HTML).

## Start-of-task behavior · 开始任务时

1. Determine whether this is a new project or a continuation. Reuse verified existing artifacts; do not repeat completed research unless freshness or scope changed.
2. Identify the current stage from the ordered workflow below.
3. Ask for missing inputs at the moment they become necessary. Never wait for the user to notice that a URL, market, business fact, or implementation detail is missing.
4. Ask one compact batch of related questions per gate, not a long interrogation. Explain which downstream decision each missing item affects.
5. If the user supplies a named site but no URL, ask for the official URL before auditing it. If the user asks AI to discover competitors, research candidates first and ask the user to approve the proposed official domains before deep auditing.
6. If a public page is blocked, first record the access boundary. Then ask the user for the exact URL, exported HTML, screenshot, policy text, or authenticated-page capture needed; do not bypass access controls.

Read [references/role-modules.md](references/role-modules.md) before execution; it preserves the four required roles, their inputs, checks, outputs, and handoffs. Read [references/workflow.md](references/workflow.md) for stage gates and required inputs. Read [references/schemas.md](references/schemas.md) before creating evidence tables, the master checklist, copy, backlogs, or QA outputs. Use [references/coverage-matrix.md](references/coverage-matrix.md) during final self-review to ensure no requirement from the originating workflow was dropped.

## Required role chain · 必选角色链

Execute the four roles in order. Do not collapse away their separate responsibilities:

1. `Role 1 — North American digital-entertainment and AI/Web3 technical SEO specialist`: discovers and classifies the 5 + 5 + 5 competitor sample.
2. `Role 2 — North American website compliance auditor and Programmatic SEO specialist`: performs evidence-backed site audits and extracts 3–5 short, attributable English disclosure samples per competitor when available.
3. `Role 3 — Senior international UX copywriter and legal-compliance specialist`: converts verified findings and current official requirements into the target site's master checklist and original English copy.
4. `Role 4 — International Web product manager`: converts approved checklist rows into a UI/frontend development backlog and an operations copy/mock-material pack.

Each role receives the prior role's approved output. If a required handoff is missing, stop and request it rather than silently filling the gap.

## Ordered workflow · 有序流程

### Stage 0 — Scope and applicability intake · 范围与适用性摄入

Define the target website and real business before looking for patterns to copy. Collect the target domain, legal entity and contacts, markets and jurisdictions, product and content model, content sources, UGC and real-person inputs, content rating and restrictions, accounts and data, vendors, monetization, subscription/refund behavior, advertising/affiliate activity, marketing communications, and supported platforms.

If the target domain or critical product facts are missing, ask now. Do not infer them from the competitor categories.

Output: a scope card with `confirmed`, `working assumption`, `unconfirmed`, `not applicable`, and `launch blocker` states.

Gate: the target product, primary jurisdictions, content/UGC model, real-person involvement, monetization, and major data flows are clear enough to determine what is relevant.

### Stage 1 — Competitor discovery and sample lock · 竞品发现与样本锁定

Activate Role 1.

Build the requested sample by function, not by name recognition alone. Default for this workflow:

- 5 AI-native or AI-assisted content or short-video platforms.
- 5 AI character or interactive-content platforms.
- 5 creator-subscription, live, or video platforms.

Label each site's actual type. A traditional distributor is not a direct product match; a live or UGC site may still be a scale, SEO, safety, or regulatory reference.

Use the selection rubric in `workflow.md`. Provide official domain, business model, comparison role, North American relevance, evidence strength, and selection reason. Do not claim traffic leadership without a verifiable traffic source.

If the user already has a list, validate domains and categories. If URLs are missing or ambiguous, ask for them before deep audit.

Gate: the user or assigned reviewer approves the 15-site sample and substitutions.

### Stage 2 — Site-by-site evidence capture · 逐站取证

Activate Role 2.

Audit one site at a time. Capture the homepage/footer, key content templates, robots/sitemap/canonical/hreflang/schema, author and editorial signals, affiliate or sponsored disclosure, AI-content disclosure, accessibility signals, policies, privacy choices, age or access restrictions, payment/cancellation/refund flows, copyright and safety reporting, impersonation/synthetic-media and real-person-likeness controls, and relevant registration or checkout states.

Do not score a site from search snippets alone. Preserve screenshots or page extracts where permitted and identify blocked or authenticated-only flows. For each competitor, collect 3–5 short English disclosure examples when available, with URL, placement, access date, purpose, and a note that the language is evidence rather than target-site copy. If fewer than three are available, report the shortfall instead of padding the set.

Gate: each site has a minimum evidence record or an explicit reason why evidence is unavailable.

### Stage 3 — Official-source baseline and comparative audit · 官方源基线与对比审计

Verify current requirements against first-party sources for the target jurisdictions. Build separate matrices for:

- SEO and content quality.
- Privacy, cookies, consumer rights, and marketing communications.
- Age restrictions and child safety.
- Copyright, DMCA, impersonation, synthetic-media misuse, and content reporting.
- Pricing, auto-renewal, cancellation, refunds, virtual currency, and disputes.
- Accessibility and technical implementation.

For every finding, state whether it is a legal requirement, platform rule, technical recommendation, competitor pattern, or counsel question. High-change topics such as state privacy laws, consumer-protection rules, and provincial requirements need an `as of` date and jurisdiction matrix.

Gate: a human reviewer checks missing evidence and confirms that competitor practice was not confused with law.

### Stage 4 — Master execution checklist and original copy · 主清单与原创文案

Activate Role 3.

Merge only applicable findings into the master checklist. Each row must answer: where it appears, why it applies, what must be built or written, the English copy or copy placeholder, who owns it, what evidence supports it, and how QA proves it works.

Draft concise operational copy directly. For Terms, Privacy, Cookie, DMCA, content-safety policies, subscriptions, refunds, and dispute clauses, create a structured counsel-review draft with placeholders and issue flags rather than claiming it is publication-ready.

Copy snippets taken from competitors are evidence samples, not final copy. Preserve provenance and write a new version for the target product.

Gate: AI performs a row-by-row self-check, then a human reviews applicability, omissions, real-world facts, and legal escalation items.

### Stage 5 — UI and frontend backlog view · UI 与前端 backlog

Activate Role 4, Deliverable A.

Export rows that require product, design, frontend, backend, consent management, SEO infrastructure, or QA work. Include triggers, states, regional logic, device behavior, authentication state, storage/consent behavior, accessibility, Copy ID, dependencies, analytics events when authorized, and acceptance criteria.

Do not turn a policy statement into a product requirement unless a user-visible or operational capability must change.

### Stage 6 — Operations copy and mock-material view · 运营文案与素材视图

Continue Role 4, Deliverable B.

Export rows owned by operations, content, support, trust and safety, or legal coordination. Include static copy, policy inputs, FAQ and support scripts, author/reviewer evidence, company/contact fields, content review records, and clearly labeled sample data needed for development or review environments.

Never propose a fabricated author, expert, North American address, testimonial, review, or compliance certification as production material.

### Stage 7 — Launch QA and maintenance · 上线 QA 与维护

Test regional, device, consent, rejection, failure, cancellation, reporting, data-rights, crawler, accessibility, and policy-version scenarios. A policy link without the matching product flow or operating process does not pass.

Close only when each P0 row has an owner, implementation or approved not-applicable reason, copy status, legal status, and QA evidence. Record a review cadence and triggers for re-audit: jurisdiction expansion, new monetization, UGC, real-person inputs, new vendors, material AI capability changes, or regulatory updates.

## Interaction and stopping rules · 交互与停止规则

- At the end of each stage, lead with the decision-ready result, then list evidence gaps and the exact human checks required.
- Continue automatically within the current approved stage. Stop at a gate when the next stage depends on a material user choice or human verification.
- Ask for the target URL at Stage 0 if current-site assessment is in scope. Ask for competitor URLs at Stage 1 when the user supplies names without reliable official domains. Ask for page exports or screenshots at Stage 2 only when access is blocked or the flow is non-public.
- Do not mark any version `final`, move it to confirmed outputs, publish policies, install this skill, or overwrite existing artifacts without explicit approval.

## Quality bar · 质量门槛

A complete run produces:

1. A verified scope card.
2. A locked competitor sample with classification and evidence boundaries.
3. Per-site evidence records and a comparative audit.
4. A current official-source and counsel-question matrix.
5. One self-contained master execution checklist with unique Requirement IDs and Copy IDs.
6. A UI/development backlog view and an operations copy/mock-material view derived from that checklist.
7. A P0 launch QA record and an update plan.
8. A completed coverage-matrix review confirming that every required role and requested control was handled or explicitly marked not applicable.

If any item is missing, state exactly which gate remains open and what input or reviewer is needed.
