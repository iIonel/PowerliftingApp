from repository.user_repo import UserRepository


class UserController:
    """
    Controller class for user
    """

    def __init__(self, database):
        self.repo = UserRepository(database)

    def get_users(self):
        return self.repo.get_users()

    def get_user(self, user_id):
        return self.repo.get_user(user_id)

    def get_user_by_email(self, email):
        return self.repo.get_user_by_email(email)

    def get_users_by_status(self, status):
        return self.repo.get_users_by_status(status)

    def add_user(self, user):
        return self.repo.add_user(user)

    def delete_user(self, user_id):
        return self.repo.delete_user(user_id)

    def update_user(self, user_id, user):
        return self.repo.update_user(user_id, user)

    def get_personal_records(self, user_id):
        return self.repo.get_personal_records(user_id)

    def add_personal_record(self, personal_records):
        return self.repo.add_personal_record(personal_records)