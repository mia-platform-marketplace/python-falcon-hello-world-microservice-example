from falcon import testing
import pytest
import app


@pytest.fixture()
def client():
    return testing.TestClient(app.create())


def test_get_message(client):
    doc = {u'message': u'Hello World!'}

    result = client.simulate_get('/hello')
    assert result.json == doc
