import requests
from tabulate import tabulate
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


def get_tasks_in_project():
    project_id = input("Which project do you want to see? (pass it's number) ").strip().lower()
    tasks = requests.get(f"http://localhost:5001/projects/{project_id}/todo", headers= {"content-type":"application/json"})
    print(list(tasks.json()))
 


def run():
    display_projects('projects')
    get_tasks_in_project()




if __name__ == '__main__':
    run()