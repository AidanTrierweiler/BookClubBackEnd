from models import Club
from database import session

'''
 Class Outline: Cole
'''


def setClub(club):
    session.add(club)
    session.commit()


def getFromId(id):
    id_club = session.query(Club).filter(Club.id == id).first()
    if (id_club == None):
        print("There is no book with this id")
    else:
        return id_club
'''
:return: the name of the club
'''
def getFromName(name):
    name_club = session.query(Club).filter(Club.name == name).first()
    if (name_club == None):
        print("There is no book with this id")
    else:
        return name_club

def getFromDirector(director):
    director_clubs = session.query(Club).filter(Club.director_id == director).first()
    if (director_clubs == None):
        print("There is no book with this id")
    else:
        return director_clubs

'''
:param name: a string that will be the new name for the club
:return:
'''
def setName(self, name):
    pass

'''
:return: the user who is the director of the club
'''


'''
:param user: the user who will be the new director of the club
:return:
'''
def setDirector(self, user):
    pass

'''
:return: the user who is currently the monthly host
'''
def getMonthlyHost(self):
    pass

'''
:param user: the user who will be the new monthly host for the club
:return:
'''
def setMonthlyHost(self, user):
    pass

'''
:return: the list of all members in the club
'''
def getMembers(self):
    pass

'''
:param name: the name of the user 
:return: the member object associated with the input name
'''
def getMember(self, name):
    pass

'''
:param user: a user object that will be added to the club memberList
:return:
'''
def addMember(self, user):
    pass

'''
:return: a list of all books the club has read in the past
'''
def get_books(self):
    pass

'''
:param title: the title of a book that is being searched for in the club's books list
:return: the book object that has the input title
'''
def get_book(self, title):
    pass

'''
:param book: a book object that will be added to the books list
:return:
'''
def addBook(self, book):
    pass

'''
:param address: a string that is the address for the club meeting location
:return:
'''
def setMeetingLocation(self, address):
    pass

'''
:return: the current meeting location for the club
'''
def getMeetingLocation(self):
    pass