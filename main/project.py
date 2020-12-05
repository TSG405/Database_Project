#CODED BY @TSG,2020 ---------------------------------------------------------------------------------------//

import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, tenth_marks INTEGER, twelveth_marks INTEGER, graduate_CGPA DECIMAL(10,5), interest TEXT);"
INSERT_STUDENT = "INSERT INTO students (name,tenth_marks,twelveth_marks,graduate_CGPA,interest)VALUES(?,?,?,?,?);"

GET_ALL_STUDENT = " SELECT * FROM students; "

GET_STUDENT_BY_NAME = " SELECT * FROM students WHERE name = ?;"

GET_TOPPER = """
SELECT name FROM Students
ORDER BY graduate_CGPA DESC
LIMIT 1;
"""

OPPORTUNITY = " SELECT interest FROM students WHERE name = ?;"

def connect():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)

def add_student(connection, name , tenth_marks , twelveth_marks , graduate_CGPA , interest):
    with connection:
        connection.execute(INSERT_STUDENT, (name,tenth_marks,twelveth_marks,graduate_CGPA,interest))

def get_all_students(connection):
    with connection:
        return connection.execute(GET_ALL_STUDENT).fetchall()

def get_student_by_name(connection,name):
    with connection:
        return connection.execute(GET_STUDENT_BY_NAME,(name,)).fetchall()

def get_topper(connection):
    with connection:
        return connection.execute(GET_TOPPER).fetchone()

def opportunity(connection,name):
    with connection:
        return connection.execute(OPPORTUNITY,(name,)).fetchone()
