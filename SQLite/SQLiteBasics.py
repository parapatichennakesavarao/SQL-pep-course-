#SQL LITE:is a lightweight database that stores data in a file and is inbuilt into python.
#Commands/keywords for sqlite:
"""1)connect()->open database
2)cusror()->run sql
3)excute()->excute the sql(you can write sql command inside it)
4)commit->save changes
5)close()->close database"""
import sqlite3
"""connection1=sqlite3.connect('school.db')
print("Database opened successfully")
connection1.close()"""
"""connection1=sqlite3.connect('school.db')
cursor1=connection1.cursor()
print("Successfully connected to database")
connection1.close()"""
"""connection1=sqlite3.connect('school.db')
cursor1=connection1.cursor()
cursor1.execute('''CREATE TABLE STUDENTS
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
MARKS INT NOT NULL);''')
print("Table created successfully")
connection1.commit()
connection1.close()"""
"""connection1=sqlite3.connect('school.db')
cursor1=connection1.cursor()
cursor1.execute("INSERT INTO STUDENTS(ID,NAME,MARKS) VALUES(1,'John',85)")
cursor1.execute("INSERT INTO STUDENTS(ID,NAME,MARKS) VALUES(2,'Alice',90)")
cursor1.execute("INSERT INTO STUDENTS(ID,NAME,MARKS) VALUES(3,'Bob',78)")
print("Records inserted successfully")
connection1.commit()
connection1.close()"""
"""connection1=sqlite3.connect('school.db')
cursor1=connection1.cursor()
cursor1.execute("SELECT * FROM STUDENTS")
rows=cursor1.fetchall()
#print(rows)
for row in rows:
    print(row)
for row in rows:
    print("ID:",row[0])
    print("Name:",row[1])
    print("Marks:",row[2])
    print()
connection1.close()"""

"""connection2=sqlite3.connect('Employees.db')
cursor2=connection2.cursor()
cursor2.execute('''CREATE TABLE EMPLOYEES
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY INT NOT NULL);''')
print("Table created successfully")
connection2.execute("INSERT INTO EMPLOYEES(ID,NAME,AGE,SALARY) VALUES(1,'Gabbi',30,50000)")
connection2.execute("INSERT INTO EMPLOYEES(ID,NAME,AGE,SALARY) VALUES(2,'RAM',28,60000)")
connection2.execute("INSERT INTO EMPLOYEES(ID,NAME,AGE,SALARY) VALUES(3,'Salar',35,55000)")
print("Records inserted successfully")
connection2.commit()
cursor2.execute("SELECT * FROM EMPLOYEES")
rows=cursor2.fetchall()
for row in rows:
    print(row)
connection2.close()"""


"""connection3=sqlite3.connect('products.db')
cursor3=connection3.cursor()
cursor3.execute('''CREATE TABLE PRODUCTS
            (PRODUCT_ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
                PRICE REAL NOT NULL);''')
cursor3.execute("INSERT INTO PRODUCTS(PRODUCT_ID,NAME,PRICE) VALUES(1,'Laptop',999.99)")
cursor3.execute("INSERT INTO PRODUCTS(PRODUCT_ID,NAME,PRICE) VALUES(2,'Smartphone',499.99)")
cursor3.execute("INSERT INTO PRODUCTS(PRODUCT_ID,NAME,PRICE) VALUES(3,'Headphones',199.99)")
print("Records inserted successfully")
connection3.commit()
cursor3.execute("SELECT * FROM PRODUCTS")
rows=cursor3.fetchall()
for i in rows:    
    print(i)
connection3.close()"""

#DDL->Data Definition Language:used to define the structure of the database and its objects.
"""connection3=sqlite3.connect('products.db')
cursor3=connection3.cursor()
cursor3.execute('''CREATE TABLE PRODUCTS
            (PRODUCT_ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
                PRICE REAL NOT NULL);''')
cursor3.execute("INSERT INTO PRODUCTS(PRODUCT_ID,NAME,PRICE) VALUES(1,'Laptop',999.99)")
cursor3.execute("INSERT INTO PRODUCTS(PRODUCT_ID,NAME,PRICE) VALUES(2,'Smartphone',499.99)")
cursor3.execute("INSERT INTO PRODUCTS(PRODUCT_ID,NAME,PRICE) VALUES(3,'Headphones',199.99)")
cursor3.execute("Alter TABLE PRODUCTS ADD COLUMN STOCK INT DEFAULT 0")
cursor3.execute("UPDATE PRODUCTS SET STOCK = 10 WHERE PRODUCT_ID = 1")
cursor3.execute("DELETE FROM PRODUCTS WHERE PRODUCT_ID = 3")
print("Records inserted successfully")
connection3.commit()
cursor3.execute("SELECT * FROM PRODUCTS")
rows=cursor3.fetchall()
for i in rows:    
    print(i)
connection3.close()"""
#tcl->Transaction Control Language:used to manage transactions in the database.
connection4=sqlite3.connect('payments.db')
cursor4=connection4.cursor()
cursor4.execute('''CREATE TABLE PAYMENTS
            (PAYMENT_ID INT PRIMARY KEY NOT NULL,
            AMOUNT REAL NOT NULL,
                PAYMENT_DATE TEXT NOT NULL);''')
cursor4.execute("INSERT INTO PAYMENTS(PAYMENT_ID,AMOUNT,PAYMENT_DATE) VALUES(1,150.75,'2023-10-01')")
cursor4.execute("INSERT INTO PAYMENTS(PAYMENT_ID,AMOUNT,PAYMENT_DATE) VALUES(2,200.50,'2023-10-02')")
cursor4.execute('Commit;')  # Save the changes
connection4.commit()  # Save the changes
cursor4.execute("SELECT * FROM PAYMENTS")
rows=cursor4.fetchall()
for i in rows:
    print(i)
connection4.close()
