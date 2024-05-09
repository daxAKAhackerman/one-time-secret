from typing import Iterator, Optional
from unittest import mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def ots_database(request: pytest.FixtureRequest) -> Iterator[Optional[mock.MagicMock]]:
    if "no_ots_database_mocker" in request.keywords:
        yield
    else:
        with mock.patch("db.get_ots_database") as mocker:
            yield mocker


@pytest.fixture
def fastapi_app(ots_database: Optional[mock.MagicMock]):
    from main import app

    yield app


@pytest.fixture
def test_client(fastapi_app: FastAPI) -> Iterator[TestClient]:
    yield TestClient(fastapi_app)
