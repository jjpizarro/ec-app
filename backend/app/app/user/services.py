from typing import List, Optional

from sqlalchemy.orm import Session
from . import models
from . import schema
from app.core import hashing

async def new_user_register(user_in: schema.UserCreate, db_session: Session) -> models.User:
    new_user = models.User(name=user_in.name, email=user_in.email, password=user_in.password)
    #new_user = models.User(**user_in.dict())
    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)
    return new_user

async def all_users(db_session: Session) -> List[models.User]:
    users = db_session.query(models.User).all()
    return users

async def get_user_by_id(user_id: int, db_session: Session) -> Optional[models.User]:
    user_info = db_session.query(models.User).get(user_id)

    return user_info

async def delete_user_by_id(user_id: int, db_session: Session):
    db_session.query(models.User).filter(models.User.id == user_id).delete()
    db_session.commit()

def authenticate(*, email:str, password:str, db: Session) -> Optional[models.User]:
    user = db.query(models.User).filter(models.User.email == email).first()

    if not user:
        return None

    if not hashing.verify_password(password, user.password):
        return None

    return user
