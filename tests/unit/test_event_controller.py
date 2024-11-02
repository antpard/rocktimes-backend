from models.event_model import Event, EventModel

import unittest

class TestEvents(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)

    # Test event model class
    def test_event_model(self):
        event = EventModel(
            title="Test Event",
            description="This is a test event",
            url="https://test.com",
            image="https://test.com/image.jpg",
            starts_at="2021-09-01T00:00:00",
            ends_at="2021-09-01T00:00:00"
        )
        self.assertEqual(event.title, "Test Event")
        self.assertEqual(event.description, "This is a test event")
        self.assertEqual(event.url, "https://test.com")
        self.assertEqual(event.image, "https://test.com/image.jpg")
        self.assertEqual(event.starts_at, "2021-09-01T00:00:00")
        self.assertEqual(event.ends_at, "2021-09-01T00:00:00")

if __name__ == "__main__":
    unittest.main()
