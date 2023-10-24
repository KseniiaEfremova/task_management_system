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