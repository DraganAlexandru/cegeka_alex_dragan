import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Alex Dragan CV!' in response.data


def test_get_personal_info(client):
    response = client.get('/personal')
    assert response.status_code == 200
    assert b'name' in response.data
    assert b'email' in response.data
    assert b'phone' in response.data


def test_get_experience_info(client):
    response = client.get('/experience')
    assert response.status_code == 200
    assert b'position' in response.data
    assert b'company' in response.data
    assert b'year' in response.data


def test_get_education_info(client):
    response = client.get('/education')
    assert response.status_code == 200
    assert b'degree' in response.data
    assert b'university' in response.data
    assert b'year' in response.data


def test_invalid_route(client):
    response = client.get('/invalid_route')
    assert response.status_code == 404


if __name__ == '__main__':
    pytest.main()
