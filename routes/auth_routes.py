from fastapi import APIRouter
from controllers import auth_controller


router = APIRouter()

@router.post("/")
def auth():
    return auth_controller.auth()
