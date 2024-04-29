from datetime import date
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import master.models
from master.database import engine, SessionLocal
from sqlalchemy.orm import Session
from master.database import session
from master.crud import *
from master.schema import *
import master.crud

app = FastAPI()
master.models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = master.models.User(**user.dict())
    db.add(db_user)
    db.commit()

# Route to add a new book
@app.post("/books/", status_code=status.HTTP_201_CREATED)
def create_book(book: BookBase, db: db_dependency):
    db_book = master.models.Book(**book.dict())
    db.add(db_book)
    db.commit()

# Route to get a book by its title
@app.get("/books/{title}")
def read_book(title: str, db: db_dependency):
    return get_book_from_title(title, db)


@app.get("/books/id/{book_id}")
def read_book_by_id(book_id: int, db: db_dependency):
    return get_book_from_id(book_id, db)


@app.get("/books/author/{author_name}")
def read_books_by_author(author_name: str, db: db_dependency):
    return get_author(author_name, db)


@app.post("/clubs/", status_code=status.HTTP_201_CREATED)
async def create_user(club: ClubBase, db: db_dependency):
    db_club = master.models.Club(**club.dict())
    db.add(db_club)
    db.commit()


@app.get("/clubs/id/{club_id}")
def read_club(club_id: int, db: db_dependency):
    return getFromId(club_id)


@app.get("/clubs/name/{club_name}")
def read_club_by_name(club_name: str, db: db_dependency):
    return get_club_from_name(club_name, db)


@app.get("/users/id/{user_id}")
def read_user(user_id: int, db: db_dependency):
    return getUserFromId(user_id, db)


@app.get("/users/email/{email}")
def read_user_by_email(email: str, db: db_dependency):
    return getUserFromEmail(email, db)
