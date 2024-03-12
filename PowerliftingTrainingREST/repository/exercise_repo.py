from model.models import Exercise


class ExerciseRepository:
    """
    This class is responsible for creating and updating an exercice
    """
    def __init__(self, database):
        self.database = database

    def get_exercises(self):
        return self.database.get_exercises()

    def add_exercise(self, exercise: Exercise):
        return self.database.add_exercise(exercise)

    def delete_exercise(self, exercise_id: int):
        return self.database.delete_exercise(exercise_id)

    def update_exercise(self, exercise_id: int, exercise: Exercise):
        return self.database.update_exercise(exercise_id, exercise)
