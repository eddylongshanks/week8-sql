import sqlite3

# Connect
connection = sqlite3.connect("db/college_database.db")

# Can't issue commands without creating a cursor
cursor = connection.cursor()

# SQL query
table_name = "Students"
cursor.execute(f"SELECT * FROM {table_name};")

# Fetch all rows
res = cursor.fetchall()

print("-"*50)
print(f"{table_name} table")
print("-"*50)

for row in res:
    # row[0] returns the first column in the query (student_number),
    # row[1] returns student_rep name
    print(f'{row[0]} : {row[1]}')

print("-"*50)

