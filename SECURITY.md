# Security Policy

## Supported Versions

This repository is intended for controlled vulnerability testing
and security validation workflows.

Only the latest testing configuration is maintained.

---

## Purpose

`sl_job` intentionally includes vulnerable package versions to support:

- CVE validation
- SBOM generation
- remediation testing
- dependency graph analysis
- scanner verification

---

## Reporting Issues

Please open an issue for:

- broken dependency workflows
- SBOM inconsistencies
- container build failures
- remediation validation issues
- CI/CD scan failures

---

## Security Warning

This repository intentionally contains vulnerable software components.

Do NOT use:
- in production
- on internet-facing systems
- for sensitive workloads

This project is strictly for:
- testing
- research
- validation
- security tooling analysis

---

## Recommended Usage

Use this repository only within:
- isolated lab environments
- CI/CD security pipelines
- controlled container platforms
- local security testing setups
