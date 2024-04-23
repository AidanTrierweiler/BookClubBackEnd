# test_crud.py

from master.crud import get_book_from_title, get_book_from_id, set_book
from master.models import Book

def test_create_book(db):
    # Manually create a dummy book object
    dummy_book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "release": "2022-04-25"
    }

    # Create a new book using the CRUD function
    book = set_book(db, **dummy_book_data)

    # Assert that the returned book object matches the expected values
    assert isinstance(book, Book)
    assert book.title == dummy_book_data["title"]
    assert book.author == dummy_book_data["author"]
    assert book.release == dummy_book_data["release"]

def test_get_book_from_id(db):
    # Manually create a dummy book object
    dummy_book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "release": "2022-04-25"
    }

    # Create a new book using the CRUD function
    book = set_book(db, **dummy_book_data)

    # Retrieve the book by ID using the CRUD function
    retrieved_book = get_book_from_id(db, book.id)

    # Assert that the retrieved book matches the original book
    assert retrieved_book == book
