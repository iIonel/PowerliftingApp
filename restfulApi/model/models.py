from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    age = Column(Integer)
    natty = Column(Boolean)
    weight = Column(Float)
    height = Column(Float)
    personal_records = relationship("PersonalRecord", back_populates="user")

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'age': self.age,
            'natty': self.natty,
            'weight': self.weight,
            'height': self.height
        }


class PersonalRecord(Base):
    __tablename__ = 'personalrecords'

    pr_id = Column(Integer, primary_key=True)
    squat = Column(Float)
    bench = Column(Float)
    deadlift = Column(Float)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("User")

    def to_dict(self):
        return {
            'id': self.pr_id,
            'squat': self.squat,
            'bench': self.bench,
            'deadlift': self.deadlift
        }


class Program(Base):
    __tablename__ = 'programs'

    program_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)

    user_id = Column(Integer, ForeignKey('users.user_id'))
    user = relationship("User")


class Workout(Base):
    __tablename__ = 'workouts'

    workout_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)
    program_id = Column(Integer, ForeignKey('programs.program_id'))
    week_number = Column(Integer)
    day_number = Column(Integer)


class Exercise(Base):
    __tablename__ = 'exercises'

    exercise_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String)
    video_link = Column(String(200))

    def to_dict(self):
        return {
            'exercise_id': self.exercise_id,
            'name': self.name,
            'description': self.description,
            'video_link': self.video_link
        }


class WorkoutItem(Base):
    __tablename__ = 'workout_items'

    item_id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('exercises.exercise_id'))
    workout_id = Column(Integer, ForeignKey('workouts.workout_id'))


class Set(Base):
    __tablename__ = 'sets'

    set_id = Column(Integer, primary_key=True)
    rep_count = Column(Integer)
    workout_item_id = Column(Integer, ForeignKey('workout_items.item_id'))
    weight = Column(Float)
