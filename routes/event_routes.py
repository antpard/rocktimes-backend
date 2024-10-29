from fastapi import APIRouter
from controllers import auth_controller


router = APIRouter()

@router.get("/")
def get_all_users():
    return user_controller.get_all_users()

@router.post("/")
def create_user(user: user_controller.UserCreate):
    return user_controller.create_user(user)
