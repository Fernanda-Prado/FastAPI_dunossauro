from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_status_ok():
    client = TestClient(app)  # Arrange
    res = client.get('/')  # Act
    assert res.status_code == HTTPStatus.OK  # Assert
    assert res.json() == {'message': 'Olá mundo'}
