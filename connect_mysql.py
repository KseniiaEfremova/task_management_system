import mysql.connector
from utils import get_user_and_passwd_from_file
import logging

# Retrieve user and password from a JSON configuration file
user, password = get_user_and_passwd_from_file("mysql.json")


def connect_to_mysql_database():
    """
    Connects to a MySQL database using credentials from a JSON file.
    Returns:
        mysql.connector.MySQLConnection: A MySQL database connection object.
    Raises:
        mysql.connector.Error: If there is an error during the database connection process.
    """
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=password
        )
        return db_connection
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL database: {err}")
        raise err
    except ValueError as err:
        print(f"ValueError: {err}")
        raise err
    except Exception as e:
        # Catch unexpected exceptions, log them, and raise to crash the program
        logging.exception(f"Unexpected error occurred: {e}")
        raise
