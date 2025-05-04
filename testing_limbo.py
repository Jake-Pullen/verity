import limbo
import yaml

con = limbo.connect('verity.db')
cur = con.cursor()


def build_column(column:dict) -> str:
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

def add_table_to_db(table:dict) -> bool:
    'Creates the table in the verity database, based on the schema yaml'
    sql = f'''CREATE TABLE {table['table_name']} (
    '''
    columns = []
    for column in table['table_columns']:
        columns.append(build_column(column))
    sql += ',\n'.join(columns)
    sql += '\n)'
    try:
        cur.execute(sql)
        cur.close()
        return True
    except limbo.ProgrammingError as pe:
        print(pe)
        return False
    except limbo.OperationalError as oe:
        print(oe)
        return False

def build_database():
    with open('verity_schema.yaml') as f:
        schema = yaml.safe_load(f)
    for table in schema['tables']:
        print(table['table_name'])
        add_table_to_db(table)


try:
    cur.execute('select * from budget')
except limbo.ProgrammingError:
    # table doesnt exist, so we need to build the database.
    build_database()
