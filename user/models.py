from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), unique=True)
    password = Column(String(255))

    def __init__(self, name, email, password, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = password