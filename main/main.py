from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from UserSoftware import User
import models


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class UserBase(BaseModel):
    id: int
    name: str
    password: str
    isMonthlyHost: bool


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
