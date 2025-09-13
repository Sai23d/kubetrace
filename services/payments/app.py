from fastapi import FastAPI

app = FastAPI(title="payments")

@app.get("/healthz")
def health():
    return {"ok": True}

@app.post("/pay")
def pay():
    # accept everything for baseline
    return {"status": "accepted"}
