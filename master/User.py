
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

