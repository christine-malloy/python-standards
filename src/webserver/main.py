from http.server import BaseHTTPRequestHandler, HTTPServer
from numpy import random

class HelloWorldHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    self.wfile.write(b"Hello! Welcome to the Python Standards project.")

def get_repo_url():
  return "https://github.com/christine-malloy/python-standards"

def get_random_number():
  return random.randint(1, 100)

def run(server_class=HTTPServer, handler_class=HelloWorldHandler, port=8080):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd server on port {port}')
  httpd.serve_forever()

if __name__ == "__main__":
  run()