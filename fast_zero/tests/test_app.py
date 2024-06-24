from http import HTTPStatus


def test_read_root_status_ok(client):
    # client = TestClient(app)  # Arrange
    res = client.get('/')  # Act
    assert res.status_code == HTTPStatus.OK  # Assert
    assert res.json() == {'message': 'Olá mundo'}


def test_create_user(client):
    res = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'password',
            'email': 'test@test.com',
        },
    )
    assert res.status_code == HTTPStatus.CREATED
    assert res.json() == {
        'username': 'testusername',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    res = client.get('/users/')
    assert res.status_code == HTTPStatus.OK
    assert res.json() == {
        'users': [
            {
                'username': 'testusername',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    res = client.put(
        '/users/1',
        json={
            'password': 'password',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert res.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_unable_update_user(client):
    res = client.put(
        '/users/2',
        json={
            'password': 'password',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert res.status_code == HTTPStatus.NOT_FOUND
    assert res.json() == {'detail': 'User not found'}


def test_delete_user(client):
    res = client.delete('/users/1')
    assert res.status_code == HTTPStatus.OK
    assert res.json() == {'message': 'User deleted'}


def test_unable_delete_user(client):
    res = client.delete('/users/2')
    assert res.status_code == HTTPStatus.NOT_FOUND
    assert res.json() == {'detail': 'User not found'}
