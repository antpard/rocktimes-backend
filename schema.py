import strawberry
from typing import List
from models import Event
from resolvers import get_events

@strawberry.type
class Query:
    events: List[Event] = strawberry.field(resolver=get_events)


schema = strawberry.Schema(Query)
