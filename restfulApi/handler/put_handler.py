import json

from model.models import User, Exercise


class PutHandler:
    def __init__(self, user_controller, exercise_controller):
        self.user_controller = user_controller
        self.exercise_controller = exercise_controller

    def handle_request(self, path, post_data, send_response, send_header, end_headers, wfile):
        if path.startswith('/users/update/'):
            try:
                user_id = int(path.split('/')[-1])
                user_data = json.loads(post_data)
                updated_user = User(
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    email=user_data['email'],
                    age=user_data['age'],
                    natty=user_data['natty'],
                    weight=user_data['weight'],
                    height=user_data['height']
                )
                self.user_controller.update_user(user_id, updated_user)
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'User updated successfully'}).encode())
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())

        elif path.startswith('/exercises/update/'):
            try:
                exercise_id = int(path.split('/')[-1])
                exercise_data = json.loads(post_data)
                updated_exercise = Exercise(
                    name=exercise_data['name'],
                    description=exercise_data['description'],
                    video_link=exercise_data['video_link'],
                )
                self.exercise_controller.update_exercise(exercise_id, updated_exercise)
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'Exercise updated successfully'}).encode())
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            send_response(400)
            send_header('Content-Type', 'application/json')
            end_headers()
            wfile.write(b'Page not found')
            return