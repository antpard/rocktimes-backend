from typing import List
from models import Event
from datetime import datetime

def get_events() -> List[Event]:
    return [
        Event(
            title="Event 1",
            description="Description 1",
            datetime=datetime.now(),
        ),
        Event(
            title="Event 2",
            description="Description 2",
            datetime=datetime.now(),
        ),
    ]
