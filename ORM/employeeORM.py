from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Step 1: Create database engine
engine = create_engine("sqlite:///Emoloyee.db")

# Step 2: Create base class
Base = declarative_base()

# Step 3: Define Employee table
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    department = Column(String)

# Step 4: Create table
Base.metadata.create_all(engine)

# Step 5: Create session
Session = sessionmaker(bind=engine)
session = Session()

# Step 6: Insert records
e1 = Employee(name="Chenna", age=21, department="HR")
e2 = Employee(name="Gabbi", age=22, department="IT")
e3 = Employee(name="Rohit", age=23, department="Finance")

session.add_all([e1, e2, e3])
session.commit()

# Display records
print("\nBefore Update:")
employees = session.query(Employee).all()
for emp in employees:
    print(emp.id, emp.name, emp.age, emp.department)

# Step 7: Update record
emp = session.query(Employee).filter_by(id=1).first()
if emp:
    emp.name = "Chennai"
    session.commit()
    print("\nRecord updated successfully!")

# Display after update
print("\nAfter Update:")
employees = session.query(Employee).all()
for emp in employees:
    print(emp.id, emp.name, emp.age, emp.department)

# Step 8: DELETE record (FIXED CODE TO DELETE EMPLOYEE WITH id=1)
emp = session.query(Employee).filter_by(id=1).first()

if emp:
    session.delete(emp)   # mark for deletion
    session.commit()      # save deletion
    print("\nRecord deleted successfully!")
else:
    print("\nEmployee with id=1 not found!")

# Display after delete
print("\nAfter Delete:")
employees = session.query(Employee).all()
for emp in employees:
    print(emp.id, emp.name, emp.age, emp.department)

emp = session.query(Employee).filter(Employee.age > 22).all()
print("\nEmployees with age greater than 22:")
if emp:
    for e in emp:
        session.delete(e)   # mark for deletion
    session.commit()      # save deletion
    print("\nRecord deleted successfully!")
else:
    print("\nNo employees found with age greater than 22!")
# Display after delete
print("\nAfter Delete:")
employees = session.query(Employee).all()
for emp in employees:
    print(emp.id, emp.name, emp.age, emp.department)

#AND operation
emp = session.query(Employee).filter(Employee.age > 21, Employee.name == "Gabbi").first()
print("\nEmployees with age greater than 21 and name 'Gabbi':")
if emp:
    print(emp.id, emp.name, emp.age, emp.department)
else:
    print("\nNo employees found with age greater than 21 and name 'Gabbi'!")

#OR operation
"""emp = session.query(Employee).filter((Employee.age > 21) | (Employee.name == "Chennai")).all()
print("\nEmployees with age greater than 21 or name 'Chennai':")
if emp:
    for e in emp:
        print(e.id, e.name, e.age, e.department)
else:  
    print("\nNo employees found with age greater than 21 or name 'Chennai'!")"""

#orderby age in ascending order
emp = session.query(Employee).order_by(Employee.age).all()
print("\nEmployees ordered by age in ascending order:")
if emp:
    for e in emp:
        print(e.id, e.name, e.age, e.department)
else:
    print("\nNo employees found!")
#orderby age in descending order
emp = session.query(Employee).order_by(Employee.age.desc()).all()
print("\nEmployees ordered by age in descending order:")
if emp:
    for e in emp:
        print(e.id, e.name, e.age, e.department)
else:
    print("\nNo employees found!")

#limit number of records
emp = session.query(Employee).limit(2).all()
print("\nFirst 2 employees:")
if emp:
    for e in emp:
        print(e.id, e.name, e.age, e.department)
else:
    print("\nNo employees found!")
    
