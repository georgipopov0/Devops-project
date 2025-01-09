import pytest
from app.main import app

def test_hello():
    test_client = app.test_client()
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevOps!"}
