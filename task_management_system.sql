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
