# sl_job

A vulnerable Python job-processing environment designed for:

- CVE validation workflows
- SBOM generation and comparison
- HTTP client security testing
- Dependency remediation validation
- POWER vs x86 scan comparison

This repository intentionally includes vulnerable versions of
`idna` and `requests` to simulate realistic enterprise API
and background job-processing environments.

---

## 🎯 Purpose

`sl_job` is designed to validate:

- Vulnerability scanner behavior
- Python dependency analysis
- SBOM tooling consistency
- HTTP client security findings
- Remediation workflow verification

---

## 📦 Vulnerable Packages

| Package | Version | Vulnerability |
|---|---|---|
| idna | 3.6 | CVE-2024-3651 |
| requests | 2.32.2 | CVE-2024-47081 |
| requests | 2.32.2 | CVE-2026-25645 |

---

## 🧱 Repository Goals

This repository is used for:

- CVE reproducibility testing
- dependency graph validation
- SBOM drift comparison
- HTTP library remediation testing
- architecture-specific vulnerability analysis

---

## 🐳 Build Image

```bash
docker build -t sl-job .
