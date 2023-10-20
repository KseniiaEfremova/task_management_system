import mysql.connector
import json
import logging
from mysql.connector import errorcode

DB_NAME = 'task_management_system'


def get_host_user_and_passwd_from_file(file_name: str) -> tuple:
    """
    Retrieves user and password information from a JSON configuration file.
    Args:
        file_name (str): The name of the JSON configuration file.
    Returns:
        tuple: A tuple containing host (str), user (str) and password (str) extracted from the file.
    Raises:
        ValueError: If the retrieved credentials (user or password) are empty or None.
        FileNotFoundError: If the specified file does not exist.
        KeyError: If the "user" or "passwd" keys are missing in the JSON data.
        json.JSONDecodeError: If the file content is not a valid JSON.
    """
    try:
        with open(file_name, 'r') as config_file:
            data = json.load(config_file)
            host = data["host"]
            user = data["user"]
            passwd = data["passwd"]
        if not host or not user or not passwd:
            # Print an error message and raise a ValueError if user or password or host is empty or None
            print("Invalid user or password or host in JSON configuration.")
            raise ValueError("Invalid user or password or host in JSON configuration.")
        return host, user, passwd
    except FileNotFoundError as e:
        print(f"The file '{file_name}' does not exist.")
        raise e
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error reading JSON data from '{file_name}': {e}")
        raise e
    except Exception as e:
        # Catch unexpected exceptions, log them, and raise to crash the program
        logging.exception(f"Unexpected error occurred: {e}")
        raise e


host, user, password = get_host_user_and_passwd_from_file("mysql.json")


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


connect_to_database_or_create_if_not_exists(DB_NAME)


class DbConnectionError(Exception):
    pass


def get_all_projects(db_name):
    projects = []
    try:
        cursor, db_connection = get_cursor_and_connection(db_name)
        print("Connected to DB: %s" % db_name)

        query = """SELECT project_id, project_name FROM projects"""

        cursor.execute(query)

        projects = cursor.fetchall()
        cursor.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return projects
