from datetime import date
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import master.models
from master.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
master.models.Base.metadata.create_all(bind=engine)


class UserBase(BaseModel):
    id: int
    name: str
    password: str
    isMonthlyHost: bool

    class BookBase(BaseModel):
        id: int
        title: str
        author: str
        rate: int
        release: date

    # class ClubBase(BaseModel):
    #     id: int
    #     name: str
    #     director: User
    #     monthly_host: User
    #     members: List[User]
    #     books: List[Book]
    #     meeting_location: str


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


@app.get("users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(master.models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
