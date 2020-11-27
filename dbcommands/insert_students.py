import sqlite3

# Connect
connection = sqlite3.connect("./db/college_database.db")

# Can't issue commands without creating a cursor
cursor = connection.cursor()

# SQL query
sql_command = """
INSERT INTO students (student_number,student_name)
VALUES (33289,"Susan Smith"),
(67830,"Bob Martin");"""

# Execute
cursor.execute(sql_command)

# Commit
connection.commit()