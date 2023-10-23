import mysql.connector
import logging
from mysql.connector import errorcode
from config import data

host, user, password = data["host"], data["user"], data["passwd"]
DB_NAME = 'task_management_system'


def connect_to_mysql_database(db_name):
    """
    Connects to a MySQL database using credentials from a JSON file.
    Returns:
        mysql.connector.MySQLConnection: A MySQL database connection object.
    Raises:
        mysql.connector.Error: If there is an error during the database connection process.
    """
    try:
        db_connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return db_connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")
        raise e
    except ValueError as e:
        print(f"ValueError: {e}")
        raise e
    except Exception as e:
        # Catch unexpected exceptions, log them, and raise to crash the program
        logging.exception(f"Unexpected error occurred: {e}")
        raise e


def get_cursor_and_connection(db_name):
    db_connection = connect_to_mysql_database(db_name)
    cursor = db_connection.cursor()
    return cursor, db_connection


def create_database(db_name):
    try:
        cursor, _ = get_cursor_and_connection(db_name)
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def connect_to_database_or_create_if_not_exists(db_name):
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(db_name)
            print("Database {} created successfully.".format(db_name))
            db_connection.database = db_name
        else:
            print(err)
            exit(1)
    print(f"You are using {db_name} database.")

def get_all_projects(db_name, table_name):
    projects = []
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print("Connected to DB: %s" % db_name)

        query = """SELECT project_id, project_name FROM {}""".format(table_name)

        cursor.execute(query)

        projects = cursor.fetchall()
        cursor.close()
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return projects


def add_new_task(db_name, project_id, description, deadline, status):
    """add_new_task() function takes in four params, which will be inserted into the DB
    establishes a connection to the DB
    executes SQL query to insert a new task into the DB using the params as values
    commits changes to the DB and closes DB connection
    if any exception occurs an error message will be  printed
    """
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print(f'Connected to database: {db_name}')

        query = """INSERT INTO tasks (project_id, description, deadline, status) 
        VALUES ('{}', '{}', '{}', '{}')""".format(project_id, description, deadline, status)

       
        cursor.execute(query)
        
        db_connection.commit()
        cursor.close()
        print("\nYour task has been successfully entered into the database!")

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()
            print("Connection closed")
