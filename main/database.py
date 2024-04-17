from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from UserSoftware import Base as UserBase


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:DougProject3!@localhost:3306/bookclubdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

UserBase.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"Base = declarative_base()"
