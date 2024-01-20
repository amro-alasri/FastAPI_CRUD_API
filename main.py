from fastapi import FastAPI, HTTPException
from enum import Enum
from typing import List
from pydantic import BaseModel
from uuid import UUID, uuid4

app = FastAPI()

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    middle_name: str
    gender: Gender
    roles: List[Role]

db: List[User] = [
    User(id=uuid4(), first_name="jamila", last_name="Ahemde", middle_name="asdf", gender=Gender.female, roles=[Role.student]),
    User(id=uuid4(), first_name="Alex", last_name="Jonse", middle_name="asdf", gender=Gender.male, roles=[Role.admin, Role.user])
]

@app.get("/")
def read_root(): 
    return {"Hello": "World"}

@app.get("/api/v1/users", response_model=List[User])
async def fetch_users():
    return db

@app.get("/api/v1/users/{user_id}", response_model=User)
async def read_user(user_id: UUID):
    user = next((u for u in db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/v1/users", response_model=User)
async def create_user(user: User):
    user.id = uuid4()
    db.append(user)
    return user

@app.put("/api/v1/users/{user_id}", response_model=User)
async def update_user(user_id: UUID, updated_user: User):
    index = next((i for i, u in enumerate(db) if u.id == user_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="User not found")
    db[index] = updated_user
    return updated_user

@app.delete("/api/v1/users/{user_id}", response_model=User)
async def delete_user(user_id: UUID):
    user = next((u for u in db if u.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.remove(user)
    return user
