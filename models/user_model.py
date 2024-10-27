import strawberry
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class User(SQLModel, table=True):
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
