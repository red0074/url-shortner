import pytest
from app.main import app
from app.models import url_store

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert data["service"] == "URL Shortener API"

def test_shorten_url_success(client):
    url_store.clear()
    response = client.post("/api/shorten", json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert "short_code" in data
    assert "short_url" in data

def test_shorten_url_invalid(client):
    response = client.post("/api/shorten", json={"url": "not-a-valid-url"})
    assert response.status_code == 400
    data = response.get_json()
    assert data["error"] == "Invalid URL"

def test_redirect_and_click_count(client):
    url_store.clear()
    shorten = client.post("/api/shorten", json={"url": "https://example.com"}).get_json()
    short_code = shorten["short_code"]

    # Redirect
    redirect_response = client.get(f"/{short_code}", follow_redirects=False)
    assert redirect_response.status_code == 302
    assert redirect_response.location == "https://example.com"

    # Check click count increment
    stats_response = client.get(f"/api/stats/{short_code}")
    stats = stats_response.get_json()
    assert stats["url"] == "https://example.com"
    assert stats["clicks"] == 1
    assert "created_at" in stats

def test_stats_not_found(client):
    response = client.get("/api/stats/invalid123")
    assert response.status_code == 404
    data = response.get_json()
    assert data["error"] == "Short URL not found"
