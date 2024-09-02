#DB CREATION IN MYSQL

CREATE DATABASE IF NOT EXISTS sample_db;

## DB USAGE
USE sample_db;

## EMPLOYEES TABLE CREATION
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE
);

## EMPLOYEES TABLE INSERTION
INSERT INTO employees (first_name, last_name, hire_date)
VALUES ('John', 'Doe', '2022-01-15'),
       ('Jane', 'Smith', '2021-12-01'),
       ('Mike', 'Johnson', '2023-03-22');

## EMPLOYEES TABLE SELECTION

SELECT * FROM employees;


