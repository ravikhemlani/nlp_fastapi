from starlette.testclient import TestClient
from main import app
import json

client = TestClient(app)


def test_read_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'NLP WebService'}


def test_read_url():
    response = client.get('//url/content')
    assert response.status_code == 200
    assert response.json() == {"detail": "ok"}


def test_create_item():
    body = {"id": 1, "url": "http://samepleurl.com", "entity": "person", "text": "user"}
    body = json.dumps(body)
    response = client.post('/add/', data=body)
    assert response.status_code == 201
