import json

from model.models import User, PersonalRecord, Exercise


class PostHandler:
    def __init__(self, user_controller, exercise_controller):
        self.user_controller = user_controller
        self.exercise_controller = exercise_controller

    def handle_request(self, path, post_data, send_response, send_header, end_headers, wfile):
        if path.startswith('/users/add/'):
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
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'User added successfully'}).encode())
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())

        elif path.startswith('/users/add_record/'):
            try:
                personal_record_data = json.loads(post_data)
                new_personal_record = PersonalRecord(
                    user_id=personal_record_data['user_id'],
                    squat=personal_record_data['squat'],
                    bench=personal_record_data['bench'],
                    deadlift=personal_record_data['deadlift']
                )
                self.user_controller.add_personal_record(new_personal_record)
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'Personal record added successfully'}).encode())
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())

        elif path.startswith('/exercises/add/'):
            try:
                exercise_data = json.loads(post_data)
                new_exercise = Exercise(
                    name=exercise_data['name'],
                    description=exercise_data['description'],
                    video_link=exercise_data['video_link'],
                )

                self.exercise_controller.add_exercise(new_exercise)
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'Exercise added successfully'}).encode())
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