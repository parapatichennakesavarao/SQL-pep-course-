import psycopg2
conn=psycopg2.connect(
    host="localhost",
    database="testdata",
    user="postgres",
    password="Chenna@2004"
)
cur=conn.cursor()
cur.execute("""CREATE TABLE employee(
    id INT,name VARCHAR(50),age INT,department VARCHAR(50)
)""")
cur.execute("""INSERT INTO employee(id,name,age,department) VALUES
(1,'GABBI',30,'HR'),
(2,'SANDY',25,'IT'),
(3,'RAJ',28,'Finance'),
(4,'ANU',32,'HR'),
(5,'VIKRAM',27,'IT')""")
conn.commit()
cur.execute("SELECT * FROM employee")
rows=cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()

#commands 
#psql -U postgres
#\c testdata
#select * from employee;
