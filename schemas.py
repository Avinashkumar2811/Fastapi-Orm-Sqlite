
#3_schemas.py — API input/output ka format banana (Pydantic)
"""API me kya data aayega aur kya data jayega, woh hum schemas me define karte hain.

👉 In short:
“API me kaunsa data aana aur chale jaana chahiye, woh fix kiya.”"""

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
