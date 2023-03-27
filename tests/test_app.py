from typing import Generator

import pytest
from flask.testing import FlaskClient

from ac_performance import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.mark.parametrize("route", ["index", "/"])
def test_home_route(route, client: FlaskClient):
    response = client.get(route)
    assert response.status_code == 200
    assert b"Hello" in response.data


def test_404(client: FlaskClient):
    response = client.get("indx")
    assert response.status_code == 404
    assert b"Not Found" in response.data
