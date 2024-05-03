import unittest
from sqlalchemy import text
from master.crud import *
from master.models import Club
from master.database import SessionLocal, engine, Base

class TestClubCRUD(unittest.TestCase):
    def setUp(self):
        # Set up a clean database for each test
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        # Clean up after each test
        session = SessionLocal()
        session.execute(text("DELETE FROM clubs"))
        session.commit()
        session.close()

    def test_add_club(self):
        # Test adding a club to the database
        new_club = Club(name="Test Club")
        session = SessionLocal()
        set_club(new_club, session)

        # Retrieve the club from the database and verify its attributes
        retrieved_club = session.query(Club).filter(Club.name == "Test Club").first()
        self.assertIsNotNone(retrieved_club)
        self.assertEqual(retrieved_club.name, "Test Club")

    def test_get_club_by_name(self):
        # Test retrieving a club by name
        # Add a club to the database
        new_club = Club(name="Test Club")
        session = SessionLocal()
        set_club(new_club, session)

        # Retrieve the club by name and verify its attributes
        retrieved_club = get_club_from_name("Test Club", session)
        self.assertIsNotNone(retrieved_club)
        self.assertEqual(retrieved_club.name, "Test Club")

if __name__ == '__main__':
    unittest.main()
