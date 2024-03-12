from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from model.models import User, PersonalRecord, Exercise
from util.connection import connect_to_db


class Database:
    """
    Database class
    """

    def __init__(self):
        self.connection = connect_to_db
        self.engine = create_engine('postgresql://postgres:1234@localhost:5433/postgres')
        self.Session = sessionmaker(bind=self.engine)

    def get_users(self):
        try:
            session = self.Session()
            users = session.query(User).all()
            session.close()
            return users
        except SQLAlchemyError as e:
            print('Error users: ', e)

    def get_user(self, user_id: int):
        try:
            session = self.Session()
            user = session.query(User).filter_by(user_id=user_id).first()
            session.close()
            return user
        except SQLAlchemyError as e:
            print('Error user id: ', e)

    def get_user_by_email(self, email):
        try:
            session = self.Session()
            user = session.query(User).filter_by(email=email).first()
            session.close()
            return user
        except SQLAlchemyError as e:
            print('Error user email: ', e)

    def get_users_by_status(self, status: bool):
        try:
            session = self.Session()
            users = session.query(User).filter_by(natty=status).all()
            session.close()
            return users
        except SQLAlchemyError as e:
            print('Error user status: ', e)

    def get_personal_records(self, user_id: int):
        try:
            session = self.Session()
            personal_records = session.query(PersonalRecord).filter_by(user_id=user_id).first()
            session.close()
            return personal_records
        except SQLAlchemyError as e:
            print('Error personal record: ', e)

    def get_exercises(self):
        try:
            session = self.Session()
            exercises = session.query(Exercise).all()
            session.close()
            return exercises
        except SQLAlchemyError as e:
            print('Error exercises: ', e)

    def add_user(self, user: User):
        try:
            session = self.Session()
            session.add(user)
            session.commit()
        except SQLAlchemyError as e:
            print('Error adding user: ', e)

    def delete_user(self, user_id: int):
        try:
            session = self.Session()
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
                session.close()
            else:
                print(f"{user_id} does not exist")
        except SQLAlchemyError as e:
            print('Error while deleting user: ', e)

    def update_user(self, user_id:int, new_user: User):
        try:
            session = self.Session()
            user = session.query(User).filter_by(user_id=user_id).first()
            if user:
                user.first_name = new_user.first_name
                user.last_name = new_user.last_name
                user.email = new_user.email
                user.age = new_user.age
                user.natty = new_user.natty
                user.weight = new_user.weight
                user.height = new_user.height
                session.commit()
                session.close()
            else:
                print(f"{user_id} does not exist")
        except SQLAlchemyError as e:
            print('Error while updating user: ', e)

    def add_personal_record(self, personal_record: PersonalRecord):
        try:
            session = self.Session()
            session.add(personal_record)
            session.commit()
        except SQLAlchemyError as e:
            print('Error adding personal record: ', e)

    def add_exercise(self, exercise: Exercise):
        try:
            session = self.Session()
            session.add(exercise)
            session.commit()
        except SQLAlchemyError as e:
            print('Error adding exercise: ', e)

    def delete_exercise(self, exercise_id: int):
        try:
            session = self.Session()
            exercise = session.query(Exercise).filter_by(exercise_id=exercise_id).first()
            if exercise:
                session.delete(exercise)
                session.commit()
                session.close()
            else:
                print(f"{exercise_id} does not exist")
        except SQLAlchemyError as e:
            print('Error while deleting exercise: ', e)

    def update_exercise(self, exercise_id: int, new_exercise: Exercise):
        try:
            session = self.Session()
            exercise = session.query(Exercise).filter_by(exercise_id=exercise_id).first()
            if exercise:
                exercise.name = new_exercise.name
                exercise.description = new_exercise.description
                exercise.video_link = new_exercise.video_link
                session.commit()
                session.close()
            else:
                print(f"{exercise_id} does not exist")
        except SQLAlchemyError as e:
            print('Error while updating exercise: ', e)
