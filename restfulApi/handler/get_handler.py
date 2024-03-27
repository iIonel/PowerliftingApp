import json


class GetHandler:
    """
    Handles GET
    """

    def __init__(self, user_controller, exercise_controller):
        self.user_controller = user_controller
        self.exercise_controller = exercise_controller

    def handle_request(self, path, send_response, send_header, end_headers, wfile):
        if path == '/users/':
            try:
                users = self.user_controller.get_users()
                if users:
                    send_response(200)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(json.dumps([user.to_dict() for user in users]).encode())
                    return
                else:
                    send_response(400)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(b'No users found')
                    return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())

        elif path.startswith('/users/email/'):
            try:
                user_email = path.split('/')[-1]
                user = self.user_controller.get_user_by_email(user_email)
                if user:
                    send_response(200)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(json.dumps(user.to_dict()).encode())
                    return
                else:
                    send_response(400)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(b'User not found')
                    return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
        elif path.startswith('/users/status/'):
            try:
                user_status = path.split('/')[-1]
                users = self.user_controller.get_users_by_status(user_status)
                if users:
                    send_response(200)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(json.dumps([user.to_dict() for user in users]).encode())
                    return
                else:
                    send_response(400)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(b'No users found')
                    return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
        elif path.startswith('/users/pr/'):
            try:
                user_pr = path.split('/')[-1]
                user = self.user_controller.get_personal_records(user_pr)
                if user:
                    send_response(200)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(json.dumps(user.to_dict()).encode())
                    return
                else:
                    send_response(400)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(b'User not found')
                    return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
        elif path == '/exercises/':
            try:
                exercises = self.exercise_controller.get_exercises()
                if exercises:
                    send_response(200)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    exercises_dicts = [exercise.to_dict() for exercise in exercises]
                    wfile.write(json.dumps(exercises_dicts).encode())
                else:
                    send_response(400)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(b'No exercises found')
                    return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
        elif path.startswith('/users/'):
            try:
                user_id = int(path.split('/')[-1])
                user = self.user_controller.get_user(user_id)
                if user:
                    send_response(200)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(json.dumps(user.to_dict()).encode())
                    return
                else:
                    send_response(400)
                    send_header('Content-Type', 'application/json')
                    end_headers()
                    wfile.write(b'User not found')
                    return
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
