CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
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
select *from customers;
select *from orders ;
/*show customers name ,pdoduct and amount :*/
SELECT 
    c.customer_name,
    o.product,
    o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
/*shows customer name and where city is delhi and product name using inner join*/
select 
c.customer_name,
c.city ,
o.product
from customers c
inner join orders o
on c.customer_id=o.customer_id
where c.city='Delhi';
/*show all customers even they have no orders*/
select 
c.customer_name,
o.product
from customers c
left join orders o
on c.customer_id=o.customer_id;