from sqlalchemy import create_engine

engine = create_engine("sqlite:///School.db")
print("SQLite database connected successfully!")
