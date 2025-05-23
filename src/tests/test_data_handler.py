import pytest

from src import data_handler
from src.config import VerityConfig


@pytest.fixture
def test_db_call():
    config = VerityConfig()
    config.DATABASE = "test_db.db"
    db_call = data_handler.database(config)
    db_call.build_database()
    yield db_call


def test_execute_sql_success(test_db_call):
    sql_statement = """INSERT INTO user(name)
    VALUES (?)
    """
    value = ("a_user_name",)
    result = test_db_call.execute_sql(sql_statement, value)
    assert result


def test_execute_sql_error(test_db_call):
    sql_statement = "SELECT * FROM non_existent_table"
    result = test_db_call.execute_sql(sql_statement)
    assert not result


def test_read_database(test_db_call):
    sql_statement = "SELECT name FROM user"
    results = test_db_call.read_database(sql_statement)
    assert isinstance(results, list)


def test_add_user_name(test_db_call):
    user_name = "Test user"
    user_id = test_db_call.add_user_name(user_name)
    assert user_id is not None


def test_get_users(test_db_call):
    users = test_db_call.get_users()
    assert isinstance(users, list)


def add_category(test_db_call):
    category_name = "Test Category"
    user_id = 1
    category_id = test_db_call.add_new_category(category_name, user_id)
    assert category_id is not None


def add_child_category(test_db_call):
    category_name = "Test Child Category"
    user_id = 1
    parent_category = 1
    category_id = test_db_call.add_new_category(category_name, user_id, parent_category)
    assert category_id is not None
