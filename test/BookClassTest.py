'''
    Class Outline: Matt
'''

import BookClass
import ReviewClass
import User

test_book_3 = BookClass()
test_user_3 = User()

'''When creating test_review_2 make sure its made by test_user_3'''
test_review_2 = ReviewClass()
test_review_3 = ReviewClass()
test_review_4 = ReviewClass()

test_book_3.add_review(test_review_2)
test_book_3.add_review(test_review_3)

'''Get Book ID'''
def get_id_test():
    result = test_book_3.get_id()

    '''update once real book object and id have been made'''
    assert result == 3


'''Returns book title'''
def get_title_test():
    result = test_book_3.get_title()

    '''update with real object'''
    assert result == "placeholder title"


'''Sets the book title if it doesnt have one'''
def set_title_test():
    test_book_3.set_title("Of Mice and Men")

    assert test_book_3.get_title() == "Of Mice and Men"


'''Returns the books author'''
def get_author_test():
    result = test_book_3.get_author()

    '''Once test JSON has been made replace with actual author of test book'''
    assert result == "Placeholder author"


'''Sets the Books author if it doesnt have one'''
def set_author_test():
    test_book_3.set_author("John Steinbeck")

    assert test_book_3.get_author() == "John Steinbeck"


'''Returns the books release date'''
def get_release_test():
    result = test_book_3.get_release_date()

    assert result == "04-24-1980"


'''Returns a list of all the books reviews'''
def get_reviews_test():
    len_result = len(test_book_3.get_reviews())
    review_list = test_book_3.get_review()
    second_review = review_list[1]

    assert len_result == 2
    ''' replace id once reviews are made and given ids'''
    assert second_review.get_id == 2


'''Reuturns the review of a book from a certain user'''
def get_review_test():
    result = test_book_3.get_review(test_user_3)

    '''When creating test_review_2 make sure its made by test_user_3'''
    assert result == test_review_2


'''Adds a review to a book'''
def add_review_test():
    test_book_3.add_review(test_review_4)

    assert len(test_book_3.get_reviews()) == 3


'''???'''
def update_rate_test():
    pass
