from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from master.database import Base
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    password = Column(String(20))
    isMonthlyHost = Column(Boolean)  # Renamed column

    # Define relationships
    books = relationship("Book", back_populates="owner", cascade="all, delete")
    clubs = relationship("Club", secondary="club_members", back_populates="members")
    ownedClubs = relationship("Club", back_populates="director",
                              foreign_keys="[Club.director_id]")  # Specify foreign key column
    monthly_host_clubs = relationship("Club", back_populates="monthly_host",
                                      foreign_keys="[Club.monthly_host_id]")  # Specify foreign key column
    reviews = relationship("Review", back_populates="user")


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
    director = relationship("User", back_populates="ownedClubs", foreign_keys=[director_id])
    monthly_host = relationship("User", back_populates="monthly_host_clubs", foreign_keys=[monthly_host_id])
    members = relationship("User", secondary="club_members", back_populates="clubs")


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    rate = Column(Integer)
    content = Column(String(255))  # Adjusted length or change to Text if needed
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