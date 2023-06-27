import os

import pytest
from starlette.testclient import TestClient

from app.config import get_settings, Settings
from app.main import create_application
from tests.utils.tortoise import register_tortoise


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="session")
def test_app():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client

    # tear down


@pytest.fixture(scope="function")
@pytest.mark.asyncio
def test_app_with_db():
    # set up
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_TEST_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )
    with TestClient(app) as test_client:
        yield test_client
