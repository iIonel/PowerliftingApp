import json
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler
from controller.exercise_controller import ExerciseController
from controller.user_controller import UserController
from model.models import User, PersonalRecord, Exercise


class HttpHandler(BaseHTTPRequestHandler):
    """
    HTTP Handler for the RESTful
    """
    def __init__(self, request, client_address, server, database):
        self.user_controller = UserController(database)
        self.exercise_controller = ExerciseController(database)

        super().__init__(request, client_address, server)

    def do_GET(self):
        if self.path == '/users/':
            users = self.user_controller.get_users()
            if users:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([user.to_dict() for user in users]).encode())
                return
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'No users found')
                return
        elif self.path.startswith('/users/email/'):
            user_email = self.path.split('/')[-1]
            user = self.user_controller.get_user_by_email(user_email)
            if user:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(user.to_dict()).encode())
                return
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'User not found')
                return
        elif self.path.startswith('/users/status/'):
            user_status = self.path.split('/')[-1]
            users = self.user_controller.get_users_by_status(user_status)
            if users:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps([user.to_dict() for user in users]).encode())
                return
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'No users found')
                return
        elif self.path.startswith('/users/pr/'):
            user_pr = self.path.split('/')[-1]
            user = self.user_controller.get_personal_records(user_pr)
            if user:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(user.to_dict()).encode())
                return
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'User not found')
                return
        elif self.path == '/exercises/':
            exercises = self.exercise_controller.get_exercises()
            if exercises:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                exercises_dicts = [exercise.to_dict() for exercise in exercises]
                self.wfile.write(json.dumps(exercises_dicts).encode())
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'No exercises found')
                return
        elif self.path.startswith('/users/'):
            user_id = int(self.path.split('/')[-1])
            user = self.user_controller.get_user(user_id)
            if user:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(user.to_dict()).encode())
                return
            else:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(b'User not found')
                return
        else:
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'Page not found')
            return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        if self.path.startswith('/users/add/'):
            try:
                user_data = json.loads(post_data)
                new_user = User(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    email=user_data['email'],
                    age=user_data['age'],
                    natty=user_data['natty'],
                    weight=user_data['weight'],
                    height=user_data['height']
                )
                self.user_controller.add_user(new_user)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'User added successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

        elif self.path.startswith('/users/add_record/'):
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                personal_record_data = json.loads(post_data)
                new_personal_record = PersonalRecord(
                    user_id=personal_record_data['user_id'],
                    squat=personal_record_data['squat'],
                    bench=personal_record_data['bench'],
                    deadlift=personal_record_data['deadlift']
                )
                self.user_controller.add_personal_record(new_personal_record)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Personal record added successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

        elif self.path.startswith('/exercises/add/'):
            try:
                exercise_data = json.loads(post_data)
                new_exercise = Exercise(
                    name=exercise_data['name'],
                    description=exercise_data['description'],
                    video_link=exercise_data['video_link'],
                )

                self.exercise_controller.add_exercise(new_exercise)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Exercise added successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_DELETE(self):
        if self.path.startswith('/users/delete/'):
            try:
                user_id = int(self.path.split('/')[-1])
                self.user_controller.delete_user(user_id)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'User deleted successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

        elif self.path.startswith('/exercises/delete/'):
            try:
                exercise_id = int(self.path.split('/')[-1])
                self.exercise_controller.delete_exercise(exercise_id)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Exercise deleted successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_PUT(self):
        if self.path.startswith('/users/update/'):
            try:
                user_id = int(self.path.split('/')[-1])
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                user_data = json.loads(post_data)
                updated_user = User(**user_data)
                self.user_controller.update_user(user_id, updated_user)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'User updated successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())

        elif self.path.startswith('/exercises/update/'):
            try:
                exercise_id = int(self.path.split('/')[-1])
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                exercise_data = json.loads(post_data)
                updated_exercise = Exercise(**exercise_data)
                self.exercise_controller.update_exercise(exercise_id, updated_exercise)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'message': 'Exercise updated successfully'}).encode())
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())