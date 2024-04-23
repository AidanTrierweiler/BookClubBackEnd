from master.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from database import session
from models import Book, Club, User

'''
    Class Outline: Matt
'''
Base = declarative_base()


"""Book Functoins"""

'''Add Book to Database'''
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



"""Club Functions"""

'''Adds a club to database'''
def setClub(club):
    session.add(club)
    session.commit()


'''Gets club with certain id'''
def getFromId(id):
    id_club = session.query(Club).filter(Club.id == id).first()
    if (id_club == None):
        print("There is no book with this id")
    else:

        return id_club
'''
Gets club with certain name
'''
def getFromName(name):
    name_club = session.query(Club).filter(Club.name == name).first()
    if (name_club == None):
        print("There is no book with this id")
    else:
        return name_club

'''Gets clubs with certain director'''
def getFromDirector(director):
    director_clubs = session.query(Club).filter(Club.director_id == director).first()
    if (director_clubs == None):
        print("There is no book with this id")
    else:
        return director_clubs



"""User Functions"""

'''Adds new suer to database'''
def setName(self, name):
    self.__name = name
def getId(self):
    pass
    '''
    Returns the user's ID
    :return: int
    '''

def getName(self):
    return self.__name

'''
Sets the user's name
:param name: New name for the user
:return: None
'''




