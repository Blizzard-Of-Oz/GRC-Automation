# Architecture Notes (Initial Scaffold)

- **Monolith-first approach:** keep a single backend service for MVP speed and operational simplicity.
- **Clean boundaries:** separate API, domain, connectors, normalization, rules, and sync concerns.
- **On-prem design:** all required runtime dependencies can be deployed via Docker Compose.
- **Eramba as system of record:** this platform only automates evidence and control outcomes.
