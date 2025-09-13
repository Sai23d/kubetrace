import httpx, pytest, time

@pytest.mark.parametrize("port,path", [(8001, "/healthz"), (8002, "/healthz")])
def test_health(port, path):
    # give containers a moment if running locally
    for _ in range(5):
        try:
            r = httpx.get(f"http://localhost:{port}{path}", timeout=2)
            assert r.status_code == 200
            assert r.json().get("ok") is True
            return
        except Exception:
            time.sleep(0.5)
    raise AssertionError("Health endpoint not reachable")
