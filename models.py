#2_models_hum Python classes banate hain:
#Iska matlab:
"""Database me ek users table banega
Columns honge → id, name, email
ORM ke through ye Python object ban jaata hai"""

#In short:
#“Table aur columns define kiye.”

from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
