import ssdwebsite


def test_import():
    assert ssdwebsite


def test_home(client):
    assert client.get('/').status_code == 200

    response = client.get('/')

    assert b"<h2>A philoslopy built on action and looking to" in response.data

    assert b"<h3>Multiple Choice Voting</h3>" in response.data

def test_vision(client):
    assert client.get('/ourVision').status_code == 200

    response = client.get('/ourVision')

    assert b"<p>This is our vision</p>" in response.data

def test_contact_info(client):
    assert client.get('/contact').status_code == 200

    response = client.get('/contact')

    assert b"<h2>We love your support!</h2>" in response.data
