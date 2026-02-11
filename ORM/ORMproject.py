#add_category()->add books category
#add_book()->add new book
#borrow_book()->borrow a book
#update_book()->update book information
#search_book()->find borrowed books by date
#category_report()->generate report of books in each category
#set_limit()->set borrowing limit for each category
#limit_alert()->alert when borrowing limit is reached

from unicodedata import category
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey,text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
#data base connection
engine = create_engine("sqlite:///libtrack.db")
Base = declarative_base()
Session=sessionmaker(bind=engine)
Session=Session()
class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship("Book", back_populates="category")
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="books")
    borrows = relationship("Borrow", back_populates="book")

class Borrow(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    borrow_date = Column(Date)
    book = relationship("Book", back_populates="borrows")
class Limit(Base):
    __tablename__ = "limits"
    id = Column(Integer, primary_key=True)
    month=Column(String, unique=True)
    max_books = Column(Integer)
    Base.metadata.create_all(engine)
def add_category():
    name = input("Enter category name: ")
    Session.add(Category(name=name))
    Session.commit()
    print("Category added successfully.")
def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    category_id=int(input("Enter category ID: "))
    #create book object and add to session
    Session.add(Book(title=title, author=author, category_id=category_id))
    Session.commit()
    print("Book added successfully.")
def borrow_book():
    book_id=int(input("Enter book ID to borrow: "))
    borrow_date=input("Enter borrow date (YYYY-MM-DD): ")
    Session.add(Borrow(book_id=book_id, borrow_date=borrow_date))
    Session.commit()
    print("Book borrowed successfully.")
def update_borrow():
    bid=int(input("Enter borrow ID to update: "))
    borrow=Session.query(Borrow).filter_by(id=bid).first()
    if borrow:
        new_date=input("Enter new borrow date (YYYY-MM-DD): ")
        borrow.borrow_date=new_date
        Session.commit()
        print("Borrow updated successfully.")
    else:
        print("Borrow not found.")
def delete_borrow():
    bid=int(input("Enter borrow ID to delete: "))
    borrow=Session.query(Borrow).filter_by(id=bid).first()
    if borrow:
        Session.delete(borrow)
        Session.commit()
        print("Borrow deleted successfully.")
    else:
        print("Borrow not found.")

def search_book():
    date=input("Enter borrow date to search (YYYY-MM-DD): ")
    borrows=Session.query(Borrow).filter_by(borrow_date=date).all()
    if borrows:
        for borrow in borrows:
            book=Session.query(Book).filter_by(id=borrow.book_id).first()
            print(f"Book ID: {book.id}, Title: {book.title}, Author: {book.author}")
    else:
        print("No books found for the given date.")
def category_report():
    categories=Session.query(Category).all()
    for category in categories:
        print(f"Category: {category.name}, Books: {len(category.books)}")
def set_limit():
    month=input("Enter month to set limit (e.g., January): ")
    max_books=int(input("Enter maximum books for the month: "))
    limit=Session.query(Limit).filter_by(month=month).first()
    if limit:
        limit.max_books=max_books
    else:
        Session.add(Limit(month=month, max_books=max_books))
    Session.commit()
    print("Limit set successfully.")
def limit_alert():
    month=input("Enter month to check limit (e.g., January): ")
    limit=Session.query(Limit).filter_by(month=month).first()
    if limit:
        borrow_count=Session.query(Borrow).filter(text("strftime('%m', borrow_date) = :month")).params(month=month[:3]).count()
        if borrow_count >= limit.max_books:
            print("Borrowing limit reached for the month.")
        else:
            print(f"Borrowing count for {month}: {borrow_count}/{limit.max_books}")
    else:
        print("No limit set for the month.")
while True:
    print("\nLibrary Management System")
    print("1. Add Category")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Update Borrow")
    print("5. Delete Borrow")
    print("6. Search Book by Date")
    print("7. Category Report")
    print("8. Set Borrowing Limit")
    print("9. Check Borrowing Limit Alert")
    print("0. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_category()
    elif choice == '2':
        add_book()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        update_borrow()
    elif choice == '5':
        delete_borrow()
    elif choice == '6':
        search_book()
    elif choice == '7':
        category_report()
    elif choice == '8':
        set_limit()
    elif choice == '9':
        limit_alert()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")



   