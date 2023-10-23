import requests
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'paskudzio'

@app.route('/')
def home():
    return render_template('index.html')

def delete_project(project_name):
    response = requests.delete(f"http://127.0.0.1:5001/delete_project/<int:project_name>")
    if response.status_code == 200:
        print(f"Project: {project_name} has successfully been deleted")
    else:
        print(f"Failed to delete project.")

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
                        deadline_date_input = input(
                            "Please enter the date deadline of your task in DD/MM/YYYY format: ")
                        deadline_date = datetime.strptime(deadline_date_input, "%d/%m/%Y")
                        formatted_deadline_date = deadline_date.strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date format. Please use DD/MM/YYYY.")
                input_status = input(
                    "Please select the status of your task - 'todo', 'in progress', 'in review', 'done': ")
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
                try:
                    project_id = int(input("Please enter the ID of the project you want to delete: "))
                    delete_project(project_id)  # Call your delete project function

                    # Provide feedback based on the result of the delete operation
                    print(f"Project with ID {project_id} has been deleted successfully.")
                except ValueError:
                    print("Invalid project ID. Please enter a valid numerical ID.")
                except Exception as exc:
                    print(f"An error occurred while deleting the project: {exc}")

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

