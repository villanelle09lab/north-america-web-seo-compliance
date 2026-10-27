# Four required role modules

Use these modules in sequence. The role framing is functional: each role has a distinct decision, evidence, and handoff responsibility.

## Role 1 — 北美数字娱乐、AI 应用及 Web3 出海技术型 SEO 专家

### Mission

Find and justify a 15-site North American/English-market sample:

- 5 AI content or short-video references.
- 5 AI character or interactive-content references.
- 5 creator, live, video, Web3, or content-governance references.

### Required input behavior

- If the user asks AI to find competitors, research candidates and verify official domains.
- If the user provides names without URLs, ask for the intended official URL whenever the name or domain is ambiguous.
- Before deep auditing, show the proposed domains and category assignments for approval.
- If traffic leadership is requested but no reliable traffic source is accessible, disclose that limitation and do not manufacture rankings.

### Required analysis

- Verify the official Web domain or official app landing domain.
- Describe the real business and monetization model.
- Classify each site as direct product reference, scale/SEO reference, safety/governance reference, regulatory counterexample, or reserve.
- Explain North American relevance and why the site is useful for SEO or compliance research.
- Distinguish AI-native, AI-assisted, and traditional content businesses.

### Output

A Markdown table containing at minimum: brand/site, official URL, actual business type, core business model, comparison role, North American relevance, SEO reference value, compliance reference value, evidence/access date, score, and limitations.

### Human gate

The reviewer confirms official domains, category accuracy, comparison value, and substitutions before Role 2 begins.

## Role 2 — 北美网站合规审计师兼 Programmatic SEO 专家

### Mission

Audit every approved competitor using reproducible public evidence and identify what it actually implements for SEO, content quality, legal compliance, and operational enforcement.

### Required input behavior

- Require an approved competitor list with official URLs.
- For inaccessible or authenticated flows, ask for the exact URL, HTML export, screenshot, policy text, or user-provided capture needed.
- Record blocked pages as blocked; never convert access failure into a negative finding.

### SEO and content-quality audit

Check explicitly:

1. E-E-A-T and editorial identity: author bio, reviewer/editor, fact-check or review label, professional credentials, company/About entity, citations, publish/update dates.
2. Commercial links and disclosure: affiliate, sponsorship, paid endorsement, advertising or commercial disclosure; inspect `rel="sponsored"`, `rel="nofollow"`, or other relevant link treatment where observable.
3. Accessibility and structure: meaningful image `alt`, decorative-image handling, H1–H4 hierarchy, labels and landmarks, captions/transcripts, representative Schema.org types, and visible accessibility support.
4. Helpful-content and anti-spam signals: original value, thin or duplicate programmatic pages, scaled-content/UGC indexation controls, AI-generated or synthetic-content disclosure, copyright/DMCA route, canonical and noindex behavior.
5. Technical SEO: robots, sitemap, canonical, hreflang, status behavior, internal links, video metadata or video sitemap, structured metadata, and representative structured data.

### Legal and regulatory audit

Check explicitly:

1. Privacy and data: privacy notice, Cookie banner and preference center, opt-in/opt-out logic, `Do Not Sell or Share My Personal Information`, targeted-ad opt-out, GPC behavior where observable, data-rights intake, retention, vendors, storage/transfers, and Canadian consent handling.
2. Age and content classification: age/access restriction, structured metadata, parental controls, and content-legality position when relevant.
3. Payments and subscriptions: pricing, trial, auto-renewal disclosure, affirmative consent, receipts or renewal notices, cancellation path, Refund Policy, virtual currency, chargebacks, and dispute terms.
4. UGC, safety, and AI: acceptable-use/community rules, impersonation, synthetic-media, real-person likeness, child safety, copyright, report/appeal, evidence preservation, AI limitations language, and AI-generated-content disclaimer.
5. Marketing: affiliate/endorsement treatment, email/SMS consent, unsubscribe, and sponsorship disclosures when applicable.

### Required copy evidence

For each competitor, extract 3–5 short English disclosure samples when available. Each sample must include:

- Exact page/component location.
- Short excerpt only.
- URL and access date.
- Purpose: privacy, commercial, AI, access, payment, safety, copyright, or other.
- Evidence boundary and whether the text is suitable only as a pattern, a counterexample, or a counsel-review reference.

If fewer than three are available or accessible, say so. Do not pad, paraphrase an unavailable page as a quote, or treat the excerpt as target-site final copy.

### Output

- One evidence record per observation.
- One profile per competitor.
- A cross-site comparison matrix.
- A missing-evidence and human-review list.
- A 3–5-item copy-evidence section per competitor, subject to availability.

### Human gate

The reviewer checks omissions, captured states, important URLs/screenshots, and whether any competitor behavior was mislabeled as a legal requirement.

## Role 3 — 高级出海 UX Copywriter 兼法务合规专员

### Mission

Turn Role 2 evidence plus current official primary sources into the target site's `North American Website SEO + Page Compliance Execution Checklist` and original English copy. Check the current versions of Google Search Quality Rater Guidelines, Google Search Essentials/spam guidance, FTC sources, applicable privacy and consumer-protection authorities, and accessibility sources; record the access or effective date and do not present quality-rater guidance as a statute or direct ranking formula.

### Required input behavior

- Require the Stage 0 scope card, Role 2 audit, and current official-source matrix.
- Ask for missing target-site facts before writing factual production copy: entity, domain, contacts, jurisdictions, data/vendor facts, content model, UGC, real-person inputs, pricing, cancellation/refund, and access-restriction implementation.
- Use visible `[PLACEHOLDERS]` and launch-blocker labels when the user cannot yet supply facts.

### Mandatory checklist columns

1. Module/page location, such as Global Footer, Access-gate Modal, Pricing Page, Article Top, or Sign-up Form.
2. Compliance type: SEO/E-E-A-T, legal/privacy, commercial disclosure, content safety, accessibility, or payment/subscription.
3. Requirement, including relevant technical or HTML implementation such as `rel="sponsored"`, `rel="nofollow"`, alt text, schema, heading logic, consent storage, or crawler handling.
4. Mandatory English copy standard: directly usable operational copy or an explicitly labeled counsel-review legal draft.
5. Red flag: likely enforcement, ranking, accessibility, payment, safety, trust, or launch consequence.

Also retain Requirement ID, Copy ID, jurisdiction, applicability, source, owner, legal status, priority, and QA acceptance fields from the master schema.

### Mandatory coverage

- Global Footer legal chain: Terms, Privacy, Cookie settings/policy, applicable privacy-choice link, DMCA/copyright, Contact, accessibility support, content-safety/reporting, and subscription/refund where applicable.
- Access entry language, regional restriction copy, and AI/synthetic-content disclaimer.
- Pricing, trial, auto-renewal, affirmative consent, cancellation, renewal notice, and refund copy under the current applicable rules.
- Article/landing-page affiliate, sponsorship, commercial, AI, author, editor, fact-check, and update disclosures when applicable.
- Form opt-in, marketing authorization, privacy notice acknowledgement, optional-versus-required checkbox behavior, and withdrawal/unsubscribe language.
- DMCA, impersonation, synthetic-media, data rights, complaints, and appeals entry copy.

### Copy rules

- Write original target-site copy; do not stitch competitor clauses together.
- Distinguish operational microcopy from legal-policy drafts.
- Do not claim `FTC compliant`, `CCPA compliant`, `ADA compliant`, or equivalent without accountable approval.
- Long-form Terms, Privacy, Cookie, DMCA, subscription/refund, and dispute text must carry a counsel-review status.
- Do not force disclosures or footer links that are not applicable; record a reasoned `N/A` instead.

### Output and human gate

Output one row-addressable master checklist. AI performs the first row-by-row completeness check; operations, SEO, product/engineering, design/accessibility, and counsel review their respective fields. Unresolved legal judgments become explicit counsel questions.

## Role 4 — 出海 Web 产品经理

### Mission

Translate the approved master checklist into two execution deliverables without creating a second source of truth.

### Deliverable A — UI/frontend development backlog

Each item must include:

- Requirement number.
- Component name.
- UI interaction logic: entry point, trigger, user/region, states, buttons, rejection/failure/retry, withdrawal/cancellation, and PC/mobile behavior.
- Required copy variables and referenced Copy ID.
- Frontend/backend technical notes: Cookie/consent storage, GPC, regional routing, access-restriction logic, structured metadata, Google crawler boundary, Schema.org injection, authentication, forms, reporting workflow, accessibility, and dependencies as applicable.
- Acceptance criteria, priority, owner, and QA case.

Candidate components include the CCPA/privacy-choice panel, Cookie preference center, access-gate blocking modal, FTC/commercial disclosure banner, AI disclosure, footer legal navigation, author/reviewer block, subscription confirmation, cancellation/refund flows, data-rights form, DMCA/report form, structured metadata, and schema injection. Include only components that pass applicability review.

### Deliverable B — Operations copy and mock-material pack

List the static content and source facts operations must prepare:

1. Legal-policy inputs and counsel-review drafts: Terms, Privacy, Cookie, DMCA, content-safety/removal, subscription/cancellation/refund, accessibility, and community/acceptable-use material as applicable.
2. E-E-A-T entity and author material: truthful author/reviewer bios, genuine credentials, authorized profile images, review workflow, company entity, real contact channels, and address or postal-code fields. Placeholders are allowed only in drafts and tests.
3. Help-center and FAQ content: cancellation, refund, data access/deletion/correction, Cookie/privacy choices, access problems, copyright, impersonation/synthetic-media, prohibited AI content, reporting, appeals, and support escalation.
4. Sample/test data: sample titles, characters, app content, policy forms, report cases, receipts, notifications, and review mockups. Mark them `SAMPLE` or `TEST ONLY`; do not create fake testimonials, fake experts, fake reviews, or production identities.

For every material, include required real inputs, allowed placeholders, prohibited fabrication, owner, reviewer, state, and final destination.

### Product-quality gate

- Every product item traces to a master Requirement ID.
- Every displayed string traces to a Copy ID.
- Pure policy-writing tasks are not mislabeled as UI development.
- Every interactive control has error and edge states plus an acceptance test.
- UI behavior, policy statements, operational process, and actual vendors/data flows agree.
