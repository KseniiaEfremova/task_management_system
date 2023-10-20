from db_utils import get_all_projects, DB_NAME


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
        # function is called to view all existing projects
        if selection == 1:
            pass

        # ====If User Selects 2 ====
        # function is called to view all tasks in a project
        elif selection == 2:
            pass


        # ====If User Selects 3====
        # function is called to add a new project
        elif selection == 3:
            pass

        # ====If User Selects 4====
        # function is called to add a task to a project
        elif selection == 4:
            pass

        # ====If User Selects 5====
        # function is called to update a task
        elif selection == 5:
            pass

        # ====If User Selects 6====
        # function is called to delete a project
        elif selection == 6:
            pass

        # ====If User Selects 7====
        # function is called to delete a task
        elif selection == 7:
            pass

        # ====If User Selects 0 ====
        # Task Management System is exited
        elif selection == 0:
            print('\Goodbye, you are exiting the Task Management System\n')
   
        # Else, the user is informed that they made the wrong choice
        else:
            print("\nIncorrect choice of number, options are between 0-7 only\n")

    except ValueError:
        print("\nInvalid input, enter a numerical digit between 0-7\n")

if __name__ == '__main__':
    run()