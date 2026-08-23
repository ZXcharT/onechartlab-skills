# Changelog

## Unreleased

- Redefined collaboration around observable task structure: no collaboration when there is nothing useful to split, light collaboration for ordinary independent work, and controlled collaboration for important, complex, content-heavy or omission-prone tasks.
- Described controlled collaboration to users as enhanced collaboration, with Plan review, clear ownership and handoffs, uninterrupted communication and independent result review.
- Separated project safety controls from collaboration level: formal data, permissions, external systems and high-risk operations follow their own safety rules.
- Made Canary probes depend on call risk, run directories on write/output structure, and `FINAL.md` on handoff needs without automatically escalating collaboration level.
- Added side-by-side user examples and replaced internal governance language in the user guide with direct explanations.

## 0.1.1 — 2026-08-11

- Added direct, light and controlled execution paths; ordinary multi-step single-Agent work uses a brief approved plan without entering controlled collaboration.
- Improved automatic matching for natural requests that explicitly ask multiple Agents or assistants to divide, parallelize or independently check work.
- Escalated light collaboration when risk, write isolation, formal handoff or other controlled conditions appear.
- Made Canary probes, run directories and `FINAL.md` conditional on execution risk, write structure and handoff needs.
- Limited independent review to one Plan review and one result review in controlled collaboration; additional review requires explicit user approval.
- Added task-aware Agent selection with current-role child fallback when no suitable specialist is available.
- Preserved user-selected Agent priority, thread identity, least-privilege access and default-model inheritance.

## 0.1.0 — 2026-08-02

- Published the first OneChartLab Skills repository.
- Added the HanaAgent-targeted Agent Cowork Control Skill and its public protocols.
- Added deterministic T01–T14 behavior tests, repository checks, archive verification and local release tools.
- Added Chinese-first and English user documentation.
- Added plain-language installation, first-use, automatic-use and workflow guides.
- Made “send the repository URL to the Agent” the primary installation method.
- Added an optional advanced HanaAgent setup guide.
- Added MIT licensing, contribution guidance, security policy, compatibility boundaries and rule mapping.
