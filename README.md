Reference Architecture (GitHub Advanced Security + Azure AI Foundry)

Overview:
-This repository documents a reference architecture for an AI-assisted, governance-first DevSecOps security triage agent built using Azure AI Foundry and GitHub Advanced Security (GHAS).
-The solution demonstrates how organizations can use AI to analyze, correlate, and prioritize SDLC security signals—such as CodeQL findings, secret scanning alerts, and dependency vulnerabilities—while maintaining human oversight, auditability, and strong governance boundaries.
-The architecture is intentionally designed for regulated and enterprise environments, where security teams must balance automation with control, traceability, and risk management.

TL;DR

-Built: Read-only AI security triage agent (Azure AI Foundry + GitHub Advanced Security / CodeQL)
-Does: Summarizes and prioritizes security findings and produces remediation guidance
-Why: Reduces alert fatigue, standardizes security reviews, and improves SDLC security posture without introducing autonomous enforcement risk


Problem Statement:
-Modern engineering organizations face systemic challenges in SDLC security operations:
-Alert fatigue from GitHub Advanced Security (SAST, code scanning, secret scanning)
-Untriaged Dependabot alerts accumulating across repositories
-Security findings lacking context, ownership, or prioritization
-Inconsistent and ad-hoc security reviews across teams
-Limited ability to reason about overall security posture rather than individual alerts


*While organizations may already have strong tools in place, security intelligence remains fragmented and difficult to operationalize at scale.*

Solution Overview:
-This architecture introduces an AI Security Architect Agent that acts as a read-only intelligence layer across existing GitHub security signals.
-The agent does not replace existing scanners or tools. Instead, it:
-Aggregates security signals across repositories
-Interprets findings in architectural and organizational context
-Produces prioritized, human-readable remediation guidance
-Supports security, engineering, and governance stakeholders
-Architecture Principles


This reference architecture is guided by the following principles:
-Read-only by design – no autonomous code changes or enforcement
-Identity-aware access – OAuth-based authentication, no static secrets
-Governance-first – auditability, traceability, and human decision ownership
-Composable intelligence – works across existing GitHub security tooling
-Future-aligned – designed to evolve toward stricter least-privilege models


High-Level Architecture:
-Core Components
-GitHub Organization / Repositories
-Source code, pull requests, and workflows
-GitHub Advanced Security signals:
-Code scanning (CodeQL)
-Secret scanning
-Dependabot alerts
-MCP-Based GitHub Connector
-Mediates all access to GitHub APIs
-Exposes security and repository metadata as structured tools
-Enforces scoped access and identity propagation
-AI Security Architect Agent (Azure AI Foundry)



Interprets security signals in context of:
-Repository
-Team
-Service boundaries
-Aggregates and prioritizes findings
-Generates remediation guidance and reports
-Client Surfaces (Optional)
-CLI or chat interface for engineers
-Scheduled reports for security and governance teams
-PR review or GitHub Checks integrations (advisory only)
-Authentication, Permissions, and Governance Model


Current State (Documented Reality)
-Access to GitHub is handled via OAuth identity passthrough using the Microsoft Foundry Agent Service MCP GitHub App.
-Because this GitHub App is publisher-managed, its permission set is broader than strictly required for this specific use case and cannot currently be reduced by consumers.
-This is a known and explicitly documented constraint of the current integration model.


Compensating Controls (Implemented)
-To mitigate this constraint, the architecture applies multiple compensating controls:
-Operationally read-only agent behavior instructions built into the AI Agent 
-No modification of code, workflows, issues, PRs, or repository settings
-Explicit repository allowlisting
-Agent scope restricted to approved repositories only
-Scoped MCP access
-Only security findings and repository metadata are consumed
-No credential materialization
-No PATs, secrets, or tokens stored by the agent
-Auditability
-Agent interactions and outputs are logged for traceability and review
-These controls limit blast radius and ensure the agent functions as an advisor, not an actor.



Future State (Target Architecture)
-The long-term target state for this architecture is:
-True least-privilege, read-only GitHub access
-Consumer-scoped permissions for MCP connectors
-Fine-grained API exposure aligned to security-only use cases
-First-class support for security posture aggregation



*This reference architecture is intentionally designed so that no core logic changes are required when finer-grained permissions become available.*

Example Capabilities:

“Provide a prioritized list of the top security risks across all payment-related repositories.”

“Summarize new high-severity Dependabot alerts this week and group them by owning team.”

“Review this pull request for common security anti-patterns, referencing existing GHAS findings.”

“Generate a weekly executive summary of SDLC security posture and trends.”



*These scenarios demonstrate how AI can act as a Security Architect co-pilot embedded in the SDLC, rather than another standalone dashboard.*



***Disclaimer***
This repository includes intentionally vulnerable demo code under demo_vulns/ to generate CodeQL findings for triage demonstrations.
These patterns are for demonstration only and must not be used in production systems.




Summary:
-This reference architecture demonstrates how AI can be safely integrated into SDLC security workflows by:
-Treating AI as a reasoning and prioritization layer
-Preserving human accountability and governance
-Explicitly documenting constraints and tradeoffs
-Designing for future least-privilege enforcement

It reflects real-world enterprise conditions and provides a practical, extensible foundation for AI-assisted security operations at scale.




