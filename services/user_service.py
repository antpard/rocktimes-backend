from models.user_model import User

class UserService:
    @staticmethod
    def get_all_users():
        # Logic to get all users
        return []

    @staticmethod
    def create_user(user : User):
        # Logic to create a new user
        return {"message": "User created successfully"}
