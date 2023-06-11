import os
import psycopg2
import psycopg2.extras


def establish_connection(connection_data=None):
    """
    Create a database connection based on the :connection_data: parameter
    :connection_data: Connection string attributes
    :returns: psycopg2.connection
    """
    if connection_data is None:
        connection_data = get_connection_data()
    try:
        connect_str = "dbname={} user={} host={} password={}".format(connection_data['dbname'],
                                                                     connection_data['user'],
                                                                     connection_data['host'],
                                                                     connection_data['password'])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
    except psycopg2.DatabaseError as e:
        print("Cannot connect to database.")
        print(e)
    else:
        return conn


def get_connection_data(db_name=None):
    """
    Give back a properly formatted dictionary based on the environment variables values which are started
    with :MY__PSQL_: prefix
    :db_name: optional parameter. By default it uses the environment variable value.
    """
    if db_name is None:
        db_name = os.environ.get('PSQL_DB_NAME')

    return {
        'dbname': db_name,
        'user': os.environ.get('PSQL_USER_NAME'),
        'host': os.environ.get('PSQL_HOST'),
        'password': os.environ.get('PSQL_PASSWORD')
    }

def execute_update(statement, variables=None):
    """
    Execute an UPDATE statement optionally parameterized and return the updated row.

    Example:
    > execute_update('UPDATE shows SET title = %(new_title)s WHERE id = %(show_id)s', 
                    variables={'new_title': 'New Title', 'show_id': 1})
    statement: UPDATE statement
    variables: optional parameter dict
    """
    updated_row = None
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement + ' RETURNING *', variables)
            if cursor.rowcount > 0:
                updated_row = cursor.fetchone()
    return updated_row

def execute_insert(statement, variables=None):
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement + ' RETURNING *', variables)
            inserted_row = cursor.fetchone()  # Retrieve the newly inserted row
            return inserted_row
            

def execute_select(statement, variables=None, fetchall=True):
    """
    Execute SELECT statement optionally parameterized.
    Use fetchall=False to get back one value (fetchone)

    Example:
    > execute_select('SELECT %(title)s; FROM shows', variables={'title': 'Codecool'})
    statement: SELECT statement
    variables:  optional parameter dict, optional parameter fetchall"""
    result_set = []
    with establish_connection() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(statement, variables)
            result_set = cursor.fetchall() if fetchall else cursor.fetchone()
    return result_set

