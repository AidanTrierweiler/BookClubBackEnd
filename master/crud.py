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

from models import Club
from database import session

'''
 Class Outline: Cole
'''


def setClub(club):
    session.add(club)
    session.commit()


def getFromId(id):
    id_club = session.query(Club).filter(Club.id == id).first()
    if (id_club == None):
        print("There is no book with this id")
    else:
        return id_club
'''
:return: the name of the club
'''
def getFromName(name):
    name_club = session.query(Club).filter(Club.name == name).first()
    if (name_club == None):
        print("There is no book with this id")
    else:
        return name_club

def getFromDirector(director):
    director_clubs = session.query(Club).filter(Club.director_id == director).first()
    if (director_clubs == None):
        print("There is no book with this id")
    else:
        return director_clubs

'''
:param name: a string that will be the new name for the club
:return:
'''
def setName(self, name):
    pass

'''
:return: the user who is the director of the club
'''


'''
:param user: the user who will be the new director of the club
:return:
'''
def setDirector(self, user):
    pass

'''
:return: the user who is currently the monthly host
'''
def getMonthlyHost(self):
    pass

'''
:param user: the user who will be the new monthly host for the club
:return:
'''
def setMonthlyHost(self, user):
    pass

'''
:return: the list of all members in the club
'''
def getMembers(self):
    pass

'''
:param name: the name of the user 
:return: the member object associated with the input name
'''
def getMember(self, name):
    pass

'''
:param user: a user object that will be added to the club memberList
:return:
'''
def addMember(self, user):
    pass

'''
:return: a list of all books the club has read in the past
'''
def get_books(self):
    pass

'''
:param title: the title of a book that is being searched for in the club's books list
:return: the book object that has the input title
'''
def get_book(self, title):
    pass

'''
:param book: a book object that will be added to the books list
:return:
'''
def addBook(self, book):
    pass

'''
:param address: a string that is the address for the club meeting location
:return:
'''
def setMeetingLocation(self, address):
    pass

'''
:return: the current meeting location for the club
'''
def getMeetingLocation(self):
    pass

'''
    Class outline: Aidan
    Class implementation
'''


class User:

    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__books = []
        self.__clubs = []
        self.__ownedClubs = []
        self.__isMonthlyHost = False
        self.__reviews = []

    def __repr__(self):
        return f"User: {self.__name}"

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
    def setName(self, name):
        self.__name = name

    '''
    Returns the user's password
    :return: str
     '''
    def getPassword(self):
        return self.__password

    '''
        Sets the user's password
        :param password: New password for the user
        :return: None
        '''
    def setPassword(self, password):
        self.__password = password

    '''
        Returns a list of books associated with the user
        :return: list[Book]
        '''
    def getBooks(self):
        return self.__books

    '''
        Returns the book with the specified title associated with the user
        :param title: Title of the book to retrieve
        :return: Book
        '''
    def getBook(self, title):
        for book in self.__books:
            if book.getTitle() == title:
                return book
        return None


    '''
    Returns a list of books by the specified author associated with the user
    :param author: Author of the books to retrieve
    :return: list[Book]
    '''
    def getBooksByAuthor(self, author):
        for book in self.__books:
            if book.getAuthot() == author:
                return book
        return None

    '''
        Sets a book for the user
        :param book: Book object to set
        :return: None
        '''
    def setBook(self, book):
        self.__books.append(book)

        '''
        Returns a list of clubs associated with the user
        :return: list[Club]
        '''
    def getClubs(self):
        return self.__clubs


    '''
        Returns the club with the specified name associated with the user
        :param name: Name of the club to retrieve
        :return: Club
        '''
    def getClub(self, name):
        for club in self.__clubs:
            if club.getName() == name:
                return club
        return None

    '''
    Adds a club to the user's list of clubs
        :param club: Club object to add
        :return: None
        '''
    def addClub(self, club):
        self.__clubs.append(club)


    '''
            Checks if the user is the monthly host
            :return: bool
            '''
    def isMonthlyHost(self):
        return self.__isMonthlyHost

    '''
            Returns a list of reviews associated with the user
            :return: list[Review]
            '''
    def getReviews(self):
        return self.__reviews

    '''
            Returns a list of reviews written on the specified date associated with the user
            :param date: Date of the reviews to retrieve
            :return: list[Review]
            '''
    def getReviewByDate(self, date):
        for review in self.__reviews:
            if review.getDate() == date:
                return review
        return None

    '''
            Returns a list of reviews with the specified rating associated with the user
            :param rate: Rating of the reviews to retrieve
            :return: list[Review]
            '''
    def getReviewByRate(self, rate):
        reviewList = []
        for review in self.__reviews:
            if review.getRate() == rate:
                reviewList.append(review)
        if len(reviewList) == 0:
            return None
        return reviewList

    '''
            Adds a review to the user's list of reviews
            :param review: Review object to add
            :return: None
            '''
    def addReview(self, review):
        self.__reviews.append(review)

