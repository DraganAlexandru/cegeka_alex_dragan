import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_personal_info(client):
    response = client.get('/personal')
    assert response.status_code == 200
    assert 'name' in response.json
    assert 'email' in response.json
    assert 'phone' in response.json


def test_get_experience_info(client):
    response = client.get('/experience')
    assert response.status_code == 200

    data = response.json
    assert isinstance(data, list)

    for education_item in data:
        assert 'position' in education_item
        assert 'company' in education_item
        assert 'year' in education_item


def test_get_education_info(client):
    response = client.get('/education')
    assert response.status_code == 200

    data = response.json
    assert isinstance(data, list)

    for education_item in data:
        assert 'degree' in education_item
        assert 'university' in education_item
        assert 'year' in education_item


def test_invalid_route(client):
    response = client.get('/invalid_route')
    assert response.status_code == 404


if __name__ == '__main__':
    pytest.main()
