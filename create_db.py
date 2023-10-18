import mysql.connector
from mysql.connector import errorcode
from connect_mysql import connect_to_mysql_database

cnx = connect_to_mysql_database()
cursor = cnx.cursor()


def create_database(db_name):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def connect_to_database_or_create_if_not_exists(db_name):
    try:
        cursor.execute("USE {}".format(db_name))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(db_name))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(db_name)
            print("Database {} created successfully.".format(db_name))
            cnx.database = db_name
        else:
            print(err)
            exit(1)
    print(f"You are using {db_name} database.")


connect_to_database_or_create_if_not_exists('task_management_system')
