SQL:



**create database classroom;                         #create a new database**

**use classroom;                                     #using created database to enter the values**

**CREATE TABLE Student (**

 **student\_id INT PRIMARY KEY,                       #adding first column name Student\_id as primary key**

    **name VARCHAR(50),                              #adding Column 2 name VARCHAR(50)means characters values**

    **class VARCHAR(10),**

    **age INT**

**);**

**INSERT INTO Student VALUES                         #inserting values into table based on columns created** 

**(1, 'Ravi', '10A', 15),**

**(2, 'Sita', '10A', 14),**

**(3, 'Arjun', '9B', 14);**

**SELECT \* FROM Student;                            #showing complete table** 

**SELECT \* FROM Student WHERE class = '10A';        #shows the table by where condition** 

**UPDATE Student SET age = 16 WHERE student\_id = 1; #setting the student age by where condition** 

**DELETE FROM Student WHERE student\_id = 3;         #Delete the row by where condition** 

**ALTER TABLE Student                               #adding new column to already existing table**

**ADD marks INT;                                    #adding column(INT)**

**UPDATE Student SET marks = 85 WHERE student\_id = 1;#updating student marks based on primary key in where condition**

**UPDATE Student SET marks = 90 WHERE student\_id = 2;**

**select \*from Student limit 2;                     # top rows in table will fetch** 

**select \*from Student order by marks desc limit 2; #selectiing top 2 students by marks** 





###### **AGGREGATION:**

->Order by ->Sorting after the table 

->Sum(marks)->Sum of marks before the table 

->AVG(marks)-> Avg the marks

->MAX(marks)->max marks

->MIN(marks)->Min marks

->COUNT(\*)->Count the number of values in table 



\#AND

select \*from Student where student\_id=2 and marks=90

\#OR

select \*from Student where student\_id=3 or marks=90



**DELETE KEYWORD:**

\*Removes selected rows

\*Uses WHERE condition

\*Can be rolled back (if transaction)

\*Table structure remains

EX:DELETE FROM Student WHERE student\_id = 3;





**TRUNCATE KEYWORD:**

\*Removes ALL rows and remains the table

\*Cannot use WHERE

\*Very fast

\*Cannot be rolled back

\*Table structure remains

EX:TRUNCATE TABLE Student;



**DROP KEYWORD:**

\*Deletes entire table

\*Data + structure both removed

\*Cannot be rolled back

ex: DROP TABLE Student;





##### **Group By:**

**GROUP BY in SQL is used to group rows that have the same values in one or more columns and then apply aggregate functions on each group.**

EX:select Course,Avg(marks) from Student group by Course

EX:Select Course,age,avg(marks),max(marks) from Student Group by Course,age;



### **SQL constraints:**

**1)primary Key**:

->Combination of NOT NULL + UNIQUE

->Uniquely identifies each row in a table

->Only one primary key per table

EX:CREATE TABLE Employee (

&nbsp;   emp\_id INT PRIMARY KEY,

&nbsp;   emp\_name VARCHAR(50)

);





**2)NOT NULL**:Ensures a column cannot have NULL values

EX:CREATE TABLE Student (

&nbsp;   id INT NOT NULL,

&nbsp;   name VARCHAR(50) NOT NULL

);



**3)CHECK**:

Ensures values satisfy a specific condition

EX:CREATE TABLE Student (

&nbsp;   age INT CHECK (age >= 18)

);





**4)Default**: Sets a default value if no value is provided

EX:CREATE TABLE Account (

&nbsp;   status VARCHAR(20) DEFAULT 'Active'

);



**5)FOREIGN KEY**:Links one table to another



Maintains referential integrity

EX:CREATE TABLE Orders (

&nbsp;   order\_id INT PRIMARY KEY,

&nbsp;   emp\_id INT,

&nbsp;   FOREIGN KEY (emp\_id) REFERENCES Employee(emp\_id)

);



**6)AUTO\_INCREMENT (MySQL)**:Automatically increases numeric values (mostly for primary keys)

EX:CREATE TABLE Product (

&nbsp;   product\_id INT AUTO\_INCREMENT PRIMARY KEY,

&nbsp;   product\_name VARCHAR(50)

);



**2️⃣ UNIQUE**:Ensures all values in a column are different

EX:CREATE TABLE User (

&nbsp;   email VARCHAR(100) UNIQUE

);





### **JOINS in SQL**

A JOIN is used to combine rows from two or more tables based on a related column (usually a Primary Key ↔ Foreign Key).



**1.inner join**:Returns only matching records from both tables.

EX:SELECT t1.student\_id, t1.name, t2.subject, t2.marks

FROM table1 t1

INNER JOIN table2 t2

ON t1.student\_id = t2.student\_id;



**2.Left Join**:👉 Returns ALL records from left table + matching from right table.(A+AnB)

SELECT t1.student\_id, t1.name, t2.subject, t2.marks

FROM table1 t1

LEFT JOIN table2 t2

ON t1.student\_id = t2.student\_id;



**3.Right Join**:👉 Returns ALL records from right table + matching from left table.(B+BnA)

SELECT t1.student\_id, t1.name, t2.subject, t2.marks

FROM table1 t1

RIGHT JOIN table2 t2

ON t1.student\_id = t2.student\_id;



**4.FULL JOIN**:👉 Returns ALL records from both tables.(A+B+(AnB))

SELECT t1.student\_id, t1.name, t2.subject, t2.marks

FROM table1 t1

FULL OUTER JOIN table2 t2

ON t1.student\_id = t2.student\_id;



**EXAMPLE**:

CREATE TABLE customers (

&nbsp;   customer\_id INT PRIMARY KEY,

&nbsp;   customer\_name VARCHAR(50),

&nbsp;   city VARCHAR(50)

);



CREATE TABLE orders (

&nbsp;   order\_id INT PRIMARY KEY,

&nbsp;   customer\_id INT,

&nbsp;   product VARCHAR(50),

&nbsp;   amount INT

);

INSERT INTO customers VALUES

(1, 'Aman', 'Delhi'),

(2, 'Riya', 'Mumbai'),

(3, 'Kabir', 'Delhi'),

(4, 'Neha', 'Pune'),

(5, 'Arjun', 'Bangalore'),

(6, 'Simran', 'Mumbai'),

(7, 'Rahul', 'Delhi'),

(8, 'Pooja', 'Chennai'),

(9, 'Vikas', 'Pune'),

(10, 'Anita', 'Bangalore');

INSERT INTO orders VALUES

(101, 1, 'Laptop', 60000),

(102, 1, 'Mouse', 1500),

(103, 2, 'Mobile', 30000),

(104, 3, 'Keyboard', 2500),

(105, 3, 'Monitor', 12000),

(106, 5, 'Tablet', 20000),

(107, 6, 'Laptop', 65000),

(108, 7, 'Mobile', 28000),

(109, 7, 'Earphones', 2000),

(110, 11, 'Camera', 40000);

select \*from customers;

select \*from orders ;

/\*show customers name ,product and amount :\*/

SELECT 

&nbsp;   c.customer\_name,

&nbsp;   o.product,

&nbsp;   o.amount

FROM customers c

INNER JOIN orders o

ON c.customer\_id = o.customer\_id;

/\*shows customer name and where city is delhi and product name using inner join\*/

select 

c.customer\_name,

c.city ,

o.product

from customers c

inner join orders o

on c.customer\_id=o.customer\_id

where city='Delhi';

ON c.customer\_id = o.customer\_id;

/\*show all customers even they have no orders\*/

select 

c.customer\_name,

o.product

from customers c

left join orders o

on c.customer\_id=o.customer\_id;

/\*show all orders even they have no customers\*/

select 

c.customer\_name,

o.product,

o.amount

from customers c

right join orders o

on c.customer\_id=o.customer\_id;

/\*find Orders  with no matching Customers\*/

SELECT 

&nbsp;   o.order\_id,

&nbsp;   o.customer\_id,

&nbsp;   o.product,

&nbsp;   o.amount

FROM orders o

right join customers c

ON o.customer\_id = c.customer\_id

WHERE c.customer\_id IS NULL;

/\*Show all Customers and orders\*/

select 

c.customer\_name,

c.customer\_id,

o.product,

o.amount

from customers c

&nbsp;join orders o

on c.customer\_id=o.customer\_id;

select \*from orders where amount between 25000 and 100000;



\***Difference Between Where and Having with Example:**

Difference Between WHERE and HAVING in SQL

Key Differences: WHERE vs HAVING

Criteria	            WHERE Clause	                                                   HAVING Clause

Filtering Level	          Filters individual rows	                                        Filters groups of rows

Aggregate Functions	Cannot use aggregate functions (COUNT, SUM, AVG, etc.)	           Can use aggregate functions

Execution                 Order	Applied before GROUP BY	                                               Applied after GROUP BY

SQL Statements	         Used with SELECT, UPDATE, DELETE	                                      Used only with SELECT

Performance	          Faster (filters data earlier)	                                  Slower (filters after aggregation)



1\. **WHERE Clause (Filtering Individual Rows)**

Example:



To find orders where the amount of an individual product is greater than 100:



SELECT CustomerID, ProductID, Amount

FROM Orders

WHERE Amount > 100;



Explanation:



The WHERE clause filters each row separately



Orders with Amount ≤ 100 are removed



Filtering happens before any grouping



**2. HAVING Clause (Filtering Grouped Data)**

Example:



To find customers whose total order amount is greater than 500:



SELECT CustomerID, SUM(Amount) AS TotalSpent

FROM Orders

GROUP BY CustomerID

HAVING SUM(Amount) > 500;



Explanation:



GROUP BY groups orders by CustomerID



HAVING filters groups, not individual rows



Aggregate function SUM() is allowed in HAVING





#### **SUB QUERY in SQL : Query Inside the Query**

\*One question depends on another question 

\*Subquery is a query where results are read by another query 

EX:select emp\_name,emp\_salary from employees where emp\_salary>(select avg(emp\_salary) from employees)

EX:select customer\_id,customer\_name from customers where customer\_id in (select customer\_id from orders)

EX:select customer\_id,customer\_name from customers where customer\_id not in (select customer\_id from orders)

EX:SELECT customer\_id, customer\_name

FROM customers

WHERE customer\_id IN (

&nbsp;   SELECT customer\_id

&nbsp;   FROM orders

&nbsp;   WHERE amount > (

&nbsp;       SELECT AVG(amount)

&nbsp;       FROM orders

&nbsp;   )

);



#### **Transaction in SQL (Simple Definition)**



A transaction in SQL is a group of one or more SQL statements that are executed as a single unit of work.

👉 (Either all statements succeed or none of them are applied.)

Real-Life Example (Bank Transfer 💰)



If money is transferred:



Amount is debited from one account



Amount is credited to another account



✔ Both must happen

❌ If one fails, everything should be undone

EX:start transaction;

update bank\_acc set balance=balance-500 where acc\_id=1;

commit ;

### 

### **INDEXING:**

Indexing in SQL is a technique used to speed up data retrieval from a table.

An index works like a book index — it helps the database find data faster without scanning the whole table.



🔹 Why Indexing is Needed?

Without index → Full table scan (slow ❌)

With index → Direct access to data (fast ✅)



Syntax:

CREATE INDEX index\_name

ON table\_name(column\_name);



EX:create index idx\_name on customers(customer\_name);

select customer\_name from customers where customer\_name='vikas';



Drawbacks:

don't use it for small data(tables)

it occupies the space in database

insert ,update delete become slow 

##### 

##### **DCL(data Control Language):**

**👉 It is used to control access and permissions on database objects like tables, views, databases, etc.**

**-GRANT → gives permissions to users**

**Syntax:GRANT SELECT ON students TO students\_user;**

**-REVOKE → removes permissions**

**Syntax:REVOKE SELECT ON students FROM students\_user;**





**📌 1. DDL – Data Definition Language**

**🔹 Full Form**



**Data Definition Language**



**🔹 Purpose**



**Used to define, create, modify, and delete database structures (tables, databases, schemas).**



**🔹 Commands**



**CREATE**



**ALTER**



**DROP**



**TRUNCATE**



**RENAME**



**🔹 Example**

**CREATE TABLE students (**

    **id INT,**

    **name VARCHAR(50)**

**);**



**📌 2. DML – Data Manipulation Language**

**🔹 Full Form**



**Data Manipulation Language**



**🔹 Purpose**



**Used to insert, update, and delete data inside tables.**



**🔹 Commands**



**INSERT**



**UPDATE**



**DELETE**



**🔹 Example**

**INSERT INTO students VALUES (1, 'Neha');**



**📌 3. DQL – Data Query Language**

**🔹 Full Form**



**Data Query Language**



**🔹 Purpose**



**Used to retrieve (fetch) data from database tables.**



**🔹 Commands**



**SELECT**



**🔹 Example**

**SELECT \* FROM students;**



**📌 4. DCL – Data Control Language**

**🔹 Full Form**



**Data Control Language**



**🔹 Purpose**



**Used to control access and permissions in the database.**



**🔹 Commands**



**GRANT**



**REVOKE**



**🔹 Example**

**GRANT SELECT ON students TO user1;**



**📌 5. TCL – Transaction Control Language**

**🔹 Full Form**



**Transaction Control Language**



**🔹 Purpose**



**Used to manage transactions and control changes made by DML commands.**



**🔹 Commands**



**COMMIT**



**ROLLBACK**



**SAVEPOINT**



**SET TRANSACTION**



**🔹 Example**

**COMMIT;**

### 

### **Normalization:**

**defination:Normalization is the process of organizing data in a database to reduce data redundancy and improve data integrity.**



**Why normalization:**

**1.data duplication**

**2.insert anomaly**

**3.update anomaly**

**4.delete anomaly**



**1NF=first normal form -> one cell = one value**

**2NF=**







**EXAMPLE for JOIN+GROUP BY** 

CREATE TABLE employees (

&nbsp;   emp\_id INT PRIMARY KEY,

&nbsp;   emp\_name VARCHAR(50),

&nbsp;   department VARCHAR(50)

);



INSERT INTO employees VALUES

(1,'Rahul','IT'),

(2,'Neha','HR'),

(3,'Amit','IT'),

(4,'Priya','Finance'),

(5,'Karan','HR');

CREATE TABLE projects (

&nbsp;   project\_id INT PRIMARY KEY,

&nbsp;   project\_name VARCHAR(50),

&nbsp;   budget INT

);



INSERT INTO projects VALUES

(101,'Website Revamp',100000),

(102,'Mobile App',150000),

(103,'Payroll System',80000);

CREATE TABLE employee\_projects (

&nbsp;   emp\_id INT,

&nbsp;   project\_id INT,

&nbsp;   hours\_worked INT,

&nbsp;   FOREIGN KEY (emp\_id) REFERENCES employees(emp\_id),

&nbsp;   FOREIGN KEY (project\_id) REFERENCES projects(project\_id)

);



INSERT INTO employee\_projects VALUES

(1,101,40),

(1,102,30),

(2,103,20),

(3,101,50),

(3,102,25),

(4,103,35),

(5,103,30);

select \*from employees

select \*from projects

select \*from employee\_projects

/\*Find total hours worked by each employee\*/

SELECT e.emp\_id, e.emp\_name, 

&nbsp;      SUM(ep.hours\_worked) AS total\_hours

FROM employees e

JOIN employee\_projects ep

ON e.emp\_id = ep.emp\_id

GROUP BY e.emp\_id, e.emp\_name;

/\*Find total hours spent on each project\*/

SELECT p.project\_id, p.project\_name,

&nbsp;      SUM(ep.hours\_worked) AS total\_hours

FROM projects p

JOIN employee\_projects ep

ON p.project\_id = ep.project\_id

GROUP BY p.project\_id, p.project\_name;

/\*Find department-wise total working hours\*/

SELECT e.department,

&nbsp;      SUM(ep.hours\_worked) AS total\_hours

FROM employees e

JOIN employee\_projects ep

ON e.emp\_id = ep.emp\_id

GROUP BY e.department;





