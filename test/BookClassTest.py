'''
    Class Outline: Matt
'''

from master.BookClass import Book
from master.ReviewClass import Review
from master.User import User

test_book_3 = Book('''Make with the first book in the bookTestData.json''')
test_user_3 = User("Test User", "Password")
test_user_4 = User("Test User", "Password")
test_user_5 = User("Test User", "Password")

test_review_2 = Review(test_user_3, test_book_3, "00-00-0000", 8, "This is test review content.")
test_review_3 = Review(test_user_4, test_book_3, "00-00-0001", 7, "This is test review content number 2.")
test_review_4 = Review(test_user_5, test_book_3, "00-00-0002", 6, "This is test review content number 3.")

test_book_3.add_review(test_review_2)
test_book_3.add_review(test_review_3)

'''Get Book ID'''
def get_id_test():
    result = test_book_3.get_id()

    assert result == "k1nCE5hSoTkC"


'''Returns book title'''
def get_title_test():
    result = test_book_3.get_title()

    assert result == "The Language of Flowers"


'''Sets the book title if it doesnt have one'''
def set_title_test():
    test_book_3.set_title("Of Mice and Men")

    assert test_book_3.get_title() == "Of Mice and Men"


'''Returns the books author'''
def get_author_test():
    result = test_book_3.get_author()

    '''What do we do if there is more than one author of the book?'''
    assert result == "Vanessa Diffenbaugh"


'''Sets the Books author if it doesnt have one'''
def set_author_test():
    test_book_3.set_author("John Steinbeck")

    assert test_book_3.get_author() == "John Steinbeck"


'''Returns the books release date'''
def get_release_test():
    result = test_book_3.get_release()

    assert result == "2011"


'''Returns a list of all the books reviews'''
def get_reviews_test():
    len_result = len(test_book_3.get_reviews())
    review_list = test_book_3.get_review()
    second_review = review_list[1]

    assert len_result == 2
    ''' replace id once reviews are made and given ids'''
    assert second_review.get_id == 2


'''Returns the review of a book from a certain user'''
def get_review_test():
    result = test_book_3.get_review(test_user_3)

    assert result == test_review_2


'''Adds a review to a book'''
def add_review_test():
    test_book_3.add_review(test_review_4)
    review_list = test_book_3.get_reviews()

    assert len(test_book_3.get_reviews()) == 3
    assert review_list[2] == test_review_4


'''???'''
def update_rate_test():
    pass
