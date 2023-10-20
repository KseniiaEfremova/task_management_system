import mysql.connector
from create_db import get_cursor_and_connection


def delete_task():
    try:
        db_name = 'task_management_system'
        cursor, db_connection = get_cursor_and_connection(db_name)
        print(f"Connected to database {db_name}")

        # Get user input
        task_id = input('Please enter the Task ID of the task you would like to delete: ')
        task_id = int(task_id)  # Convert the input from str to int

        # Query deleting the task with ID provided by the user from the db
        query = """DELETE FROM tasks WHERE TASK_id = '{x}'""".format(x=task_id)
        cursor.execute(query)
        db_connection.commit()

        cursor.close()
        print('Your task has been deleted')

    except Exception as exc:
        print(exc)

    finally:
        if db_connection:
            db_connection.close()


delete_task()
