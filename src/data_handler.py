import sqlite3
import logging
from config import VerityConfig

logger = logging.getLogger(__name__)

class database():
    'basic Database class to start some development'
    def __init__(self, config: VerityConfig ) -> None:
        self.database = config.DATABASE
        self.schema = config.DATABASE_SCHEMA

    @staticmethod
    def _build_column(column:dict) -> str:
        name = column['column_name']
        is_pk = column['is_pk']
        datatype = column['datatype']
        nullable = column['nullable']
        column_string = f'{name} {datatype}'
        if is_pk:
            column_string += ' PRIMARY KEY AUTOINCREMENT'
        if not nullable:
            column_string += ' NOT NULL'
        return column_string

    @staticmethod
    def _build_foreign_key(key:dict) -> str:
        column = key['column']
        reference_table = key['references']
        reference_column = key['reference_column']
        return f'FOREIGN KEY ({column}) REFERENCES {reference_table} ({reference_column})'

    def _add_table_to_db(self, table:dict) -> bool:
        'Creates the table in the verity database, based on the schema yaml'
        sql = f'''CREATE TABLE IF NOT EXISTS {table['table_name']} (
        '''
        columns = []
        for column in table['table_columns']:
            columns.append(self._build_column(column))
        sql += ',\n'.join(columns)
        if table.get('table_foreign_keys', None):
            sql += ',\n'
            for key in table['table_foreign_keys']:
                sql += f'{self._build_foreign_key(key)}'
        sql += '\n);'
        success_status = False
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            success_status = True
        except sqlite3.ProgrammingError as pe:
            logger.error(pe)
        except sqlite3.OperationalError as oe:
            logger.error(oe)
        except sqlite3.InterfaceError as ie:
            logger.error(ie)
        finally:
            try:
                connection.close()
            except Exception as e:
                logger.error(e)
            return success_status

    def build_database(self):
        for table in self.schema['tables']:
            logger.info(f"Checking {table['table_name']}")
            # Add true/false handling here to gracefully handle errors
            self._add_table_to_db(table)

    def print_table_schema(self, table_name):
        """
        Connects to the sqlite3 database, retrieves the schema of a specified table,
        and prints it to the console.

        Args:
            table_name (str): The name of the table to inspect.
        """
        try:
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()

            # Use PRAGMA table_info to get table schema
            cursor.execute(f"PRAGMA table_info({table_name})")

            # Print the schema
            logger.debug(f"Schema for table: {table_name}")
            for row in cursor.fetchall():
                logger.debug(f"  Column Name: {row[1]}, Data Type: {row[2]}, Not Null: {row[3]}")

        except Exception as e:
            logger.error(f"An error occurred: {e}")

        finally:
            try:
                connection.close()
            except Exception as e:
                logger.error(e)