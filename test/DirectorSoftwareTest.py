
'''
File outline: Kaiden
Class Implementation:
'''

import ClubClass
import User
import DirectorSoftware

test_club_1 = ClubClass()
'''set all attributes of testClub1'''
test_user_0 = User()
test_director_user_0 = User()
test_director_user_0.ownedClubs.add(test_club_1)

'''Make test_user_1 have the name "Tester One"'''
test_user_1 = User()
test_user_2 = User()
test_user_3 = User()
test_club_1.addMember(test_user_1)
test_club_1.addMember(test_user_2)
test_club_1.addMember(test_user_3)

'''
Integration Test

creates director, club, and user to see if the director can set the clubs monthly host to a user
'''
def set_monthly_host_test():
    DirectorSoftware.set_monthly_host(test_director_user_0, test_club_1, test_user_0)

    assert test_club_1.get_monthly_host.getName() == test_user_0.getName()

    '''
    Integration Test

    creates director, club, and user to see if the director can retrieve the monthly host of the club
    '''
def get_monthly_host_test():
    result = DirectorSoftware.get_monthly_host(test_director_user_0, test_club_1)

    assert result.getName() == test_user_0.getName()

    '''
    Integration Test

    creates director, club, and user to see if the director can retrieve all users from a club
    '''
def get_members_test():
    result = test_club_1.get_members()

    expected_result = []
    expected_result.append(test_user_1)
    expected_result.append(test_user_2)
    expected_result.append(test_user_3)

    assert result == expected_result

    '''
    Integration Test

    creates director, club, and users to see if the director can get a specific member from a club
    '''
def get_member_test():
    result = DirectorSoftware.get_member(test_director_user_0, test_club_1, "Tester One")

    assert result == test_user_1

    '''
    Integration Test

    creates director, club, and book to see if the director can add a book to the club list
    '''
def add_book_to_club_test():
    pass

    '''
    Integration Test

    creates director, club, and books to see if the director can remove a book from the club list
    '''
def remove_book_from_club_test():
    pass

    '''
    Integration Test

    creates director, club, and books to see if the director can retrieve all books from the club list 
    '''
def get_all_club_books_test():
    pass

    '''
    Integration Test

    creates director, club, and book to see if the director can retrieve a specific book from the clubs book list
    '''
def get_club_book_test():
    pass

    '''
    Integration Test

    creates director, club, and user to see if the director can accept a member request to join a club
    '''
def accept_member_test():
    pass








