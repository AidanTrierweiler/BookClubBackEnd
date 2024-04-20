
    '''
    Class outline: Aidan
    Class implementation
    '''


class UserSoftware:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.books = []
        self.clubs = []
        self.ownedClubs = []
        self.isMonthlyHost = False
        self.reviews = []

    def __repr__(self):
        return f"User: self.name"

    def getId(self):
        pass
        '''
        Returns the user's ID
        :return: int
        '''

    def getName(self):
        return self.name

    '''
    Sets the user's name
    :param name: New name for the user
    :return: None
    '''
    def setName(self, name):
        self.name = name

    '''
    Returns the user's password
    :return: str
     '''
    def getPassword(self):
        return self.password

    '''
        Sets the user's password
        :param password: New password for the user
        :return: None
        '''
    def setPassword(self, password):
        self.password = password

    '''
        Returns a list of books associated with the user
        :return: list[Book]
        '''
    def getBooks(self):
        return self.books

    '''
        Returns the book with the specified title associated with the user
        :param title: Title of the book to retrieve
        :return: Book
        '''
    def getBook(self, title):
        for book in self.books:
            if book.getTitle() == title:
                return book
        return None

        # for book in self.books:
        #     if book.getTitle() == title:
        #         return book
        # return None


     '''
        Returns a list of books by the specified author associated with the user
        :param author: Author of the books to retrieve
        :return: list[Book]
        '''
    def getBooksByAuthor(self, author):
        for book in self.books:
            if book.getAuthot() == author:
                return book
        return None

    '''
        Sets a book for the user
        :param book: Book object to set
        :return: None
        '''
    def setBook(self, book):
        self.books.append(book)

        '''
        Returns a list of clubs associated with the user
        :return: list[Club]
        '''
    def getClubs(self):
        return self.clubs


    '''
        Returns the club with the specified name associated with the user
        :param name: Name of the club to retrieve
        :return: Club
        '''
    def getClub(self, name):
        for club in self.clubs:
            if club.getName() == name:
                return club
        return None

        # for club in self.clubs:
        #     if club.getName() == name:
        #         return club
        # return None

      '''
        Adds a club to the user's list of clubs
        :param club: Club object to add
        :return: None
        '''
    def addClub(self, club):
        self.clubs.append(club)


    '''
            Checks if the user is the monthly host
            :return: bool
            '''
    def isMonthlyHost(self):
        return self.isMonthlyHost

    '''
            Returns a list of reviews associated with the user
            :return: list[Review]
            '''
    def getReviews(self):
        return self.reviews

    '''
            Returns a list of reviews written on the specified date associated with the user
            :param date: Date of the reviews to retrieve
            :return: list[Review]
            '''
    def getReviewByDate(self, date):
        for review in self.reviews:
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
        for review in self.reviews:
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
        self.reviews.append(review)

