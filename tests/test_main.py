from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI!"}
    
def test_read_name():
    response = client.get("/name")
    assert response.status_code == 200
    assert response.json() == {"message": "Christian"}
    
