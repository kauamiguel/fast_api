from fastapi.testclient import (
    TestClient,
)
from fast_zero.app import (
    app,
)


def test_html():
    client = TestClient(
        app
    )
    response = client.get(
        "/html"
    )
    assert (
        response.status_code
        == 200
    )
    assert (
        "<h1>Hello World</h1>"
        in response.text
    )
