'''
    Class outline: Matt
'''

import ReviewClass
import BookClass
import User

test_user_2 = User()
test_book_1 = BookClass("Enter params once book constructor has been implemented")
test_book_2 = BookClass("Enter params once book constructor has been implemented")

test_review_0 = ReviewClass()
''' make this a real book once books can be created '''
test_review_0.set_book("Book Title Here")

test_review_1 = ReviewClass()

test_book_1.add_review(test_review_0, test_user_2)
test_book_1.add_review(test_review_1, test_user_2)

'''Returns the ID of the review'''
def get_id_test():
    ''' to write this I need to know how we will be assigning IDs to reviews, so I know what to assert
        the review id is == to'''
    pass

'''Returns the user who wrote the review'''
def get_user_test():
    result = test_review_0.get_user()

    assert result == test_user_2

'''Sets the user for a new review'''
def set_user_test():
    pass

'''Returns the book that the review is about'''
def get_book_test():
    result = test_review_0.get_book()

    assert result == test_book_1

'''Ties the review to a book'''
def set_book_test():
    test_review_0.set_book("Test Book Two")

    assert test_review_0.get_book() == test_book_2

'''Returns the date the review was written'''
def get_date_test():
    result = test_review_0.get_date()

    assert result == "PlaceHolder Date"

'''Sets the date for a new review'''
def set_date_test():
    test_review_0.set_date("04-19-24")

    assert test_review_0.get_date() == "04-19-24"

'''Gets the rating from a review'''
def get_rate_test():
    pass

'''Allows the user to rate a book with the review'''
def set_rate_test():
    pass

'''Returns the contents of the review'''
def get_content_test():
    result = test_review_0.get_content()

    assert result == "Placeholder content, content content content content content content"

'''Allows teh user to write a review paragraph'''
def set_content_test():
    test_review_0.set_content("This is a review, I love writing reviews. This was a good book.")

    assert test_review_0.get_content == "This is a review, I love writing reviews. This was a good book."