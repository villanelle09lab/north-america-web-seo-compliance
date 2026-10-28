# Deliverable schemas

Use these schemas when the workflow creates tables or structured outputs. A spreadsheet may add filters and validation, but it must preserve the fields below.

## Competitor shortlist

| Field | Requirement |
|---|---|
| Segment | Content / AI / creator or mixed reference |
| Brand | Official brand name |
| Official URL | Canonical domain or verified app landing domain |
| Actual business type | Accurate product and content model |
| Core business model | Free, ads, subscription, credits, creator share, etc. |
| Comparison role | Direct / scale-SEO / governance / counterexample / reserve |
| North American relevance | Evidence-backed reason |
| SEO reference value | Specific infrastructure or content pattern |
| Compliance reference value | Specific policy, control, or operational flow |
| Evidence and access date | Linked source(s) and YYYY-MM-DD |
| Score and limitations | Weighted score plus evidence caveat |

## Evidence record

Use one row per observation:

`Evidence ID / Brand / Page or component / Topic / Observation / Short excerpt if essential / Evidence class / Status / URL / Screenshot or saved artifact / Access date / Jurisdiction / Notes`

Keep excerpts short. Store longer page captures separately where permitted.

## Comparative audit

`Audit ID / Topic / Competitor / Observed implementation / Evidence ID / Completeness / Reusable pattern / Risk or anti-pattern / Target-product relevance / Official-source check / Counsel status`

Cover, when applicable:

- Crawl/indexation, canonical/hreflang, sitemaps, structured data, video search, heading/alt patterns, programmatic-page quality, author/editorial evidence, AI/affiliate disclosure, copyright reporting, and accessibility.
- Privacy notices and choices, cookie consent, sale/share/targeted-ad opt-out, GPC, Canadian consent, retention, vendors, transfers, data rights, and marketing consent.
- Age/access restriction, structured metadata, content rating, child safety, impersonation, synthetic-media, report/appeal, evidence preservation, and law-enforcement contact.
- Pricing, trials, auto-renewal, cancellation, refunds, virtual currency, disputes, and receipts/notices.

## Master execution work order · 主执行工单

Deliver as **three phase sheets, not one wide matrix**. Each sheet is a filtered, execution-sequenced view of the single master checklist. Internal evidence/audit fields (source URL, evidence class, access date, counsel status, competitor evidence, etc.) stay in the Evidence record and Comparative audit tables — never in the delivered columns.

The three parts map to the three sheets: `技术排版` → Sheet 1 `1 开发`; `UI 设计排版` → Sheet 2 `2 UI+开发`; `运营排版` → Sheet 3 `3 运营文案`.

### Sheet 1 — `1 开发`（engineering-only items, no UI needed）

- Row 1 (title): `1 开发处理（无需 UI 出稿）`
- Row 2 (scope / collaboration): e.g. `后端 / 前端 / 运维 / SEO 技术实现。P0 = 上线阻断。最后一列 = 对参考文件的修正。`
- Row 3 (columns): `编号 | 优先级 | 模块 | 事项 | 具体需求（做什么）| 合规/SEO 依据 | 验收标准 | 对参考文件的修正/备注`

### Sheet 2 — `2 UI+开发`（UI and engineering together）

- Row 2 (collaboration): e.g. `先由 UI 出组件、状态、响应式和无障碍方案，再交开发实现；文案按 C-xx 引用运营表。`
- Columns: `编号 | 优先级 | 模块 | 事项 | 具体需求（做什么）| 对参考文件的修正/备注`

### Sheet 3 — `3 运营文案`（operations copy）

- Row 2 (scope): e.g. `英文基线仅为草稿，最终以法务审定为准。政策正文由运营备料、法务起草定稿。`
- Columns: `编号 | 优先级 | 类型 | 文案/资料 | 需要写什么（要点）| 建议英文基线 | 展示位置`

### Cross-cutting norms · 通用规范

- **ID 前缀 by phase**: `D-` = 开发, `U-` = UI, `C-` = 文案, `L-` = 法务. Cross-reference explicitly across sheets (e.g. `U-10 引用 C-08`, `C-05 引用 L-10`), never leave the dependency implicit.
- **优先级**: `P0` = 上线阻断; `P1` = 上线后/次要; `P0（条件）` = 只有条件触发时才是 P0（如某项声明按法务结论显示）。
- **模块分组**: cluster rows into `A` / `B` / `C` logical groups within each sheet (e.g. 开发: A 地区与年龄门 / B 搜索引擎技术 SEO / C 账户与登录)。Group by module, not by dimension.
- **具体需求（做什么）**: write as numbered steps `1) 2) 3)`, each concrete and testable, with exact values (durations, ages, field names, status codes), not prose.
- **验收标准**: testable and scenario-based (e.g. 「清 Cookie、改地区、改文案版本、过期四种情况都会重新弹出」); write `—` when none applies. Do not leave the column empty on P0 rows.
- **对参考文件的修正/备注**: wherever a row corrects or extends an earlier source or a prior version, state it explicitly (e.g. `原文件漏了 X` / `参考文件未覆盖` / `增加了 Y` / `补 Z`). Self-review must surface and flag omissions, never silently patch them.
- **文案英文基线**: write usable English copy with `{VARIABLES}` and `[PLACEHOLDERS]`; tag full drafts as `已起草：xxx.docx` / `待起草` / `(Subject to legal review)`.
- **法务半成品剥离**: Terms / Privacy / Cookie / data-retention counsel drafts are separate inputs, not rows in these three sheets.
- **列按 sheet 定制**: columns differ per sheet; do not force one uniform column set across all sheets.

Priority meanings:

- `P0`: release blocker, material enforcement/safety risk, or critical user-rights failure.
- `P1`: required or high-value remediation scheduled immediately after blockers.
- `P2`: SEO, trust, maintainability, or experience improvement.
- `N/A`: assessed and inapplicable, with reason.

Legal status values:

- `Not reviewed`
- `Counsel question open`
- `Draft for counsel`
- `Counsel approved`
- `Implementation deviates from approved text`
- `Not applicable`

Part (execution owner) values:

- `技术排版` — technical implementation (engineering).
- `UI 设计排版` — UI/design collaboration.
- `运营排版` — operations self-service.

## Copy standard

For every copy item, include:

- `Copy ID`
- Exact placement and trigger.
- Audience and jurisdiction.
- English copy.
- Dynamic variables in `[BRACKETS]`.
- Whether it is operational microcopy, disclosure, FAQ/support copy, or legal-policy draft.
- Source rationale without suggesting the source text was copied.
- Owner, reviewer, approval state, version date, and linked QA case.

Do not label wording `FTC compliant`, `CCPA compliant`, `ADA compliant`, or equivalent unless qualified counsel or the relevant accountable reviewer has approved that claim. Prefer `drafted to address [identified requirement]`.

## Policy document structure · 政策文档结构（Terms / Privacy / Cookie）

When producing a Terms of Service, Privacy Policy, Cookie Policy, or similar legal-policy draft, follow this skeleton and these conventions.

### Document skeleton · 文档骨架

1. Title (e.g. `[Product] Privacy Policy`).
2. Subtitle: `Draft for legal review. Highlighted text in [brackets] must be completed or confirmed before publication.`
3. `Last Updated: [EFFECTIVE DATE]`.
4. For age-restricted or high-sensitivity products: a prominent warning banner; for Privacy, a `Key Points` bullet block (the 4–6 sentence "in short" version).
5. Numbered sections in a fixed order. Terms: Who We Are → Eligibility/Age/Location → Accounts → Content → Free/Paid → License & Restrictions → Feedback/Material → IP/Copyright → Reporting → Privacy → Third-Party → Suspension/Termination → Disclaimers → Liability → Governing Law/Disputes → Changes → General → Contact. Privacy: Key Points → Who We Are → Information We Collect → How We Use & Legal Bases → What We Do Not Do → Video Viewing Privacy → How We Disclose → Cookies → Retention → Where We Process → Rights → Minors → Security → Automated Processing → Changes → Contact.
6. End with a `Notes for Legal Review (delete before publication)` section.

### Conventions · 规范

- **Placeholders**: every unresolved fact (emails, dates, URL, court, file number, hosting regions, DPO/Privacy-Officer name/title) goes in `[BRACKETS]` and is a launch blocker. A fully-bracketed sentence is conditional — keep it only if the referenced feature ships, otherwise delete it.
- **Tables for structured data**: data categories, purpose + legal basis, recipients, and retention periods go in tables, not prose.
- **Legal-basis table**: for Privacy, list each purpose with its GDPR Art. 6(1)(a)–(f) basis, and state the Canada consent basis separately.
- **Retention table**: one row per data type with a specific period, plus a "may keep longer where the law requires" clause.
- **Negative lists**: for age-restricted or high-sensitivity products, include explicit "what we do NOT collect" and "what we do NOT do" lists (no ID/selfie/DOB, no sell/share/targeted ads, no session recording, no AI training on user data, no automated significant decisions, no viewing history linked to account).
- **Jurisdiction carve-outs**: explicit clauses for Quebec (French version, CPA s. 11.1/11.2, Law 25 Privacy Officer + location-tech disclosure + de-indexing right), California (CCPA categories + § 1789.3 contact + "do not sell"), Ontario (arbitration restriction), Utah, Canada (implied consent, OPC/provincial commissioners), and the open U.S. state privacy laws. Cross-reference checklist decision IDs.
- **Product-state truthfulness**: every clause matches the actual product state (free vs paid, comments/uploads, viewing history, sign-in method, ad SDKs). No aspirational clauses. Bracketed security/analytics sentences are kept only if engineering confirms the feature is in place.
- **Entity/contact consistency**: use the exact legal entity (name, address, ID, registration) everywhere; define the functional email roles once (support, legal, privacy, copyright, safety, and others as applicable) and reuse.
- **Cross-referencing**: incorporate sibling policies by name ("our Content Standards … form part of these Terms"), and keep page names identical across the Footer, the /legal hub, and every policy. Flag any name mismatch for resolution.
- **Synthetic-media and age-gate protective clauses**: "do not train AI on Content", "do not create synthetic-media likenesses of real people", "do not bypass the age gate", "do not provide to minors", "no location-disguising tools", "age confirmation is self-reported and false information is a breach", and a video-viewing-privacy clause stating viewing info is not disclosed except as required by law.

### Notes for Legal Review · 法务审阅备注（决策日志）

Always end the document with `Notes for Legal Review (delete before publication)`. Each note must:

1. Cross-reference the checklist decision ID (`L-xx` / `D-xx` / `C-xx`).
2. State the legal reasoning behind a specific choice (why a clause is included, omitted, or consumer-friendly).
3. Flag anything counsel must decide (e.g. special-category-data status, DPIA, arbitration vs no-arbitration).
4. Flag inconsistencies (page naming, retention values vs engineering config) to resolve.
5. Say `delete before publication`.

## UI/frontend backlog view

`编号 / Component / User and region / Entry point / Trigger / States and error paths / Actions / PC-mobile behavior / Authentication state / Copy ID / Consent-storage behavior / Accessibility / SEO metadata or schema / Frontend notes / Backend/vendor dependency / Analytics requirement / Acceptance criteria / Priority / Owner`

Common components, only when applicable:

- Age or access restriction.
- Cookie banner and preference center.
- Do Not Sell or Share / targeted-ad opt-out / GPC handling.
- AI, synthetic-content, affiliate, sponsored, or commercial disclosure.
- Impersonation, synthetic-media, copyright, and safety reporting.
- Data-rights intake and identity verification.
- Subscription disclosure, checkout consent, cancellation, refund, and renewal notices.
- Footer legal navigation, author/reviewer module, schema, structured metadata, and accessibility controls.

Every component needs positive, negative, failure, retry, and withdrawal/cancellation states where relevant.

## Operations copy and mock-material view

`Material ID / 编号 or Copy ID / Material / Purpose / Production or test / Required real inputs / Allowed placeholders / Prohibited fabrication / Owner / Reviewer / Due state / Destination`

Include as applicable:

- Terms, Privacy, Cookie, DMCA, content-safety/removal, subscriptions/cancellation/refund, accessibility, and community rules.
- Footer labels, modal copy, form consent, confirmation/error messages, FAQ, cancellation instructions, data deletion, and reporting/support scripts.
- Author/reviewer biography input forms, genuine credentials, profile media rights, company/contact records, vendor lists, retention schedules, and consent/content provenance records.
- Test accounts, sample characters or titles, sample reports, sample receipts, and review-environment content clearly marked `SAMPLE` or `TEST ONLY`.

## Launch QA matrix

`QA ID / 编号 / Jurisdiction / Device-browser / Account state / Consent state / Scenario / Steps / Expected copy / Expected behavior / Evidence artifact / Result / Defect owner / Retest date`

Minimum scenarios, when applicable:

- First visit, return visit, cleared storage, withdrawal, and GPC.
- Eligible user, minor, refusal, verification failure, vendor timeout, and regional mismatch.
- Crawler behavior, robots/noindex, canonical, sitemap, video metadata, and duplicate templates.
- Accept all, reject all, granular choices, and preference persistence.
- Signup, marketing opt-in, checkout disclosure, renewal notice, cancellation, refund, and payment failure.
- Logged-out reporting, report receipt, escalation, appeal, duplicate/re-upload handling, and SLA evidence.
- Access, correction, export, deletion, and identity-verification failure.
- Keyboard navigation, focus, screen-reader name/role/state, contrast, zoom, captions/transcripts, and error messaging.

## Final response pattern for each stage

Lead with:

1. `Stage result`: what is now decided or produced.
2. `Evidence boundary`: what was verified, inferred, blocked, or still stale.
3. `Human check`: the exact rows or questions a person must review.
4. `Next gate`: the one decision or input needed before advancing.

Do not bury a missing URL or business-critical fact at the end of a long report.
