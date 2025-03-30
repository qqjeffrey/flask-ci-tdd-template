def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_hello(client):
    response = client.get('/hello/Jeff')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Jeff!"}