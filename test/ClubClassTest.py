'''
Outline: Cole
'''

import ClubClass

testClub0 = ClubClass()
''' Set all attributes of testClub0 to be the stuff from the tests below once it's init method has been declared'''

'''
Assures the club object is created with all the correct attributes.
'''
def constructorTest():
    pass

'''
Assures that the repr method returns the correct string
'''
def reprTest():
    pass

'''
Assures the correct ID is returned
'''
def getIdTest():
    result = testClub0.getId()

    expectedId = 0
    assert result == expectedId

'''
Assures the correct name is returned
'''
def getNameTest():
    result = testClub0.getName()

    expectedName = "Test Club 0"
    assert result == expectedName

'''
Assures that when the name attribute is altered the string is updated correctly
'''
def setNameTest():
    testClub0.setName("Set Name Test")

    assert testClub0.getName() == "Set Name Test"

'''
Assures that the correct user object is returned when the director is asked for
'''
def getDirectorTest():
    result = testClub0.getDirector().getName()

    expectedName = "Clark Kent"
    assert result == expectedName

'''
Assures that the director attribute is updated correctly
'''
def setDirectorTest():
    testClub0.setDirector("Peter Parker")

    assert testClub0.getDirector().getName() == "Peter Parker"

'''
Assures that when the monthly host is asked for the correct user object is returned
'''
def getMonthlyHostTest():
    result = testClub0.getMonthlyHost().getName()

    expectedName = "Bruce Wayne"
    assert result == expectedName

'''
Assures that the monthly host attribute is updated correctly
'''
def setMonthlyHostTest():
    testClub0.setMonthlyHost("Willy Wonka")

    assert testClub0.getMonthlyHost.getName() == "Willy Wonka"

'''
Assures that the correct list of users is returned
'''
def getMembersTest():
    members = testClub0.getMembers()

    '''Maybe change this to check IDs so that everything is unique, I just don't know what the ids will be yet'''
    expectedNames = "Member One, Member Two, Member Three"
    actualNames = ""
    for user in members:
        if actualNames == "":
            actualNames += user.getName()
        else:
            actualNames += ", " + user.getName()

    assert  expectedNames == actualNames

'''
Assures that the correct user object is returned when asking for a specific member of the club
'''
def getMemberTest():
    ''' maybe change to use id as well'''
    result = testClub0.getMember("Member One")

    assert result.getName() == "Member One"

'''
Assures that the user list attribute is updated ocrrectly when a member is added to the club
'''
def addMemberTest():
    '''create member here'''
    testClub0.addMember('''created member goes here''')

    assert '''created member''' in testClub0.getMembers()

'''
Assures that the correct list of books is returned
'''
def getBooksTest():
    books = testClub0.getBooks()
    '''ID instead of book titles?'''

    '''make the real book titles once book JSON and implementation has been worked out'''
    expectedBooks = "Book One, Book Two, Book Three"
    actualBooks = ""

    for book in books:
        if actualBooks == "":
            actualBooks += book.getTitle()
        else:
            actualBooks += ", " + book.getTitle()

    assert actualBooks == expectedBooks

'''
Assures the correct book object is returned when a specific one is asked for
'''
def getBookTest():
    ''' maybe change to use id as well'''
    result = testClub0.getBook("Book One")

    assert result.getTitle() == "Book One"

'''
Assures that the books list is updated correctly
'''
def addBookTest():
    '''create book here'''
    testClub0.addBook('''created book here''')

    assert '''created book''' in testClub0.getBooks()

'''
Assures that the meeting location attribute is updated correctly
'''
def setMeetingLocationTest():
    testClub0.setMeetingLocation("123 Example Road")

    assert testClub0.getLocation() == "123 Example Road"

'''
Assures that the correct meeting location is returned
'''
def getMeetingLocationTest():
    result = testClub0.getMeetingLocation()

    assert result == "123 Example Road"