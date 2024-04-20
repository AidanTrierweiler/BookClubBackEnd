'''
    Class Outline: Matt
'''

import mysql.connector

class Review:

    def __init__(self, user, book, date, rate, content):
        self.__user = user
        self.__book = book
        self.__date = date
        self.__rate = rate
        self.__content = content

    def __repr__(self):
        return f"{self.__user.getName()} rated {self.__book.getName()} a {self.__book.getRate()}"

    '''Returns the ID of the review'''
    def get_id(self):
        pass

    '''Returns the user who wrote the review'''
    def get_user(self):
        return self.__user

    '''Sets the user for a new review'''
    def set_user(self, user):
        self.__user = user

    '''Returns the book that the review is about'''
    def get_book(self):
        return self.__book

    '''Ties the review to a book'''
    def set_book(self, book):
        self.__book = book

    '''Returns the date the review was written'''
    def get_data(self):
        return self.__date

    '''Sets the date for a new review'''
    def set_data(self, date):
        self.__date = date

    '''Gets the rating from a review'''
    def get_rate(self):
        return self.__rate

    '''Allows teh user to rate a book with the review'''
    def set_rate(self, rate):
        self.__rate = rate

    '''Returns the contents of the review'''
    def get_content(self):
        return self.__content

    '''Allows teh user to write a review paragraph'''
    def set_content(self, content):
        self.__content = content