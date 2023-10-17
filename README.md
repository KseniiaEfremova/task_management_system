Here are concise instructions for using the mysql.json file to store MySQL database credentials securely:
1. Create a file named mysql.json in your project directory with the following format:
```
{
  "user": "your_username",
  "passwd": "your_password"
}
```
Replace `"your_username"` with your MySQL username and `"your_password"` with your MySQL password.
2. Ensure that the mysql.json file has restricted permissions: use command line `chmod 600 mysql.json` 