
from http.server import HTTPServer, BaseHTTPRequestHandler

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Docker + Jenkins + Gmail Notification Working!")

HTTPServer(("0.0.0.0", 5000), App).serve_forever()
