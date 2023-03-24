from typing import Generator
import pytest
from flask.testing import FlaskClient

from ac_performance.app import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_route(client: FlaskClient):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
