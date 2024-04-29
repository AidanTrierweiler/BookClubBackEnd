import unittest
from sqlalchemy import text  # Import the text function
from master.crud import *
from master.models import Book, Club
from master.database import SessionLocal, engine, Base

class TestClubCRUD(unittest.TestCase):
    def setUp(self):
        # Set up a clean database for each test
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        # Clean up after each test
        session = SessionLocal()
        session.execute(text("DELETE FROM clubs"))  # Use text function to declare SQL expression
        session.commit()  # Commit the transaction
        session.close()

    def test_add_club(self):
        # Test adding a book to the database
        new_club = Club(name = "Test Club")
        session = SessionLocal()  # Create a session object
        set_club(new_club, session)  # Pass the session object to the set_book function

        # Retrieve the book from the database and verify its attributes
        retrieved_club = session.query(Club).filter(Club.name == "Test Club").first()
        self.assertIsNotNone(retrieved_club)
        self.assertEqual(retrieved_club.name, "Test Club")

    def test_get_club_by_name(self):
        # Test retrieving a book by title
        # Add a book to the database
        new_club = Club(title="Test Club")
        session = SessionLocal()  # Create a session object
        set_book(new_club, session)  # Pass the session object to the set_book function

        # Retrieve the book by title and verify its attributes
        retrieved_club = get_club_from_name("Test Club",
                                             session)  # Pass the session object to the get_book_from_title function
        self.assertIsNotNone(retrieved_club)
        self.assertEqual(retrieved_club.name, "Test Club")

if __name__ == '__main__':
    unittest.main()
