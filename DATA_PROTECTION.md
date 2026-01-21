# Data Protection & Compliance Framework (Annie)
## Global Standards Alignment (v1.0)

Annie is built to handle sensitive IP (Scripts, Brand Personalities, Creative Strategies). This document outlines the technical safeguards implementing **GDPR**, **Nigeria Data Protection Regulation (NDPR)**, and **ISO 27001** principles.

### 1. Data Classification
| Data Type | Sensitivity | Storage Strategy | Retention |
|-----------|-------------|-------------------|-----------|
| User Profiles | High | Relational (PostgreSQL) - Encrypted | Permanent (until deletion) |
| Script Drafts | Critical | Document Store (MongoDB) - AES-256 | Optional "Zero-Retention" Mode |
| Voice Vault (Embeddings) | Critical | Vector DB (Pinecone Private) | Permanent for Brand Persona |
| Research Data | Low | Cache / S3 | Transient |

### 2. Privacy by Design
- **Zero-Retention Mode**: For high-security corporate clients (e.g., Tesla), AI processing happens in stateless containers. No script data is stored after the session ends.
- **VPC Isolation**: The core AI engine (LangChain/Python) runs within a private subnet, shielded from the public internet.
- **Anonymization**: PII (Personally Identifiable Information) is automatically scrubbed from scripts before being sent to 3rd party LLM providers (Claude/Gemini) if "Privacy Shield" is active.

### 3. Compliance Checklist
- [x] **GDPR**: Right to erasure, Data portability, Consent logs.
- [x] **NDPR**: Local node replication (optional), Data Protection Officer (DPO) portal.
- [x] **WCAG 2.1**: Screen reader compatibility, Keyboard-only navigation for the entire editor.
- [x] **ISO 27001**: Role-based Access Control (RBAC), Audit logs for all file exports.

### 4. Technical Safeguards
- **Encryption**: TLS 1.3 for data in transit; AES-256 for data at rest.
- **Authentication**: Multi-Factor Authentication (MFA) required for "Brand Manager" roles.
- **Audits**: Quarterly penetration testing and automated vulnerability scanning (GitHub Advanced Security).
