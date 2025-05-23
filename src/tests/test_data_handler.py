import os
import sqlite3
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
    sql_statement = """INSERT INTO budget (
    name,
    created_date
    )
    VALUES ('a_budget_name','2025-05-23 09:04:00')
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
    sql_statement = "SELECT name FROM budget"
    results = test_db_call.read_database(sql_statement)
    assert isinstance(results, list)
    # Check the contents of the list
    # self.assertIsNotNone(results)
    # self.assertIsInstance(results[0], str)


def test_add_budget_name(test_db_call):
    # Test adding a new budget name
    budget_name = "Test Budget"
    budget_id = test_db_call.add_budget_name(budget_name)
    assert budget_id is not None
    # Check if the budget name was actually added
    # You might need to query the database to verify
    # self.assertEqual(budget_id, 1)


def test_get_budgets(test_db_call):
    # Test getting budgets
    budgets = test_db_call.get_budgets()
    assert isinstance(budgets, list)
    # Check the contents of the list
    # self.assertIsNotNone(budgets)
    # self.assertIsInstance(budgets[0], str)
