
    '''
    Class outline: Kaiden
    Class Implemntation:
    '''


class DirectorSoftware(MemberSoftware):

    # needs to have the club the director is trying to work one and a list of all users from that club from the DB
    def __init__(self):
        pass

    def __repr__(self):
        pass

    '''
    Allows director of club to set the monthly host of the book club
    :param user: The user that is the director of the club
    :param club: The club that is being affected by the user
    :param name: name of theuser to be sat as the monthly host
    :return: None
    '''
    def setMonthlyHost(self, director, club, name):
        pass

    '''
        returns the user that is the current monthly host of the club
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :return: User
        '''
    def getMonthlyHost(self, director, club):
        pass

        '''
        gets a list of all users in the club
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :return: List<User>
        '''
    def getMembers(self, director, club):
        pass

        '''
        returns a member from the club given the name of the user
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user
        :param name: The name of the user trying to be returned 
        :return: User
        '''
    def getMember(self, director, club, name):
        pass

        '''
        gets a book using the title and adds it to the clubs list of books
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :param title: name of the book that is being added
        :return: Void
        '''
    def addBookToClub(self, director, club, title):
        pass

        '''
        removes a book object from the club book list history
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :param title: The title of the book that is to be added
        :return: Void
        '''
    def removeBookFromClub(self, director, club, title):
        pass

        '''
        This Might need to move to MemberSoftware??
        Gets all the books that are in book club
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :return: List<Book>
        '''
    def getAllClubBooks(self, director, club):
        pass

        '''
        This Might need to move to MemberSoftware?? 
        gets a book from the club given the title 
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :param title: Title of the book being requested
        :return: Book
        '''
    def getClubBook(self, director, club, title):
        pass

        '''
        allows the requested user to join the club
        :param user: The user that is the director of the club
        :param club: The club that is being affected by the user 
        :param name: name of the user allowed into the club
        :return: Void
        '''
    def acceptMember(self, director, club, name):
        pass













