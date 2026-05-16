from app.client import fetch_url

def test_fetch_url():
    status = fetch_url("https://example.com")

    assert status == 200
