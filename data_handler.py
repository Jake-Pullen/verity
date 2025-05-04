import limbo
import yaml


class database():
    'basic Database class to start some development'
    def __init__(self) -> None:
        self.database = 'verity.db'


    @staticmethod
    def _build_column(column:dict) -> str:
        name = column['column_name']
        is_pk = column['is_pk']
        datatype = column['datatype']
        nullable = column['nullable']
        column_string = f'{name} {datatype}'
        if is_pk:
            column_string += ' IDENTITY(1,1) PRIMARY KEY'
        if not nullable:
            column_string += ' NOT NULL'
        return column_string

    @staticmethod
    def _build_foreign_key(key) -> str:
        column = key['column']
        reference_table = key['references']
        reference_column = key['reference_column']
        return f'FOREIGN KEY ({column}) REFERENCES {reference_table} ({reference_column})'

    def _add_table_to_db(self, table:dict) -> bool:
        'Creates the table in the verity database, based on the schema yaml'
        sql = f'''CREATE TABLE {table['table_name']} (
        '''
        columns = []
        for column in table['table_columns']:
            columns.append(self._build_column(column))
        sql += ',\n'.join(columns)
        # i dont think Limbo supports FK's right now, will keep an eye on it
        # if table.get('table_foreign_keys',None):
        #     sql += ','
        #     for key in table['table_foreign_keys']:
        #         sql += f'\n{build_foreign_key(key)},'
        sql += '\n);'
        # print(sql)
        success_status = False
        try:
            connection = limbo.connect(self.database)
            cursor = connection.cursor()
            response = cursor.execute(sql).fetchall()
            print(response) # TODO: Check this, hopefully we get a success response
            if response == 'Success':
                success_status = True
        except limbo.ProgrammingError as pe:
            print(pe)
        except limbo.OperationalError as oe:
            print(oe)
        except limbo.InterfaceError as ie:
            print(ie)
        finally:
            try:
                connection.close()
            except Exception as e:
                print(e)
            return success_status

    def build_database(self, schema):
        for table in schema['tables']:
            print(table['table_name'])
            self._add_table_to_db(table)


    def print_table_schema(self, table_name):
        """
        Connects to the limbo database, retrieves the schema of a specified table,
        and prints it to the console.

        Args:
            db_file (str): The path to the limbo database file.
            table_name (str): The name of the table to inspect.
        """
        try:
            connection = limbo.connect(self.database)
            cursor = connection.cursor()

            # Use PRAGMA table_info to get table schema
            cursor.execute(f"PRAGMA table_info({table_name})")

            # Print the schema
            print(f"Schema for table: {table_name}")
            for row in cursor.fetchall():
                print(f"  Column Name: {row[1]}, Data Type: {row[2]}, Not Null: {row[3]}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            try:
                connection.close()
            except Exception as e:
                print(e)

    def check_database_exists(self):
        with open('docs/verity_schema.yaml') as f:
            schema = yaml.safe_load(f)
        try:
            connection = limbo.connect(self.database)
            cursor = connection.cursor()
            # do we want to check all the tables?
            cursor.execute('select * from budget')
        except limbo.ProgrammingError:
            # table doesnt exist, so we need to build the database.
            self.build_database(schema = schema)

        for table in schema['tables']:
            self.print_table_schema(table['table_name'])
