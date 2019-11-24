import pytest
import json

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_home(client):
    rv = client.get('/')
    assert b'Boulou' in rv.data


def test_get_all_route(client):
    resp = client.get('/pokemon')
    data = json.loads(resp.data)
    assert len(data['items']) == 964
