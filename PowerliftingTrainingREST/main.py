from http.server import HTTPServer

from controllers.http_handler import HttpHandler

server = ('localhost', 8000)
http = HTTPServer(server, HttpHandler)
print('server started on http://localhost:8080')
http.serve_forever()
