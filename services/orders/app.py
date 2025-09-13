from fastapi import FastAPI

app = FastAPI(title="orders")

@app.get("/healthz")
def health():
    return {"ok": True}

@app.get("/orders")
def list_orders():
    # trivial payload to keep baseline simple
    return {"orders": [{"id": 1, "status": "new"}]}
