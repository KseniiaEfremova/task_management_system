import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from connect_mysql import connect_to_mysql_database
from create_db import get_cursor_and_connection

db_name = 'task_management_system'

def insert_new_task():
    try:
        # connecting to database
        cursor, _ = get_cursor_and_connection(db_name)
        print(f'Connected to database: {db_name}')

        # Get user input
        project_id = int(input("Please enter the Project ID number you would like to add a task to: "))
        description = input("Please enter a description of your task: ")
        # while True loop will break if a valid date is entered
        # or loop if a Value error and ask the user to reenter a valid date
        while True:
            try:
                deadline_date_input = input("Please enter the date deadline of your task in DD/MM/YYYY format: ")
                deadline_date = datetime.strptime(deadline_date_input, "%d/%m/%Y")
                formatted_deadline_date = deadline_date.strftime("%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")
        status = input("Please select the status of your task - 'todo', 'in progress', 'in review', 'done': ")
        
        # Query
        query = """INSERT INTO {db_name} ({}) VALUES ('{}', '{}', '{}', '{}')""", (project_id, description, formatted_deadline_date, status)
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

insert_new_task()
