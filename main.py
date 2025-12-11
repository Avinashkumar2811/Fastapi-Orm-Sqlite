#main.py — FastAPI endpoints + sabko connect karna
"""Yahan:
API endpoints create karte hain
database session ko inject karte hain
CRUD functions call karte hain
"""
#Example:
"""@app.post("/users/")
def create_user_api(user: UserCreate, db=Depends(get_db)):
    return create_user(db, user)
"""
#In short:
#User request aata hai → DB session milta hai → CRUD functions run hote hain → response milta hai.



from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from models import Base
from crud import create_user, get_user
from schemas import UserCreate, UserResponse

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency → DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserResponse) 
def create_new_user(user: UserCreate, db=Depends(get_db)): #user add kro post se
    return create_user(db, user)

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db=Depends(get_db)): #user dekh lo get se
    user = get_user(db, user_id)
    return user
