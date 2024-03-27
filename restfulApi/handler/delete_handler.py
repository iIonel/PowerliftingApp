import json


class DeleteHandler:
    """
    Handles DELETE
    """

    def __init__(self, user_controller, exercise_controller):
        self.user_controller = user_controller
        self.exercise_controller = exercise_controller

    def handle_request(self, path, send_response, send_header, end_headers, wfile):
        if path.startswith('/users/delete/'):
            try:
                user_id = int(path.split('/')[-1])
                self.user_controller.delete_user(user_id)
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'User deleted successfully'}).encode())
                return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
                return

        elif path.startswith('/exercises/delete/'):
            try:
                exercise_id = int(path.split('/')[-1])
                self.exercise_controller.delete_exercise(exercise_id)
                send_response(200)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'message': 'Exercise deleted successfully'}).encode())
                return
            except Exception as e:
                send_response(500)
                send_header('Content-type', 'application/json')
                end_headers()
                wfile.write(json.dumps({'error': str(e)}).encode())
                return
        else:
            send_response(400)
            send_header('Content-Type', 'application/json')
            end_headers()
            wfile.write(b'Page not found')
            return
