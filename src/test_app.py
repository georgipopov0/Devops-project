from app import app


def test_hello():
    # We use the test client provided by Flask
    test_client = app.test_client()
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevOps!"}
