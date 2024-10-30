from fastapi import APIRouter
from controllers import event_controller


router = APIRouter()

@router.get("/")
def get_all_events():
    return event_controller.get_all_events()

@router.post("/")
def create_post(event: event_controller.EventCreate):
    return event_controller.create_event(event)
