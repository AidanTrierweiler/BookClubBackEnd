from sqlalchemy import Column, Integer, String, Boolean
from UserSoftware import Base


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    isMonthlyHost = Column(Boolean)
