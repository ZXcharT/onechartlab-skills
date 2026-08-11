<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/onechart-symbol-white.svg">
    <img src="assets/brand/onechart-symbol-black.svg" width="88" height="88" alt="OneChart">
  </picture>
</p>
<h1 align="center">OneChartLab Skills</h1>
<p align="center">An open-source OneChart project for auditable AI Agent collaboration</p>
<p align="center"><a href="README.md">简体中文</a></p>

## What is Agent Cowork Control?

> When work benefits from several Agents sharing responsibility, this Skill helps the lead Agent define the plan, delegate tasks, and check the result.

When installed in a tool that supports subagents, it can help the lead Agent:

- show you a plan and wait for confirmation before starting important work;
- assign research, file editing, and checks to different helper agents;
- report unavailable tools, insufficient permissions, or unreliable evidence;
- verify files, data, and tests before delivery;
- keep one main Agent responsible for the final result.

It is not a standalone application. It is a working method for AI agents.

## Good use cases

Examples include:

- researching a company or industry across news, filings, financials, and reports;
- preparing a local project for a public GitHub release;
- building a report, website, or tool that spans multiple files and checks;
- independently reviewing an important result for omissions;
- work that combines research, execution, and final verification.

## When it should not start

It is normally unnecessary for:

- casual conversation or simple questions;
- translation, rewriting one sentence, or explaining a concept;
- reading or summarizing one file;
- a small, clearly scoped edit;
- work one Agent can finish quickly.

## Is it automatic?

In tools that can load Skills automatically, an Agent may use it when delegation would clearly help. You do not need to mention its name every time.

If it does not start automatically, simply say:

> This task would benefit from delegation. Please use Agent Cowork Control.

It is not a background service and does not run on a schedule. For important work or actions that may affect external systems, the lead Agent shows a plan and waits for approval. Installing the Skill does not authorize automatic publishing, permission expansion, dependency installation, or account access.

## Installation

For HanaAgent, the simplest method is to send it this repository URL:

```text
https://github.com/ZXcharT/onechartlab-skills
```

Then say:

> Open this repository and install the Agent Cowork Control Skill inside it.

HanaAgent will locate the Skill in the repository and install it.

If the current Agent cannot install from a GitHub repository, download `agent-cowork-control.skill` from the Release page, drag it into the chat, and ask the current Agent to install it. See [Installation, updates, and removal](docs/INSTALLATION.md) for other methods.

## First use

No special command syntax is required. Ask for the real task, for example:

> Prepare this project for open source. Confirm the plan first, then delegate research, edits, and checks where useful.

You can also ask for evidence-heavy research:

> Research this company across multiple sources. Separate the key conclusions, supporting evidence, and remaining uncertainty.

When the lead Agent determines that delegation would help, it will show a plan first. Work begins after you approve it.

## Learn more

Most users can stop here. The following documents cover installation details, internal behavior, compatibility, and maintenance:

- [Installation, updates, and removal](docs/INSTALLATION.md)
- [How it works](docs/HOW-IT-WORKS.md)
- [Platform compatibility](docs/COMPATIBILITY.md)
- [Advanced HanaAgent setup](docs/HANAAGENT-SETUP.md)
- [Security policy](SECURITY.md)
- [Contributing](CONTRIBUTING.md)
- [Project standards](docs/STANDARDS.md)
- [Rule mapping](docs/RULE-MAPPING.md)
- [Maintainer release process](docs/RELEASE.md)
- [Changelog](CHANGELOG.md)

## License

Code and documentation are available under the [MIT License](LICENSE), © 2026 ZXcharT. The OneChart, OneChartLab, and ZXcharT names and logos are excluded from the MIT grant; see [TRADEMARKS.md](TRADEMARKS.md).
