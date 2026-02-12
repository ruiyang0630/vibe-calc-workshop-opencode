from fastapi.testclient import TestClient
# 注意：重構後 AI 會自動修正這裡的 import 路徑
from main import app

client = TestClient(app)

def test_add():
    response = client.get("/add/10/20")
    assert response.status_code == 200
    assert response.json() == {"result": 30}

def test_multiply():
    response = client.get("/multiply/6/7")
    assert response.status_code == 200
    assert response.json() == {"result": 42}
