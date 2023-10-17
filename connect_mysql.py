import mysql.connector
from utils import get_user_and_passwd_from_file


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
        # Establish a connection to the MySQL database
        db_connection = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=password
        )
        return db_connection
    except mysql.connector.Error as err:
        # Handle MySQL database connection errors
        raise err

