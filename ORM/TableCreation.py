"""from unicodedata import name
from sqlalchemy import create_engine

engine = create_engine("sqlite:///School.db")
print("SQLite database connected successfully!")

#import declarative_base 
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker 
#create base class
base= declarative_base()
#base will be used to create tables in the database
#base is a class that will be used to create tables in the database
#creating a table called user
class Student(base):
    __tablename__= 'students'
    id= Column(Integer, primary_key=True)
    name= Column(String)
    age= Column(Integer)
    course= Column(String)
base.metadata.create_all(engine)
session= sessionmaker(bind=engine)
session=session()
S1= Student(id=1, name='John Doe', age=20, course='Computer Science')
s2= Student(id=2, name='Jane Smith', age=22, course='Mathematics')
session.add(S1)
session.add(s2)
session.commit()
students=session.query(Student).all()
for i in students:
    print(i.id, i.name, i.age, i.course)"""

#import declarative base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
#step 1
engine=create_engine("sqlite:///school.db")
#create base class
#step 2
Base=declarative_base()
#base will be parent of all models
#step 3
class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course=Column(String)
#create all tables defined using base
#step 4
Base.metadata.create_all(engine)

#step 5
Session=sessionmaker(bind=engine)
session=Session()
s1=Student(name="rahul",age=21,course="python")
s2=Student(name="karan",age=22,course="java")
session.add(s1)
session.add(s2)
session.commit()
students = session.query(Student).all()
for i in students:
    print(i.id,i.name,i.age,i.course)



