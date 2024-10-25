import typing
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
import datetime


@strawberry.type
class Event:
    title: str
    description: str
    datetime: datetime.datetime

def get_events():
    return [
        Event(
            title="Event 1",
            description="Description 1",
            datetime=datetime.datetime.now(),
        ),
        Event(
            title="Event 2",
            description="Description 2",
            datetime=datetime.datetime.now(),
        ),
    ]

@strawberry.type
class Query:
    events: typing.List[Event] = strawberry.field(resolver=get_events)


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
