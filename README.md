# NetMetrics C2 Telemetry Relay & Edge Node Pipeline

[![CI/CD Pipeline](https://github.com/netmetrics-net/c2-deploy-pipeline/actions/workflows/deploy.yml/badge.svg)](https://github.com/netmetrics-net/c2-deploy-pipeline/actions/workflows/deploy.yml)
[![Version](https://img.shields.io/badge/version-2.4.1-blue.svg)](https://github.com/netmetrics-net/c2-deploy-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Coverage](https://img.shields.io/badge/coverage-94.8%25-brightgreen.svg)](https://github.com/netmetrics-net/c2-deploy-pipeline)

Automated continuous integration and edge deployment pipeline for NetMetrics distributed telemetry collection agents. This service coordinates real-time telemetry forwarding from regional worker clusters to central telemetry ingestors.

---

## Architecture Overview

```text
+-------------------+       +-----------------------+       +-------------------------+
| Regional Edge Node| ----> | Telemetry Relay Agent | ----> | Central InfluxDB Cluster|
| (CPU/Mem/Net Poll)|       | (Encrypted mTLS Sync) |       | (Time-Series Analytics) |
+-------------------+       +-----------------------+       +-------------------------+
                                        ^
                                        |
                            +-----------------------+
                            | GitHub CI/CD Pipeline |
                            | (Automated Edge Deploy|
                            +-----------------------+
```

---

## Deployment & Pipeline Security

- **Target Nodes:** Regional edge clusters in APAC (ID-JKT, SG-SIN, JP-TYO).
- **Security Protocols:** All edge node synchronizations require valid API credentials securely supplied via CI/CD platform secrets (`C2_API_KEY`).
- **Audit Policy:** In compliance with SOC2 Type II, production keys are strictly managed by GitHub Actions Secrets and must never be committed to repository branches.

---

## Local Development & Testing

```bash
# Clone the repository
git clone https://github.com/netmetrics-net/c2-deploy-pipeline.git
cd c2-deploy-pipeline

# Run unit tests
make test

# Start local test container
docker compose up -d
```
