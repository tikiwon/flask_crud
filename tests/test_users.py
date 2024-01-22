import pytest
from flask.testing import FlaskClient

from run import app


@pytest.fixture
def client():
    return app.test_client()


def test_get_all_users(client):
    resp = client.get('/users')

    # Validate get_users
    assert resp.status_code == 200
    assert isinstance(resp.json, list)

def test_create_users(client):
    resp1 = client.post('/users', json={'id': '1', 'username': 'timoteo', 'email': 'timoteo@gmail.com'})
    resp2 = client.post('/users', data='asd')
    resp3 = client.post('/users', json={'id': '2', 'username': 'timoteokang'})
    resp4 = client.post('/users', json={'username': 'erick', 'email': 'erick@gmail.com'})
    resp5 = client.post('/users', json={'id': '4', 'email': 'morgana@gmail.com'})
    resp6 = client.post('/users', json={'id': 'a', 'username': 'dragon', 'email': 'dragon@gmail.com'})
    resp7 = client.post('/users', json={'id': '1', 'username': ';ladrao', 'email': 'ladrao@gmail.com'})
    resp8 = client.post('/users', json={'id': '3', 'username': 'timoteo', 'email': 'ladrao@gmail.com'})
    resp9 = client.post('/users', json={'id': '3', 'username': 'ladrao', 'email': 'timoteo@gmail.com'})
    #resp10 = client.post('/users', json={'id': '1', 'username': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'email': 'giga@gmail.com'})
    #resp11 = client.post('/users', json={'id': '1', 'username': 'ladrao', 'email': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com'})

    # Validate create user
    assert resp1.status_code == 200
    assert isinstance(resp1.json, dict)

    # Validate missing JSON
    assert resp2.status_code == 400
    assert not isinstance(resp2.json, dict)

    # Validate missing email
    assert resp3.status_code == 400
    assert not isinstance(resp3.json, dict)

    # Validate missing id
    assert resp4.status_code == 400
    assert not isinstance(resp4.json, dict)

    # Validate missing username
    assert resp5.status_code == 400
    assert not isinstance(resp5.json, dict)

    # Validate invalid id
    assert resp6.status_code == 400
    assert not isinstance(resp6.json, dict)

    # Validate duplicated id
    assert resp7.status_code == 409
    assert not isinstance(resp7.json, dict)

    # Validate duplicated username
    assert resp8.status_code == 409
    assert not isinstance(resp8.json, dict)

    # Validate duplicated email
    assert resp9.status_code == 409
    assert not isinstance(resp9.json, dict)

    ## Validate overcharacted username
    #assert resp10.status_code == 409
    #assert not isinstance(resp10.json, dict)
    #
    ## Validate overcharacted email
    #assert resp11.status_code == 409
    #assert not isinstance(resp11.json, dict)

def test_get_single_user(client):
    resp1 = client.get('/users/1')
    resp2 = client.get('/users/100')

    # Validate get_user
    assert resp1.status_code == 200
    assert isinstance(resp1.json, dict)

    # Validate user don't exist
    assert resp2.status_code == 404
    assert not isinstance(resp2.json, dict)

def test_update_user(client):
    client.post('/users', json={'id': '2', 'username': 'ladrao', 'email': 'ladrao@gmail.com'})
    resp1 = client.put('/users/1', json={'username': 'work', 'email': 'work@gmail.com'})
    resp2 = client.put('/users/1', data='asd')
    resp3 = client.put('/users/1', json={'username': 'timoteokang'})
    resp4 = client.put('/users', json={'username': 'erick', 'email': 'erick@gmail.com'})
    resp5 = client.put('/users/1', json={'email': 'morgana@gmail.com'})
    resp6 = client.put('/users/1', json={'username': 'roberval', 'email': 'ladrao@gmail.com'})
    resp7 = client.put('/users/1', json={'username': 'ladrao', 'email': 'roberval@gmail.com'})

    # Validate update user
    assert resp1.status_code == 200
    assert isinstance(resp1.json, dict)

    # Validate missing JSON
    assert resp2.status_code == 415
    assert not isinstance(resp2.json, dict)

    # Validate update username
    assert resp3.status_code == 200
    assert isinstance(resp3.json, dict)

    # Validate missing id
    assert resp4.status_code == 405
    assert not isinstance(resp4.json, dict)

    # Validate update email
    assert resp5.status_code == 200
    assert isinstance(resp5.json, dict)

    # Validate update with an already existing email
    assert resp6.status_code == 409
    assert not isinstance(resp6.json, dict)

    # Validate update with an already existing username
    assert resp7.status_code == 409
    assert not isinstance(resp7.json, dict)

def test_delete_user(client):
    resp1 = client.delete('/users/1')
    resp2 = client.delete('/users/1')

    # Validate success delete
    assert resp1.status_code == 204

    # Validate delete a non-exiting user
    assert resp2.status_code == 404
    assert not isinstance(resp2.json, dict)