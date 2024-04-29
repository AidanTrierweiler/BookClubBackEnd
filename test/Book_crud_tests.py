import unittest
from sqlalchemy import text  # Import the text function
from master.crud import set_book, get_book_from_title, get_book_from_id, get_author
from master.models import Book
from master.database import SessionLocal, engine, Base

class TestBookCRUD(unittest.TestCase):
    def setUp(self):
        # Set up a clean database for each test
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        # Clean up after each test
        session = SessionLocal()
        session.execute(text("DELETE FROM books"))  # Use text function to declare SQL expression
        session.commit()  # Commit the transaction
        session.close()

    def test_add_book(self):
        # Test adding a book to the database
        new_book = Book(title="Test Title", author="Test Author", rate=4)
        session = SessionLocal()  # Create a session object
        set_book(new_book, session)  # Pass the session object to the set_book function

        # Retrieve the book from the database and verify its attributes
        retrieved_book = session.query(Book).filter(Book.title == "Test Title").first()
        self.assertIsNotNone(retrieved_book)
        self.assertEqual(retrieved_book.author, "Test Author")
        self.assertEqual(retrieved_book.rate, 4)

    def test_get_book_by_title(self):
        # Test retrieving a book by title
        # Add a book to the database
        new_book = Book(title="Test Title", author="Test Author", rate=4)
        session = SessionLocal()  # Create a session object
        set_book(new_book, session)  # Pass the session object to the set_book function

        # Retrieve the book by title and verify its attributes
        retrieved_book = get_book_from_title("Test Title",
                                             session)  # Pass the session object to the get_book_from_title function
        self.assertIsNotNone(retrieved_book)
        self.assertEqual(retrieved_book.author, "Test Author")
        self.assertEqual(retrieved_book.rate, 4)

    def test_get_book_by_id(self):
        # Test retrieving a book by its ID
        # Add a book to the database
        new_book = Book(title="Test Title", author="Test Author", rate=4)
        session = SessionLocal()  # Create a session object
        set_book(new_book, session)  # Pass the session object to the set_book function

        # Retrieve the book by its ID and verify its attributes
        retrieved_book = get_book_from_id(new_book.id,
                                          session)  # Pass the session object to the get_book_from_id function
        self.assertIsNotNone(retrieved_book)
        self.assertEqual(retrieved_book.title, "Test Title")
        self.assertEqual(retrieved_book.author, "Test Author")
        self.assertEqual(retrieved_book.rate, 4)

    def test_get_author(self):
        # Test retrieving books by author
        new_book = Book(title="Test Title", author="Test Author", rate=4)
        session = SessionLocal()  # Create a session object
        set_book(new_book, session)  # Pass the session object to the set_book function

        # Retrieve books by author and verify the results
        books_by_author = get_author("Test Author", session)
        self.assertIsNotNone(books_by_author)
        self.assertEqual(len(books_by_author), 1)
        self.assertEqual(books_by_author[0].title, "Test Title")
        self.assertEqual(books_by_author[0].rate, 4)

if __name__ == '__main__':
    unittest.main()
