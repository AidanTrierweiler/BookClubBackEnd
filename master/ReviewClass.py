'''
    Class Outline: Matt
'''

import mysql.connector

class Review:

    def __init__(self):
        pass

    def __repr__(self):
        pass

    '''Returns the ID of the review'''
    def get_id(self):
        pass

    '''Returns the user who wrote the review'''
    def get_user(self):
        pass

    '''Sets the user for a new review'''
    def set_user(self, User):
        pass

    '''Returns the book that the review is about'''
    def get_book(self):
        pass

    '''Ties the review to a book'''
    def set_book(self, Book):
        pass

    '''Returns the date the review was written'''
    def get_data(self):
        pass

    '''Sets the date for a new review'''
    def set_data(self, Date):
        pass

    '''Gets the rating from a review'''
    def get_rate(self):
        pass

    '''Allows teh user to rate a book with the review'''
    def set_rate(self, rating):
        pass

    '''Returns the contents of the review'''
    def get_content(self):
        pass

    '''Allows teh user to write a review paragraph'''
    def set_content(self, content):
        pass