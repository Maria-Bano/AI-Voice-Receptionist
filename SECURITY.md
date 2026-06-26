# Security Policy

## Overview

This is a **public portfolio repository** for the AI Voice Receptionist project. It documents architecture, engineering decisions, and case study materials. It is **not** a production deployment and does not contain live credentials or operational systems.

Security in this context means:

1. Protecting proprietary implementation assets that are intentionally kept private
2. Preventing accidental exposure of credentials or customer data in portfolio materials
3. Providing a clear process for reporting legitimate security concerns

---

## Supported Versions

| Version | Supported |
|---------|-----------|
| Portfolio documentation (latest on `main`) | ✅ Actively maintained |
| Production deployment | ❌ Not hosted in this repository |

---

## No Credentials Policy

**Never commit the following to this repository:**

- API keys, tokens, or secrets
- `.env` files or environment configuration with real values
- Webhook URLs containing authentication tokens
- Service account JSON or credential files
- Production n8n workflow exports with embedded credentials
- Proprietary prompts or system instructions
- Customer, guest, or reservation data
- Real production dashboard screenshots without sanitization

The `.gitignore` is configured to block common secret file patterns. Contributors are responsible for reviewing diffs before opening pull requests.

If credentials are accidentally committed:

1. **Revoke and rotate** the exposed credential immediately
2. **Remove** the secret from git history if possible
3. **Report** via the process below so the maintainer is aware

---

## Protection of Proprietary Assets

The following assets are proprietary and intentionally excluded from this repository:

| Asset | Status |
|-------|--------|
| Production n8n workflows | Private |
| Vapi agent prompts and tuning | Private |
| Availability engine business rules | Private |
| Live Google Sheets / PMS connections | Private |
| Webhook endpoints and API integrations | Private |

Portfolio documentation describes **patterns and architecture** — not implementation internals. Do not request or submit these materials via issues or pull requests.

---

## Reporting a Vulnerability

If you discover a security issue related to this repository — including accidentally exposed credentials in commits, issues, or pull requests — please report it responsibly.

### How to report

1. **Do not** open a public GitHub issue for security-sensitive findings
2. Email the maintainer directly at: `[your.email@example.com]` <!-- Replace before publish -->
3. Include:
   - Description of the issue
   - Steps to reproduce (if applicable)
   - Affected files or commits
   - Your recommended remediation (if known)

### What to expect

| Timeline | Action |
|----------|--------|
| Within 48 hours | Acknowledgment of your report |
| Within 7 days | Initial assessment and response |
| After resolution | Confirmation and coordinated disclosure if applicable |

### Scope

**In scope:**

- Credentials or secrets committed to this repository
- Customer or PII data accidentally published in portfolio materials
- Security misconfigurations in publicly committed files

**Out of scope:**

- Vulnerabilities in third-party platforms (Vapi, n8n, Google) — report to those vendors directly
- Social engineering or physical security
- Proprietary production systems not hosted in this repository

---

## Safe Contribution Practices

Before submitting documentation changes:

- [ ] No real API keys, tokens, or webhook URLs in text or images
- [ ] Screenshots are sanitized per [docs/demo-checklist.md](docs/demo-checklist.md)
- [ ] No n8n workflow JSON files committed
- [ ] No proprietary prompts or business logic included
- [ ] No real guest or customer data in examples

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

## Contact

**Security reports:** `[your.email@example.com]` <!-- Replace before publish -->

**General inquiries:** See [README.md](README.md#contact)
