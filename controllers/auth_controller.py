import strawberry
from models import User

@strawberry.type
class AuthMutation:
    @strawberry.mutation
    def auth(username: str, password: str) -> Session:
        return auth_controller.auth(username, password)
