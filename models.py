from datetime import datetime
import strawberry

@strawberry.type
class Event:
    title: str
    description: str
    datetime: datetime
