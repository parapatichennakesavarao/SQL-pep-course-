from sqlalchemy import create_engine

engine = create_engine("sqlite:///School.db")
print("SQLite database connected successfully!")

#Commit: save changes to the database(writing with pen on paper like permanent changes)
#rollback: undo changes to the database(example: if you made a mistake and want to undo it)
#flush: send changes to the database but do not commit(writing with pencil on paper like temporary changes)



#filter_by: used to filter records based on specific criteria(=)
#example: session.query(Student).filter_by(name="John").first() will return the first student with the name "John"
#filter: used to filter records based on specific criteria(>,<,=,!=)
#example: session.query(Student).filter(Student.age > 20).all() will return all students with age greater than 20

#.all(): used to return all records that match the query
#.first(): used to return the first record that matches the query
#.one(): used to return exactly one record that matches the query, raises an error if there are multiple or no records
#.one_or_more(): used to return zero or more records that match the query, raises an error if there are multiple records
#example: session.query(Student).filter_by(age>20).one_or_more() 
#.count(): used to return the number of records that match the query
#.one_or_none(): used to return one record that matches the query or None if no record matches, raises an error if there are multiple records
#example: session.query(Student).filter_by(name="John").one_or_none() will return

