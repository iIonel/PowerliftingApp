from http.server import BaseHTTPRequestHandler
from controller.exercise_controller import ExerciseController
from controller.user_controller import UserController
from handler.get_handler import GetHandler
from handler.post_handler import PostHandler
from handler.delete_handler import DeleteHandler
from handler.put_handler import PutHandler


class HttpHandler(BaseHTTPRequestHandler):
    """
    HTTP Handler for the RESTful
    """

    def __init__(self, request, client_address, server, database):
        self.user_controller = UserController(database)
        self.exercise_controller = ExerciseController(database)
        self.get_handler = GetHandler(self.user_controller, self.exercise_controller)
        self.post_handler = PostHandler(self.user_controller, self.exercise_controller)
        self.delete_handler = DeleteHandler(self.user_controller, self.exercise_controller)
        self.put_handler = PutHandler(self.user_controller, self.exercise_controller)

        super().__init__(request, client_address, server)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        self.post_handler.handle_request(self.path, post_data, self.send_response, self.send_header, self.end_headers,
                                         self.wfile)

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        self.put_handler.handle_request(self.path, post_data, self.send_response, self.send_header, self.end_headers,
                                        self.wfile)

    def do_GET(self):
        self.get_handler.handle_request(self.path, self.send_response, self.send_header, self.end_headers, self.wfile)

    def do_DELETE(self):
        self.delete_handler.handle_request(self.path, self.send_response, self.send_header, self.end_headers,
                                           self.wfile)
