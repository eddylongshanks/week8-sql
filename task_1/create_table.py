import sqlite3

# If db exists this wont overwrite
connection = sqlite3.connect("db/college_database.db")

# Can't issue commands without creating a cursor
cursor = connection.cursor()

# SQL query
sql_command = """
CREATE TABLE IF NOT EXISTS students ( 
student_number INTEGER PRIMARY KEY, 
student_name VARCHAR(150))
"""

# Execute the statement
cursor.execute(sql_command)

# Commit
connection.commit()

