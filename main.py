import requests
import json
from datetime import datetime
from db_utils import DB_NAME, get_all_projects, connect_to_database_or_create_if_not_exists


def display_projects(table_name):
    projects = get_all_projects(DB_NAME, table_name)
    print("################################\n")
    print("All projects:")
    number_of_project = 1
    if projects:
        for project in projects:
            print(f"{number_of_project}. {project[1].capitalize()}")
            number_of_project += 1
    else:
        print("You don't have any projects")


def add_task(table_name, input_project_id, input_description, formatted_deadline_date, input_status):
    """ add_task() function akes five parameters 
    creates a dictionary called new_task with five key-value pairs using the params
    sends a POST request to URL - new_task dict as the request body in JSON format
    checks the response from the server - if status code is 201, it prints success
    """
    new_task = {
        "table_name": table_name,
        "project_id": input_project_id,
        "description": input_description,
        "deadline": formatted_deadline_date,
        "status": input_status
    }

    response = requests.post(
        'http://127.0.0.1:5000/newtask',
        json=new_task
    )

    if response.status_code == 201:
        print("Task added successfully!")
        return response.json()  
    else:
        print("Failed to add task!")
        return None  


def run():
    try:
        selection = int(input('''\nWelcome to the Task Management System

    Please choose one of the following options below:
    1   -   View all existing projects
    2   -   View all tasks in an existing project
    3   -   Add a new project
    4   -   Add a new task to a project
    5   -   Update a task
    6   -   Delete a project
    7   -   Delete a task
    0   -   Exit
    Type your option here: '''))

        # ====If User Selects 1 ====
        # Please call your view all projects function here :)
        # function is called to view all existing projects
        if selection == 1:
            pass

        # ====If User Selects 2 ====
        # Please call your view all tasks function here :)
        # function is called to view all tasks in a project
        elif selection == 2:
            pass
            

        # ====If User Selects 3====
        # Please call your view add new project function here :)
        # function is called to add a new project
        elif selection == 3:
            pass

        # ====If User Selects 4====
        # function is called to add a task to a project
        elif selection == 4:
            # table_name variable = tasks as we are adding tasks
            # Get user input
            table_name = "tasks"
            input_project_id = int(input("Please enter the Project ID number you would like to add a task to: "))
            input_description = input("Please enter a description of your new task: ")
            # while True loop will break if a valid date is entered
            # or loop if a Value error and ask the user to reenter a valid date
            # useful as this is a common input error and means the user won't have
            # to restart the whole program
            while True:
                try:
                    deadline_date_input = input("Please enter the date deadline of your task in DD/MM/YYYY format: ")
                    deadline_date = datetime.strptime(deadline_date_input, "%d/%m/%Y")
                    formatted_deadline_date = deadline_date.strftime("%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use DD/MM/YYYY.")
            input_status = input("Please select the status of your task - 'todo', 'in progress', 'in review', 'done': ")
            # add_task() function called
            add_task(table_name, input_project_id, input_description, formatted_deadline_date, input_status)

        # ====If User Selects 5====
        # Please call your update task function here :)
        # function is called to update a task
        elif selection == 5:
            pass

        # ====If User Selects 6====
        # Please call your delete a project function here :)
        # function is called to delete a project
        elif selection == 6:
            pass

        # ====If User Selects 7====
        # Please call your delete a task function here :)
        # function is called to delete a task
        elif selection == 7:
            pass

        # ====If User Selects 0 ====
        # Task Management System is exited
        elif selection == 0:
            print('\Goodbye, you are exiting the Task Management System\n')
   
        # Else, the user is informed that they made the wrong choice of number
        else:
            print("\nIncorrect choice of number, options are between 0-7 only\n")
    # Except value error - if user enters something other than a number
    except ValueError:
        print("\nInvalid input, enter a numerical digit between 0-7\n")

if __name__ == '__main__':
    run()
