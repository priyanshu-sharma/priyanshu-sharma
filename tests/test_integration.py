import pytest


@pytest.mark.anyio
async def test_ui_root(client):
    """Verify that the FastHTML UI root is accessible."""
    response = await client.get("/")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_api_health(client):
    """Verify that the FastAPI endpoint is accessible via /api/health."""
    response = await client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
