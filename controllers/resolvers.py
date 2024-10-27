import strawberry
from typing import List
from models.event_model import Event
from models.user_model import User
from datetime import datetime


@strawberry.type
class EventMutation:
    @strawberry.mutation
    def get_events() -> List[Event]:
        return [
            Event(
                title="Event 1",
                description="Description 1",
                url="http://localhost/",
                image="event1.png",
                starts_at=datetime.now(),
                ends_at=datetime.now(),
            ),
            Event(
                title="Event 2",
                description="Description 2",
                url="http://localhost/",
                image="event2.png",
                starts_at=datetime.now(),
                ends_at=datetime.now(),
            ),
        ]


def get_user() -> User:
    return User(
        email="user1@example.com",
        name="User 1",
        created_at=datetime.now(),
    )