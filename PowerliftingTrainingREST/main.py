from http.server import HTTPServer
from controller.http_handler import HttpHandler
from util.database import Database


database = Database()
server = ('', 8000)
http = HTTPServer(server, lambda request, client_address, server: HttpHandler(request, client_address, server, database))
print('server started on http://localhost:8000')
http.serve_forever()
