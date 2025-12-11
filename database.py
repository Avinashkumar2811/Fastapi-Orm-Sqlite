#1️database.py — Database se connection banana
"""Yahan hum FastAPI ko bolte hain ki database kahan hai.
SQLite/PostgreSQL/MySQL ka URL dete hain
A “Session” banaate hain → jisse hum query kar sakte hain
Base class banate hain → jisme models register hote hain
"""
#In short:
#“FastAPI ko bata diya ki database kahan hai aur kaise connect karna hai.”


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"   # MySQL/Postgres bhi use kar sakte ho

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
