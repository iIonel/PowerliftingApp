import string

from model.models import User, PersonalRecord


class UserRepository:
    """
    This class is responsible for creating and updating users
    """

    def __init__(self, database):
        self.database = database

    def get_users(self):
        return self.database.get_users()

    def get_user(self, user_id: int):
        return self.database.get_user(user_id)

    def get_user_by_email(self, email: string):
        return self.database.get_user_by_email(email)

    def get_users_by_status(self, status: bool):
        return self.database.get_users_by_status(status)

    def add_user(self, user: User):
        return self.database.add_user(user)

    def delete_user(self, user_id: int):
        return self.database.delete_user(user_id)

    def update_user(self, user_id:int, user: User):
        return self.database.update_user(user_id, user)

    def get_personal_records(self, user_id:int):
        return self.database.get_personal_records(user_id)

    def add_personal_record(self, personal_record: PersonalRecord):
        return self.database.add_personal_record(personal_record)


