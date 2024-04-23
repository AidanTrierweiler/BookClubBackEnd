from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str
    password: str
    isMonthlyHost: Optional[bool]


class Book(BaseModel):
    id: int
    title: str
    author: str
    rate: int
    release: str
    owner_id: int


class Club(BaseModel):
    id: int
    name: str
    director_id: int
    monthly_host_id: Optional[int]
    meeting_location: str
    members: List[User]


class Review(BaseModel):
    id: Optional[int]
    date: str
    rate: int
    content: str
    user_id: Optional[int]
    book_id: Optional[int]

    class Config:
        orm_mode = True
