from fastapi import APIRouter
from controllers import user_controller


router = APIRouter()

@router.get("/")
def get_all_users():
    return user_controller.get_all_users()

@router.post("/")
def create_user(user: user_controller.UserCreate):
    user = user_controller.UserCreate(
        username=user.username,
        email=user.email,
        password=user.password
    )

    return user_controller.create_user(user)
