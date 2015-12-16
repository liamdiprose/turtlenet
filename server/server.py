import logging
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

# Globals
BIND_ADDR = "localhost"
BIND_PORT = 54363

if len(sys.argv) == 2:
    BIND_PORT = int(sys.argv[1])
elif len(sys.argv) == 3:
    BIND_ADDR = sys.argv[1]
    BIND_PORT = sys.argv[2]



# Logging Objects
log = logging.getLogger()
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
log.addHandler(ch)

# Initiate Server Socket
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Connection Acknowledged!".encode())

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_addr = (BIND_ADDR, BIND_PORT)
    httpd = server_class(server_addr, handler_class)
    log.info("Server started on {}:{}".format(BIND_ADDR, BIND_PORT))
    httpd.serve_forever()

run()