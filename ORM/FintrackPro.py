#FINTRACK PRO Project
"""FinTrack Pro is a command line based personal finance management system developed using Python, SQLite and SQLAlchemy ORM. """
"""The project helps users to manage daily expenses, track subscriptions, search records, maintain monthly budgets and generate analytics using raw SQL queries."""
#4. System Features
#Add Expense  
#Update Expense  
# Delete Expense  
# Search by Date  
# Category Analytics  
# Monthly Budget Alert  
# Persistent Storage

# Database Design

"""Tables:
1. categories(id, name)  
2. expenses(id, title, amount, date, category_id)  
3. subscriptions(id, name, amount, next_date)  
4. budgets(id, month, limit)

Relationships:
Category 1 ---- N Expenses"""

"""6. Modules Description

a) Expense Module
- Add new expense  
- Update existing expense  
- Delete expense  
- ORM based operations

b) Report Module
- Category wise total  
- Aggregation using GROUP BY  
- Raw SQL joins

c) Budget Module
- Set monthly limit  
- Compare with spending  
- Alert when exceeded

d) Search Module
- Find expenses by date using SQL query"""

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, func, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
# Step 1: Create database engine
engine = create_engine("sqlite:///FintrackPro.db")
# Step 2: Create base class
Base = declarative_base()
# Step 3: Define tables
#Category table with one-to-many relationship to Expense
class Category(Base):
    __tablename__ = "categories"#Table name in database
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    expenses = relationship("Expense", back_populates="category")#Relationship to Expense table
#Expense table with foreign key to Category
class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(Date)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")
#Subscription table
class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    next_date = Column(Date)
#Budget table
class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True)
    month = Column(String, unique=True)
    limit = Column(Float)
Base.metadata.create_all(engine)#Create tables in the database
Session = sessionmaker(bind=engine)#Create session factory and bind to engine
Session = Session()#Create session instance for database operations used for inserting, updating, deleting and querying data from the database
#Functions for each feature of the system
def add_category():#Function to add new category
    name = input("Enter category name: ")
    Session.add(Category(name=name))#Add new category to session
    Session.commit()#Commit changes to database
    print("Category added successfully.")
def add_expense():#Function to add new expense
    title = input("Enter expense title: ")
    amount = float(input("Enter expense amount: "))
#Parse date input and convert to date object
    date = datetime.strptime(
        input("Enter expense date (YYYY-MM-DD): "),
        "%Y-%m-%d"
    ).date()

    category_id = int(input("Enter category ID: "))
#Create expense object and add to session
    Session.add(
        Expense(
            title=title,
            amount=amount,
            date=date,
            category_id=category_id
        )
    )
    Session.commit()#Commit changes to database
    print(" Expense added successfully")
def update_expense():#Function to update existing expense
    eid = int(input("Enter expense ID to update: "))
    expense = Session.query(Expense).filter_by(id=eid).first()#Query expense by ID
    if expense:#If expense exists, update details
        new_title = input("Enter new expense title: ")
        new_amount = float(input("Enter new expense amount: "))
        new_date = input("Enter new expense date (YYYY-MM-DD): ")
        new_category_id = int(input("Enter new category ID: "))
        expense.title = new_title
        expense.amount = new_amount
        expense.date = datetime.strptime(new_date, "%Y-%m-%d").date()#Convert string to date object
        expense.category_id = new_category_id
        Session.commit()#Commit changes to database
        print("Expense updated successfully.")
    else:
        print("Expense not found.")
def delete_expense():#Function to delete expense
    eid = int(input("Enter expense ID to delete: "))
    expense = Session.query(Expense).filter_by(id=eid).first()#Query expense by ID
    if expense:
        Session.delete(expense)#Delete expense from session
        Session.commit()#Commit changes to database
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")
def search_by_date():#Function to search expenses by date
    date = input("Enter date to search (YYYY-MM-DD): ")
    expenses = Session.query(Expense).filter_by(date=date).all()#Query expenses by date
    if expenses:
        for exp in expenses:#Print details of each expense found
            print(f"ID: {exp.id}, Title: {exp.title}, Amount: {exp.amount}, Category ID: {exp.category_id}")
    else:
        print("No expenses found for the given date.")
def category_analytics():#Function to perform category-wise analytics
    from sqlalchemy import func #Import func for aggregation
    #Use raw SQL query to perform join and aggregation
    analytics = Session.query(Category.name, func.sum(Expense.amount)).join(Expense).group_by(Category.id).all()
    for category, total in analytics:#Print category name and total amount spent in that category
        print(f"Category: {category}, Total Spent: {total}")
def set_monthly_budget():#Function to set or update monthly budget
    month = input("Enter month (YYYY-MM): ")
    limit = float(input("Enter monthly budget limit: "))
    #Check if budget for the month already exists, if yes update it, otherwise create new budget entry
    existing_budget = Session.query(Budget).filter_by(month=month).first()
    if existing_budget:#If budget exists, update the limit
        existing_budget.limit = limit
        print("Budget updated successfully.")
    else:
        Session.add(Budget(month=month, limit=limit))#Add new budget to session
        print("Budget set successfully.")
    Session.commit()
def budget_alert():#Function to alert if budget exceeded
    month = input("Enter month to check: ")

    budget = Session.query(Budget).filter_by(month=month).first()#Query budget for the given month
    if not budget:#If no budget set for the month
        print(" No budget set for this month")
        return

    total = Session.execute(text(f"""
        SELECT SUM(amount) FROM expenses
    """)).scalar() or 0 #Calculate total spending for the month

    print(f" Total Spending: ₹{total}")
    print(f" Budget Limit: ₹{budget.limit}")

    if total > budget.limit:
        print(" Budget Exceeded!")
    else:
        print(" Within Budget")
while True:
    print("\nFinTrack Pro - Personal Finance Management")
    print("1. Add Category")
    print("2. Add Expense")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search by Date")
    print("6. Category Analytics")
    print("7. Set Monthly Budget")
    print("8. Budget Alert")
    print("9. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_category()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        update_expense()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        search_by_date()
    elif choice == '6':
        category_analytics()
    elif choice == '7':
        set_monthly_budget()
    elif choice == '8':
        budget_alert()
    elif choice == '9':
        print("Exiting FinTrack Pro. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
        


