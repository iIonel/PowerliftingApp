from http.server import BaseHTTPRequestHandler


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('')
        self.end_headers()
        self.wfile.write(b'')