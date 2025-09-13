# Helm + kind Kit (Orders)

Deploys the **orders** service to a local kind cluster with **readiness/liveness probes**.

## Quick Start (from your repo root, in WSL)
kind create cluster --name kubetrace --config kubetrace_helm_kind_kit/kind/kind-cluster.yaml
docker compose build orders
kind load docker-image kubetrace_starter-orders:latest --name kubetrace
helm install orders kubetrace_helm_kind_kit/charts/orders -n kubetrace --create-namespace
kubectl -n kubetrace port-forward svc/orders 8001:8000 &
curl -s http://localhost:8001/healthz
