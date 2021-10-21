import pytest
from dynaconf import settings

from app.crud.crud import create_user, get_users
from app.models import models
from app.db.database import SessionLocal, engine
from app.schemas.schemas import UserCreate


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="test")


@pytest.fixture(scope="session", autouse=True)
def set_up_db():
    models.Base.metadata.create_all(bind=engine)


def test_config_loaded():
    assert settings.IS_TEST == True


def test_create_user():
    user = create_user_helper("user_1")
    db = SessionLocal()
    res = create_user(db, user)
    assert res.email == "test_1"


def test_get_users():
    user_1 = create_user_helper("user_1")
    user_2 = create_user_helper("user_2")
    db = SessionLocal()
    res_1 = create_user(db, user_1)
    res_2 = create_user(db, user_2)
    res_3 = get_users(db)
    assert len(res_3) == 2


def create_user_helper(email):
    return UserCreate(email=email, password="fake")
