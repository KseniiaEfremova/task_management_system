CREATE DATABASE task_management_system;

USE task_management_system;


CREATE TABLE IF NOT EXISTS `projects` (
    `project_id` INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    `project_name` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`project_id`), UNIQUE KEY `project_name` (`project_name`)
    );


CREATE TABLE IF NOT EXISTS `tasks` (
    `task_id` INTEGER NOT NULL UNIQUE AUTO_INCREMENT,
    `project_id` INT NOT NULL,
    `description` VARCHAR(100) NOT NULL,
    `deadline` DATE NOT NULL,
    `status` ENUM('todo', 'in progress', 'in review', 'done'),
    PRIMARY KEY (`task_id`),
    FOREIGN KEY (`project_id`) REFERENCES `projects`(`project_id`)
    );


INSERT INTO projects (project_id, project_name) VALUES
(project_id,'task management system'),
(project_id,'learn Flask');


INSERT INTO tasks ( task_id, project_id, description, deadline, status) VALUES
(task_id, 1, 'create project repository', '2023-10-24', 'done'),
(task_id, 1, 'add requirements.txt, gitignore and README files', '2023-10-24', 'done'),
(task_id, 1, 'design database schema', '2023-10-24', 'done'),
(task_id, 1, 'create db_utils for queries', '2023-10-24', 'done'),
(task_id, 1, 'write query for getting projects', '2023-10-24', 'done'),
(task_id, 1, 'write query for getting tasks by status', '2023-10-24', 'in progress'),
(task_id, 1, 'write query for adding tasks', '2023-10-24', 'in review'),
(task_id, 1, 'write query for updating task', '2023-10-24', 'todo'),
(task_id, 1, 'write query for deleting task', '2023-10-24', 'in progress'),
(task_id, 1, 'create app.py for routes', '2023-10-24', 'done'),
(task_id, 1, 'create route for getting projects', '2023-10-24', 'done'),
(task_id, 1, 'create route for getting tasks by status per project', '2023-10-24', 'in progress'),
(task_id, 1, 'create route for adding tasks', '2023-10-24', 'in review'),
(task_id, 1, 'create route for updating task', '2023-10-24', 'todo'),
(task_id, 1, 'create route for deleting task', '2023-10-24', 'in progress'),
(task_id, 1, 'create main.py', '2023-10-24', 'done'),
(task_id, 1, 'write client side of your app', '2023-10-24', 'in progress'),
(task_id, 1, 'test your app', '2023-10-24', 'todo'),
(task_id, 1, 'add documentation to README', '2023-10-24', 'todo'),
(task_id, 1, 'create pull request for marker', '2023-10-24', 'todo'),
(task_id, 2, 'take part in sessions about Flask', '2023-10-20', 'done'),
(task_id, 2, 'add Flask as a dependency to your project', '2023-10-24', 'done'),
(task_id, 2, 'learn how to connect your db with Flask', '2023-10-24', 'done'),
(task_id, 2, 'learn how to query your db', '2023-10-24', 'done'),
(task_id, 2, 'learn how to add routes', '2023-10-24', 'done'),
(task_id, 2, 'write some queries and routes', '2023-10-24', 'in progress'),
(task_id, 2, 'learn how to connect your Flask API with front-end', '2023-10-24', 'in review'),
(task_id, 2, 'write some front-end for your app as reward', '2023-10-24', 'in review'),
(task_id, 2, 'connect front-end and back-end', '2023-10-24', 'in progress'),
(task_id, 2, 'learn about templates', '2023-10-24', 'in progress'),
(task_id, 2, 'write another Flask API and use templates as client-side', '2023-10-24', 'todo'),
(task_id, 2, 'write another Flask API as a console app', '2023-10-24', 'in progress'),
(task_id, 2, 'learn that Flask is pointless because everyone uses DjangoXD', '2023-10-24', 'todo');
