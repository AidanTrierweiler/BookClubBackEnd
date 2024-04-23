from master.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from database import session
from models import Book

'''
    Class Outline: Matt
'''
Base = declarative_base()



'''Add book to databse'''

def set_book(book):
    # Add the book to the session
    session.add(book)

    # Commit the transaction to persist the book to the database
    session.commit()

'''Returns book from given id'''
def get_book_from_id(id):
    id_book = session.query(Book).filter(Book.id == id).first()
    if (id_book == None):
        print("There is no book with this id")
    else:
        return id_book

'''Returns book with specific title'''
def get_book_from_title(term):
    title_book = session.query(Book).filter(Book.title == term).first()
    if(title_book == None):
        print("There is no book with this title")
    else:
        return title_book

'''Return the books of a specific author'''
def get_author(name):
    auth_books = session.query(Book).filter(Book.title == name).first()
    if (auth_books == None):
        print("There is no book with this title")
    else:
        return auth_books

'''Sets the Books author if it doesnt have one'''
def set_author(book, name):
    pass

'''Returns the books release date'''
def get_release(self):
    pass

'''Returns a list of all the books reviews'''
def get_reviews(self):
    pass

'''Reuturns the review of a book from a certain user'''
def get_review(self, user):
    pass

'''Adds a review to a book'''
def add_review(self, review):
    pass

'''???'''
def update_rate(self, newRate):
    pass

