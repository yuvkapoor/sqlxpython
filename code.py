import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
}

try:
    # Establish a connection to MySQL server
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS sample_db")
    cursor.execute("USE sample_db")

    # Create a new table
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS employees ("
        "  employee_id INT AUTO_INCREMENT PRIMARY KEY,"
        "  first_name VARCHAR(50),"
        "  last_name VARCHAR(50),"
        "  hire_date DATE"
        ")"
    )
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_employee_query = (
        "INSERT INTO employees (first_name, last_name, hire_date) "
        "VALUES (%s, %s, %s)"
    )
    employees = [
        ('John', 'Doe', '2022-01-15'),
        ('Jane', 'Smith', '2021-12-01'),
        ('Mike', 'Johnson', '2023-03-22'),
    ]
    cursor.executemany(insert_employee_query, employees)
    cnx.commit()  # Commit the transaction

    # Retrieve data from the table
    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)
    results = cursor.fetchall()

    # Print the results
    for (employee_id, first_name, last_name, hire_date) in results:
        print(f"ID: {employee_id}, Name: {first_name} {last_name}, Hire Date: {hire_date}")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()
