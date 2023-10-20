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

