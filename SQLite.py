#Commands/keywords for sqlite:
"""1)connect()->open database
2)cusror()->run sql
3)excute()->excute the sql
4)commit->close connections"""
import sqlite3
"""connection1=sqlite3.connect('school.db')
print("Database opened successfully")
connection1.close()"""
"""connection1=sqlite3.connect('school.db')
cursor1=connection1.cursor()
print("Successfully connected to database")
connection1.close()"""
connection1=sqlite3.connect('school.db')
cursor1=connection1.cursor()
cursor1.execute('''CREATE TABLE STUDENTS
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
MARKS INT NOT NULL);''')
print("Table created successfully")
connection1.commit()
connection1.close()
                