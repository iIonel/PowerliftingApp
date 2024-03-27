from model.models import Exercise
from repository.exercise_repo import ExerciseRepository


class ExerciseController:
    """
    Controller class for exercises
    """

    def __init__(self, database):
        self.repo = ExerciseRepository(database)

    def add_exercise(self, exercise: Exercise):
        return self.repo.add_exercise(exercise)

    def delete_exercise(self, exercise_id: int):
        return self.repo.delete_exercise(exercise_id)

    def update_exercise(self, exercise_id: int, new_exercise: Exercise):
        return self.repo.update_exercise(exercise_id, new_exercise)

    def get_exercises(self):
        return self.repo.get_exercises()
