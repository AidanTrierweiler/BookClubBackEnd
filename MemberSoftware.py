
        '''
        Class outline: Kaiden
        Class Implementation:
        '''


class MemberSoftware:

    # initilizing the user in the class so the methods can be called on a specific user
    def __init__(self):
        self.__user = user

    def __repr__(self):
        pass

        '''
        :param user: The user logged into the software
        :return:  True if the user is a host or False if not
        '''
    def __checkIfHost(self, user):
        pass

        '''
        Allows user to set a meeting location time if they are the monthly host
        :param user: The user logged into the software
        :param Book: 
        :return: 
        '''
    def setMeetingLocation(self, user, location):
        pass

        '''
        Allows user to request to join a club
        :param user: The user logged into the software
        :param Book: 
        :return: 
        '''
    def requestToJoinClub(self, user, club):
        pass

        '''
        Removes club out of the list of clubs a user object posseses
        :param user: The user logged into the software
        :param club: 
        :return: none
        '''
    def leaveClub(self, user, club):
        pass

        '''
        Takes a book and calls the addBook function for the user
        :param user: The user logged into the software
        :param Book: Book Object to be added to a user object
        :return: none
        '''
    def addBook(self, user, Book):
        pass

        '''
        Takes a title of a book,calles from the DB, and calls the addBook function for the user
        :param user: The user logged into the software
        :param tile: Book Object to be added to a user object
        :return: none
        '''
    def addBook(self, user, title):
        pass

        '''
        Takes a book object and calls the removeBook class from the user
        :param user: The user logged into the software
        :param book: The book object to be removed
        :return: none
        '''
    def removeBook(self, user, book):
        pass

        '''        
        Takes a title of a book, calls book from DB, and calls the removeBook class from the user
        :param user: The user logged into the software
        :param title: tile of book to be removed from the user
        :return: none
        '''
    def removeBook(self, user, title):
        pass

        '''
        request the entire list of books contained from user but calling getBooks() on user
        :param user: The user logged into the software
        :return: List<Book>
        '''
    def getBooks(self, user):
        pass

        '''
        request a specific book by calling getBook() on user
        :param user: The user logged into the software
        :param book: book to be retrieved from user
        :return: Book
        '''
    def getBook(self, user, title):
        pass

        '''
        request a specific book by using title to query from DB and by calling getBook() on user
        :param user: The user logged into the software
        :param title: title of book to be retrieved from user
        :return: Book
        '''
    def getBook(self, user, title):
        pass

        '''
        return all books in a user object by a single author
        :param user: The user logged into the software
        :param author: author of books requested
        :return: List<Book>
        '''
    def getBooksByAuthor(self, user, author):
        pass

        '''
        get list of clubs that a user contains
        :param user: The user logged into the software
        :return: List<Club>
        '''
    def getClubs(self, user):
        pass

        '''
        :param user: The user logged into the software
        :param name: name of the club being requested
        :return: Club
        '''
    def getClub(self, user, name):
        pass

        '''
        removes account from from DB
        :param user: The user logged into the software
        :return: none
        '''
    def deleteAccount(self, user):
        pass

        '''
        creates a club and adds it to user object
        :param user: The user logged into the software
        :return: none
        '''
    def createClub(self, user):
        pass









