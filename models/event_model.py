import strawberry
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: str
    url: str
    image: str
    starts_at: datetime = Field(default=datetime.now)
    ends_at: datetime = Field(default=datetime.now)
    #user_id: int = Field(default=None, foreign_key=":wuser.id")
    #user: 'User' = Relationship(back_populates="events")

@strawberry.experimental.pydantic.type(
    EventModel,
    fields=["title", "description", "url", "image", "starts_at", "ends_at"]
)
class Event:
    pass
