# from typing import re

import re
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from master.database import Base
from sqlalchemy.orm import relationship, declarative_base, validates


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    email = Column(String)
    password = Column(String(20))
    isMonthlyHost = Column(Boolean)

    # Define relationships
    books = relationship("Book", back_populates="owner", cascade="all, delete")
    clubs = relationship("Club", secondary="club_members", back_populates="members")
    ownedClubs = relationship("Club", primaryjoin="User.id == Club.director_id", back_populates="director")
    reviews = relationship("Review", back_populates="user")

    @validates('email')
    def validate_email(self, key, email):
        # Regular expression pattern for validating email addresses
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        if not email_pattern.match(email):
            raise ValueError("Invalid email address format")

        return email


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    author = Column(String(100))
    rate = Column(Integer)
    release = Column(Date)

    # Define relationships
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="books")
    reviews = relationship("Review", back_populates="book")


class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    director_id = Column(Integer, ForeignKey('users.id'))
    monthly_host_id = Column(Integer, ForeignKey('users.id'))
    meeting_location = Column(String(100))

    # Define relationships
    director = relationship("User", primaryjoin="Club.director_id == User.id", back_populates="ownedClubs")
    #monthly_host = relationship("User", foreign_keys=[monthly_host_id])
    members = relationship("User", secondary="club_members", back_populates="clubs")


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    rate = Column(Integer)
    content = Column(String(20))
    # Define relationships
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="reviews")
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="reviews")


# Define association table for many-to-many relationship between clubs and members
club_members = Table('club_members', Base.metadata,
                     Column('club_id', Integer, ForeignKey('clubs.id')),
                     Column('user_id', Integer, ForeignKey('users.id'))
                     )
