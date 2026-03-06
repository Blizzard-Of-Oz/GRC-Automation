# Product Scope: On-Prem Continuous Compliance Automation Platform

## Product Purpose
Build an on-prem automation layer that continuously collects technical evidence, evaluates control compliance, and synchronizes governance outcomes to **Eramba** (which remains the GRC system of record).

## MVP Goals
1. Build a stable backend foundation for evidence ingestion and compliance evaluation.
2. Implement a normalized internal evidence model and pipeline.
3. Create a rules evaluation framework for automated control checks.
4. Persist evidence and rule outcomes in PostgreSQL.
5. Synchronize summarized compliance outcomes into Eramba.
6. Operate fully on-prem via Docker Compose for initial deployment.

## Non-Goals (for MVP)
- Rebuilding Eramba.
- Rebuilding third-party systems (Fleet, osquery, Wazuh, OpenSCAP, scanners, IAM/Directory platforms).
- Building a full frontend UI.
- Implementing full authentication/authorization stack.
- Splitting into microservices or adding Kubernetes orchestration.

## First Recommended Connector
**Fleet (osquery manager)**

Why first:
- High-value endpoint visibility.
- Structured data model that is practical to normalize.
- Good starting point for recurring technical evidence collection.

## First Recommended Controls to Automate
1. **Endpoint encryption enabled** (device-level encryption evidence).
2. **Critical patch currency** (OS patch lag/SLA).
3. **EDR/agent presence and health** (security telemetry coverage).
4. **Local admin restrictions** (least-privilege posture checks).
5. **Host firewall enabled** (baseline endpoint hardening).

These controls are generally measurable from endpoint tooling and provide immediate audit/compliance value.
