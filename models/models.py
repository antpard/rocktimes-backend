import strawberry
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship


class UserModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    name: Optional[str] = Field(default=None)
    active: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now)
    #events: List['EventModel'] = Relationship(back_populates="user")

@strawberry.experimental.pydantic.type(
    UserModel,
    fields=["email", "name", "created_at"]
)
class User:
    pass


class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: str
    url: str
    image: str
    starts_at: datetime = Field(default=datetime.now)
    ends_at: datetime = Field(default=datetime.now)
    #user_id: int = Field(default=None, foreign_key="user.id")
    #user: 'User' = Relationship(back_populates="events")

@strawberry.experimental.pydantic.type(
    EventModel,
    fields=["title", "description", "url", "image", "starts_at", "ends_at"]
)
class Event:
    pass

