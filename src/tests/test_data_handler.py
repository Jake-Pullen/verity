import pytest

from src import data_handler
from src.config import VerityConfig


@pytest.fixture
def test_db_call():
    config = VerityConfig()
    db_call = data_handler.database(config)
    db_call.build_database()
    yield db_call


def test_execute_sql_success(test_db_call):
    sql_statement = """INSERT INTO user (
    name
    )
    VALUES ('a_user_name')
    """
    result = test_db_call.execute_sql(sql_statement)
    assert result


def test_execute_sql_error(test_db_call):
    sql_statement = "SELECT * FROM non_existent_table"
    result = test_db_call.execute_sql(sql_statement)
    assert not result
    # Check if an error message is logged
    # You might need to add a logging assertion here


def test_read_database(test_db_call):
    # Test reading database data
    sql_statement = "SELECT name FROM user"
    results = test_db_call.read_database(sql_statement)
    assert isinstance(results, list)
    # Check the contents of the list
    # self.assertIsNotNone(results)
    # self.assertIsInstance(results[0], str)


def test_add_user_name(test_db_call):
    # Test adding a new user name
    user_name = "Test user"
    user_id = test_db_call.add_user_name(user_name)
    assert user_id is not None
    # Check if the user name was actually added
    # You might need to query the database to verify
    # self.assertEqual(user_id, 1)


def test_get_users(test_db_call):
    # Test getting users
    users = test_db_call.get_users()
    assert isinstance(users, list)
    # Check the contents of the list
    # self.assertIsNotNone(users)
    # self.assertIsInstance(users[0], str)
