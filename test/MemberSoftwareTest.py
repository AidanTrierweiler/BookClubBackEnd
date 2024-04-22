'''
File outline: Kaiden
Class Implementation:
'''

import master.ClubClass as ClubClass
import master.User as User
from master.MemberSoftware import MemberSoftware
import master.DirectorSoftware as DirectorSoftware
import master.BookClass as BookClass

test_club_1 = ClubClass()
'''set all attributes of testClub1'''
test_user_0 = User()
test_director_user_0 = User()
test_director_user_0.__ownedClubs.add(test_club_1)

'''Make test_user_1 have the name "Tester One"'''
test_user_1 = User()
test_user_2 = User()
test_user_3 = User()
test_club_1.addMember(test_user_1)
test_club_1.addMember(test_user_2)
test_club_1.addMember(test_user_3)

'''
Integration Test

creates club, and user to checks to see if you can check and change if a user is the monthly host
    '''


def checkIfHostTest():
    MemberSoftware.__checkIfHost(test_user_1)

    '''
Integration Test
        
creates club, and user to see if a user, if is the monthly host, can set the meeting location 
        '''


def setMeetingLocationTest():
    MemberSoftware.setMeetingLocation(test_user_1, "location")

    '''
Integration test

creates club, and user to see if a user can request to join a club
        '''


def requestToJoinClubTest():
    pass

    '''
Integration test
        
creates club, and user to see if a user can remove theor account from a club list
        '''


def leaveClubTest():
    pass

    '''
Integration Test

creates Book, and user to see if a book can be added to the user books list
        '''


def addBookTest():
    pass

    '''
Integration test

creates book, and user to see f a book can be removed from a users book list      
        '''


def removeBookTest():
    pass

    '''
Integration Test

creates books, and user to see of a user can return the entire list of books in the object
        '''


def getBooksTest():
    pass

    '''
Integration Test

creates books, and user to see of user can return a specific book from their account
        '''


def getBookTest():
    pass

    '''
Integration Test        
    
creates books, and user to see of a user account can return all books in their list be a given author        
        '''


def getBooksByAuthorTest():
    pass

    '''
Integration Test        
        
creates clubs, and user to see if a user can return all the clubs that they are a part of      '''


def getClubsTest():
    pass

    '''
Integration test        
        
creates clubs, and user to see if a user can return a specific club from their list     '''


def getClubTest():
    pass

    '''
Integration test

creates user to see of it can be removed from the system
        '''


def deleteAccountTest():
    pass

    '''
Integration Test
        
creates user to see if the account can be used to create a new club with the user set as the dirctor
        '''


def createClubTest():
    pass
