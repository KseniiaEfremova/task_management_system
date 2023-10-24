# Task Management System Documentation

This document provides instructions on how to set up and run the Task Management System.



## Installation Requirements

Before you can run the API, make sure you have the following requirements installed on your system:

- Python 3.x
- MySQL Workbench
- Git (for cloning the repository)


## Installation:

In order to install dependencies:

1. install the package pipreqs:
   `pip install pipreqs`

2. to install all the packages from requirements.txt use:
   `pip install -r requirements.txt`

---

Here are concise instructions for using the mysql.json file to store MySQL database credentials securely:
1. Create a file named config.py in your project directory with the following format:
```
data = {
  "host": "your_host",
  "user": "your_username",
  "passwd": "your_password"
}
```

Replace `your_host`with your hostname, `"your_username"` with your MySQL username and `"your_password"` with your MySQL password. 2. Ensure that the mysql.json file has restricted permissions: use command line `chmod 600 mysql.json`

---

Here are step-by-step instructions on how to use the task_management_system.sql file in MySQL Workbench:

1. Launch MySQL Workbench on your system.
2. Connect to your MySQL server using the appropriate connection settings (hostname, username, password, etc.).
3. In MySQL Workbench navigate to the location where task_management_system.sql is saved and open the file.
4. Execute the SQL Statements.
5. Now, your task_management_system database and tables are set up and ready to use.


## Running the Task Management System:

1. Clone the Task Management System repository from GitHub
`git clone git@github.com:KseniiaEfremova/task_management_system.git`

3. Run the Flask application
`flask run`


## API endpoints

### Get All Projects

- **Endpoint:** `/projects`
- **Method:** GET
- **Description:** Retrieves a list of all projects from the database.

### Get Tasks in a Project by Status

- **Endpoint:** `/projects/<project_id>/`
- **Method:** GET
- **Description:** Retrieves tasks of a specific status within a project.

### Get Task in a Project by ID

- **Endpoint:** `/projects/<project_id>/id/<task_id>`
- **Method:** GET
- **Description:** Retrieves a specific task within a project by its ID.

### Add a New Project

- **Endpoint:** `/newproject`
- **Method:** POST
- **Description:** Adds a new project to the database.

**Parameters:**

- `table_name` (string): Name of the table (e.g., "projects").
- `project_name` (string): Name of the new project.

### Add a New Task to a Project

- **Endpoint:** `/newtask`
- **Method:** POST
- **Description:** Adds a new task to a project in the database.

**Parameters:**

- `table_name` (string): Name of the table (e.g., "tasks").
- `project_id` (integer): ID of the project to add the task to.
- `description` (string): Description of the task.
- `deadline` (string): Deadline of the task (in YYYY-MM-DD format).
- `status` (string): Status of the task ("todo", "in progress", "in review," or "done").

### Delete a Project

- **Endpoint:** `/delete_project/int:project_id`
- **Method:** DELETE
- **Description:** Deletes a project from the database by its ID.

### Delete a Task

- **Endpoint:** `/delete_task/int:task_id`
- **Method:** DELETE
- **Description:** Deletes a task from the database by its ID.


The Task Management System allows to perform basic CRUD operations on tasks and projects.   
You can use the provided endpoints to create, read, update, and delete tasks and projects in the database.   
The API is designed to help manage tasks efficiently.

You can perform following actions using The Task Management System:

1. **View all existing projects**

2. **View all tasks in an existing project**

3. **Add a new project**

4. **Add a new task to a project**

5. **Update a task**

6. **Delete a project**

7. **Delete a task**

0. **Exit**


## Frontend Setup
To run the front-end part of The Task Management System you need the same preparation required to run the console app, which involves ensuring that the MySQL server running with a database, tables created and data populated.

1. Run app.py as a back-end server

2. Navigate to the client directory:  
`cd client`

3. Install the required Node.js packages using npm or yarn:
```
npm install

OR

yarn install
```



4. Start the development server for the front-end application:
```
npm start

OR

yarn start
```
The front-end will be accessible at http://localhost:1234/, which serves as the main page for the Task Management System.