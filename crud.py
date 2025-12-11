
#4_Crud.py — Database pe actual operations (Create, Read, Update, Delete)
"""Yahan hum functions likhte hain jaise:
create_user
get_user
update_user
delete_user"""

#Example:
"""
def create_user(db, user):
    new = User(...)
    db.add(new)
    db.commit()"""

#In short:
#“Database me insert/update/delete ka real logic.”



from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
