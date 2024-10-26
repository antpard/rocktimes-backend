from models.user_model import User
from services.user_service import UserService
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

def get_all_users():
    return UserService.get_all_users()

def create_user(user: UserCreate):
    return UserService.create_user(user)
