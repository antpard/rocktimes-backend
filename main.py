import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
import datetime
import typing


@strawberry.type
class Event:
    title: str
    description: str
    datetime: datetime.datetime


def get_events() -> typing.List[Event]:
    return [
            Event(
                title="Event 1",
                description="Description 1",
                datetime=datetime.datetime.now(),
            ),
    ]

@strawberry.type
class Query:
    events: typing.List[Event] = strawberry.field(resolver=get_events)


schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


