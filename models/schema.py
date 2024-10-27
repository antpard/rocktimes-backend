import strawberry
from typing import List
from models import Event, User
from resolvers import get_events, get_user

@strawberry.type
class Query:
    events: List[Event] = strawberry.field(resolver=get_events)
    user: User = strawberry.field(resolver=get_user)


schema = strawberry.Schema(Query)
