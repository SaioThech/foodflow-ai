from api.main import health


def test_health_endpoint_payload():
    assert health() == {"status": "ok", "service": "foodflow-ai"}
