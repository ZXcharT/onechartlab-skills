# OneChartLab Skills

[Simplified Chinese](README.md)

OneChartLab Skills is a reviewable, testable, locally packageable collection of Agent Skills. Its first Skill, [**Agent Cowork Control**](skills/agent-cowork-control/SKILL.md), defines planning, delegation, evidence, validation, and communication boundaries for complex HanaAgent work.

## When to use it

Use it for work requiring a six-section Plan, delegated agents, multi-source evidence, multi-module writing, or independent validation. The main Agent retains responsibility for goals, acceptance, and user communication. The Skill requires an explicit delegate identity, least privilege, a structured-tool Canary, isolated run directories, and validation gates.

Do not use it for chat, read-only work, simple questions, research one Agent can complete, or small one-off edits. Skill and prompt gates are policy controls, not claims of system-level enforcement unless the host independently provides it.

## Verification status

| Status | Meaning |
|---|---|
| Runtime target | `agent-cowork-control` is written for HanaAgent semantics. The public candidate passes structure, policy-trace, and package tests; a clean installation check is still required before release. |
| Static reference | Claude Code and Codex are referenced only for open Skill directory formats; runtime behavior is unverified. |
| Unverified | Other Agent runtimes, host tool semantics, and cross-platform execution are not claimed. |

## HanaAgent install and first configuration

1. Copy `skills/agent-cowork-control/` into the HanaAgent Skill directory without changing its directory name or `SKILL.md`.
2. For every approved complex-task Plan, have the request owner or approver explicitly resolve and record `delegate_agent_id`. Never guess, substitute, or silently fall back.
3. Inherit the selected delegate Agent's configured default model. Record an override only after explicit user approval.
4. Set task-level `run_root` to `runs/` under a user-authorized workspace. High-value writing gets one isolated run directory and `FINAL.md`.
5. On first invocation, load resources in this order: `SKILL → task-packets → role protocol → communication protocol` before an event occurs.

## Upgrade, uninstall, troubleshoot

**Upgrade:** replace the whole `skills/agent-cowork-control/` directory. When using the full repository, run `python3 scripts/check_repo.py` from the repository root. Keep local task evidence out of release packages.

**Uninstall:** remove the Skill directory from HanaAgent. Existing task run directories are not removed.

**Troubleshoot:** verify frontmatter name equals directory name; verify host support for creating, continuing, closing, and inspecting delegated threads plus workflow identity semantics; verify the Plan records `delegate_agent_id` and `run_root`. An unavailable structured/MCP tool must result in `BLOCKED`, not a web-source substitute.

## Project documents

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Compatibility](docs/COMPATIBILITY.md) · [Standards](docs/STANDARDS.md) · [Rule mapping](docs/RULE-MAPPING.md) · [Release](docs/RELEASE.md) · [Changelog](CHANGELOG.md)

Run checks with Python standard library only: `python3 scripts/check_repo.py`. Build a local ZIP with `python3 scripts/build_release.py`.

## License and brand

Content is licensed under [MIT](LICENSE), © 2026 ZXcharT. MIT permits use, copying, and modification of the software; it does not grant trademark rights, endorsement, or permission to use ZXcharT, OneChartLab, or related branding. Derived projects must not imply official affiliation.
