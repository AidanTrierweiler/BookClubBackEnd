import unittest
from sqlalchemy import text
from master.crud import setUser, getUserFromEmail, getUserFromId
from master.models import User
from master.database import SessionLocal, engine, Base

class TestUserCRUD(unittest.TestCase):
    def setUp(self):
        # Set up a clean database for each test
        Base.metadata.create_all(bind=engine)
        self.session = SessionLocal()

    def tearDown(self):
        # Clean up after each test
        self.session.execute(text("DELETE FROM users"))
        self.session.commit()
        self.session.close()

    def test_add_user(self):
        # Test adding a user to the database
        new_user = User(name="Test User", email="test@example.com", password="password", isMonthlyHost=False)
        setUser(new_user, self.session)

        # Retrieve the user from the database and verify its attributes
        retrieved_user = getUserFromEmail("test@example.com", self.session)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.name, "Test User")
        self.assertEqual(retrieved_user.password, "password")
        self.assertEqual(retrieved_user.isMonthlyHost, False)

    def test_get_user_by_email(self):
        # Test retrieving a user by email
        new_user = User(name="Test User", email="test@example.com", password="password", isMonthlyHost=False)
        setUser(new_user, self.session)

        # Retrieve the user by email and verify its attributes
        retrieved_user = getUserFromEmail("test@example.com", self.session)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.name, "Test User")
        self.assertEqual(retrieved_user.password, "password")
        self.assertEqual(retrieved_user.isMonthlyHost, False)

    def test_get_user_by_id(self):
        # Test retrieving a user by ID
        new_user = User(name="Test User", email="test@example.com", password="password", isMonthlyHost=False)
        setUser(new_user, self.session)

        # Retrieve the user by ID and verify its attributes
        retrieved_user = getUserFromId(new_user.id, self.session)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.name, "Test User")
        self.assertEqual(retrieved_user.password, "password")
        self.assertEqual(retrieved_user.isMonthlyHost, False)

if __name__ == '__main__':
    unittest.main()
