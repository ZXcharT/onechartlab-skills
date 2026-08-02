# OneChartLab Skills

[简体中文](README.md)

## What is Agent Cowork Control?

> It helps an AI handle large tasks by planning first, delegating clear parts of the work, and checking the result before delivery.

After installation, it can help HanaAgent:

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

After installation, HanaAgent will try to use it for complex tasks. You do not need to mention its name every time.

If it does not start automatically, simply say:

> This task is complex. Please use Agent Cowork Control.

It is not a background service and does not run on a schedule. For important work or actions that may affect external systems, it shows a plan and waits for approval. Installing the Skill does not authorize automatic publishing, permission expansion, dependency installation, or account access.

## Installation

The simplest installation uses the official release asset:

```text
agent-cowork-control.skill
```

Drag the `.skill` file into a HanaAgent chat, then send:

> Install this Skill.

If a Release download is not available yet, install from source by following [Installation, updates, and removal](docs/INSTALLATION.md).

## First use

No special command syntax is required. Ask for the real task, for example:

> Prepare this project for open source. Confirm the plan first, then delegate research, edits, and checks where useful.

You can also ask for evidence-heavy research:

> Research this company across multiple sources. Separate the key conclusions, supporting evidence, and remaining uncertainty.

HanaAgent will show a plan first when the task is complex enough. Formal execution begins after you approve it.

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

Code and documentation are available under the [MIT License](LICENSE), © 2026 ZXcharT.
