from app.main import app

def test_homepage():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_chat():
    client = app.test_client()
    res = client.post("/chat", json={"message": "hello"})
    assert res.status_code == 200
    assert "reply" in res.get_json()
