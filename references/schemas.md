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

## Master execution checklist

Use one row per independently testable obligation or recommendation:

`Requirement ID / Copy ID / Module or page / Trigger and audience / Jurisdiction / Applicability condition / Evidence class / Compliance or SEO type / Part / Requirement / Mandatory English copy or placeholder / Dynamic variables / UI behavior / Frontend/backend implementation / Operations material / Official source / Competitor evidence / Target current state / Gap / Red flag or non-compliance risk / Priority / Owner / Legal status / QA acceptance / Not-applicable reason / Last verified`

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

## UI/frontend backlog view

`Requirement ID / Component / User and region / Entry point / Trigger / States and error paths / Actions / PC-mobile behavior / Authentication state / Copy ID / Consent-storage behavior / Accessibility / SEO metadata or schema / Frontend notes / Backend/vendor dependency / Analytics requirement / Acceptance criteria / Priority / Owner`

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

`Material ID / Requirement ID or Copy ID / Material / Purpose / Production or test / Required real inputs / Allowed placeholders / Prohibited fabrication / Owner / Reviewer / Due state / Destination`

Include as applicable:

- Terms, Privacy, Cookie, DMCA, content-safety/removal, subscriptions/cancellation/refund, accessibility, and community rules.
- Footer labels, modal copy, form consent, confirmation/error messages, FAQ, cancellation instructions, data deletion, and reporting/support scripts.
- Author/reviewer biography input forms, genuine credentials, profile media rights, company/contact records, vendor lists, retention schedules, and consent/content provenance records.
- Test accounts, sample characters or titles, sample reports, sample receipts, and review-environment content clearly marked `SAMPLE` or `TEST ONLY`.

## Launch QA matrix

`QA ID / Requirement ID / Jurisdiction / Device-browser / Account state / Consent state / Scenario / Steps / Expected copy / Expected behavior / Evidence artifact / Result / Defect owner / Retest date`

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
