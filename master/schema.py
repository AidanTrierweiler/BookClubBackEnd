from typing import List, Optional
from pydantic import BaseModel, Field, PositiveInt

class ReviewBase(BaseModel):
    date: Optional[str]
    rate: int = Field(..., ge=1, le=5)
    content: str = Field(..., max_length=255)

class ReviewCreate(ReviewBase):
    user_id: PositiveInt
    book_id: PositiveInt

class Review(ReviewBase):
    id: int
    user_id: int
    book_id: int

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    title: str = Field(..., max_length=100)
    author: str = Field(..., max_length=100)
    rate: int = Field(..., ge=1, le=5)
    release: str

class BookCreate(BookBase):
    owner_id: PositiveInt

class Book(BookBase):
    id: int
    owner_id: int
    reviews: List[Review] = []

    class Config:
        from_attributes = True

class ClubBase(BaseModel):
    name: str = Field(..., max_length=100)
    director_id: PositiveInt
    monthly_host_id: PositiveInt
    meeting_location: str = Field(..., max_length=100)

class ClubCreate(ClubBase):
    pass

class Club(ClubBase):
    id: int
    director_id: int
    monthly_host_id: int
    members: List[int] = []

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    name: str = Field(..., max_length=20)
    password: str = Field(..., max_length=20)
    isMonthlyHost: bool

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    books: List[Book] = []
    clubs: List[Club] = []
    ownedClubs: List[Club] = []
    reviews: List[Review] = []

    class Config:
        from_attributes = True
