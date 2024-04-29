from master.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base
from master.database import session
from master.models import Book, Club, User



'''
    Class Outline: Matt
'''
Base = declarative_base()


"""Book Functoins"""

'''Add Book to Database'''
def set_book(book, session):
    # Add the book to the session
    session.add(book)
    # Commit the transaction to persist the book to the database
    session.commit()

'''Returns book from given id'''
def get_book_from_id(id, session):
    id_book = session.query(Book).filter(Book.id == id).first()
    if (id_book == None):
        print("There is no book with this id")
    else:
        return id_book

'''Returns book with specific title'''
def get_book_from_title(title, session):
    title_book = session.query(Book).filter(Book.title == title).first()
    if title_book is None:
        print("There is no book with this title")
    else:
        return title_book

'''Return the books of a specific author'''
def get_author(name, session):
    auth_books = session.query(Book).filter(Book.author == name).all()
    if not auth_books:
        print("There are no books by this author")
    return auth_books



"""Club Functions"""

'''Adds a club to database'''
def set_club(club, session):
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
def get_club_from_name(name, session):
    name_club = session.query(Club).filter(Club.name == name).first()
    if (name_club == None):
        print("There is no book with this id")
    else:
        return name_club

'''Gets clubs with certain director'''
#def getFromDirector(director):
 #   director_clubs = session.query(Club).filter(Club.director_id == director).first()
  #  if (director_clubs == None):
   #     print("There is no book with this id")
    #else:
     #   return director_clubs



"""User Functions"""

'''Adds new user to database'''
def setUser(user, session):
    session.add(user)
    session.commit()


'''Gets a user from the database given an id'''
def getUserFromId(id, session):
    id_user = session.query(User).filter(User.id == id).first()
    if id_user is None:
        print("There is no user with this id")
    else:
        return id_user


'''Gets a user from their email'''
def getUserFromEmail(email, session):
    email_user = session.query(User).filter(User.email == email).first()
    if email_user is None:
        print("There is no user with this email")
    else:
        return email_user





