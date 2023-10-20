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
Replace `your_host`with your hostname, `"your_username"` with your MySQL username and `"your_password"` with your MySQL password.
2. Ensure that the mysql.json file has restricted permissions: use command line `chmod 600 mysql.json` 

---
Here are step-by-step instructions on how to use the task_management_system.sql file in MySQL Workbench:
1. Launch MySQL Workbench on your system.
2. Connect to your MySQL server using the appropriate connection settings (hostname, username, password, etc.).
3. In MySQL Workbench navigate to the location where task_management_system.sql is saved and open the file.
4. Execute the SQL Statements.
5. Now, your task_management_system database and tables are set up and ready to use. 