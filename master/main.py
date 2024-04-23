from datetime import date
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import master.models
from master.database import engine, SessionLocal
from sqlalchemy.orm import Session
from database import session
from crud import *

app = FastAPI()
master.models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



db_dependency = Annotated[Session, Depends(get_db)]

new_book = Book(title="Test Book", author="Matt")
#set_book(new_book)

#Query all books
#all_books = session.query(Book).all()

#get_book_from_title("Test")
print(get_book_from_title("Test Book"))

print()

# Print the title, author, and rating of each book
#for book in all_books:
    #print(f"Title: {book.title}, Author: {book.author}")

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = master.models.User(**user.dict())
    db.add(db_user)
    db.commit()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
