import requests
import tabulate
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


def tabulate_data(tasks):
    dataset = list(tasks.json())
    header = dataset[0].keys()
    rows = [task.values() for task in dataset]
    print(tabulate.tabulate(rows, header))


def get_tasks_in_project():
    project_id = input("Which project do you want to see? (pass it's number) ").strip().lower()
    statuses = ['todo', 'in progress', 'in review', 'done']
    for status in statuses:
        try:
            tasks = requests.get(f"http://localhost:5001/projects/{project_id}/{status}", headers= {"content-type":"application/json"})
            print(status.upper())
            tabulate_data(tasks)
        except requests.exceptions.HTTPError as error_HTTP:
            print("Http Error:", error_HTTP)
        except requests.exceptions.ConnectionError as err_connect:
            print("Error Connecting:", err_connect)
        except requests.exceptions.Timeout as err_timeout:
            print("Timeout Error:", err_timeout)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)
 

def run():
    display_projects('projects')
    get_tasks_in_project()


if __name__ == '__main__':
    run()
