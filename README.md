# KubeTrace — Starter (Day 1)

Two FastAPI services (orders, payments) in Docker + docker-compose, CI, and a k6 load test to baseline p95 latency.

## Quick Start
```bash
# 1) Build & run
docker compose up --build -d

# 2) Sanity check
curl -s localhost:8001/healthz
curl -s localhost:8002/healthz

# 3) Run k6 baseline (30 VUs, 60s) against /orders
k6 run k6/basic.js

# 4) Record the p95 & error rate in metrics_log.csv
```
> The k6 summary prints `http_req_duration........p(95)=XXX` — that is your p95.

## Make targets (optional)
```bash
make up        # build & start
make down      # stop & remove
make logs      # tail logs
make k6        # run the baseline k6 test
make test      # run pytest
```

## Next Steps (after Day 1)
- Add liveness/readiness probes via Helm, deploy to kind/minikube.
- Add OpenTelemetry + Prometheus/Grafana dashboards.
- Tune requests/limits + add HPA; re-run k6; capture before/after p95.
- Add Prometheus alert + simple runbook.
