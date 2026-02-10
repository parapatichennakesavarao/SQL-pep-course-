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
