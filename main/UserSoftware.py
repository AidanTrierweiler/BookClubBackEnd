
    '''
    Class outline: Aidan
    Class implementation
    '''


class UserSoftware:

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def getId(self):
        pass
        '''
        Returns the user's ID
        :return: int
        '''

    def getName(self):
        pass
        '''
        Returns the user's name
        :return: str
        '''

    def setName(self, name):
        pass
        '''
        Sets the user's name
        :param name: New name for the user
        :return: None
        '''

    def getPassword(self):
        pass
        '''
        Returns the user's password
        :return: str
        '''

    def setPassword(self, password):
        pass
        '''
        Sets the user's password
        :param password: New password for the user
        :return: None
        '''

    def getBooks(self):
        pass
        '''
        Returns a list of books associated with the user
        :return: list[Book]
        '''

    def getBook(self, title):
        pass
        '''
        Returns the book with the specified title associated with the user
        :param title: Title of the book to retrieve
        :return: Book
        '''

    def getBooksByAuthor(self, author):
        pass
        '''
        Returns a list of books by the specified author associated with the user
        :param author: Author of the books to retrieve
        :return: list[Book]
        '''

    def setBook(self, book):
        pass
        '''
        Sets a book for the user
        :param book: Book object to set
        :return: None
        '''

    def getClubs(self):
        pass
        '''
        Returns a list of clubs associated with the user
        :return: list[Club]
        '''

    def getClub(self, name):
        pass
        '''
        Returns the club with the specified name associated with the user
        :param name: Name of the club to retrieve
        :return: Club
        '''

    def addClub(self, club):
        pass
        '''
        Adds a club to the user's list of clubs
        :param club: Club object to add
        :return: None
        '''

    def isMonthlyHost(self):
        pass
        '''
        Checks if the user is the monthly host
        :return: bool
        '''

    def getReviews(self):
        pass
        '''
        Returns a list of reviews associated with the user
        :return: list[Review]
        '''

    def getReviewByUser(self, user):
        pass
        '''
        Returns a list of reviews written by the specified user associated with the user
        :param user: User whose reviews to retrieve
        :return: list[Review]
        '''

    def getReviewByDate(self, date):
        pass
        '''
        Returns a list of reviews written on the specified date associated with the user
        :param date: Date of the reviews to retrieve
        :return: list[Review]
        '''

    def getReviewByRate(self, rate):
        pass
        '''
        Returns a list of reviews with the specified rating associated with the user
        :param rate: Rating of the reviews to retrieve
        :return: list[Review]
        '''

    def addReview(self, review):
        pass
        '''
        Adds a review to the user's list of reviews
        :param review: Review object to add
        :return: None
        '''
