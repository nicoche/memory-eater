import argparse
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps

class Server(HTTPServer):
    def __init__(self, address, request_handler):
        super().__init__(address, request_handler)

class Path:
    BASE = "/"
    ALLOCATE = "/allocate"

class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server_class):
        self.server_class = server_class
        super().__init__(request, client_address, server_class)

    def do_GET(self):
        if self.path == "/allocate":
            print("hi")
            sleep(3)
            print("allocating...")
            xd = []
            for i in range(10000):
                xd.append(bytearray(512000000 + i))
                print("allocated 512Mb")
            sleep(1)
            print(len(xd))

        response = {"message": "Hello world"}
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Content-Length", str(len(dumps(response))))
        self.end_headers()
        self.wfile.write(str(response).encode('utf8'))

def start_server(addr, port, server_class=Server, handler_class=RequestHandler):
    server_address = (addr, port)
    http_server = server_class(server_address, handler_class)
    print(f"Starting server on {addr}:{port}")
    http_server.serve_forever()

def main():
    parser = argparse.ArgumentParser(description="Run a simple HTTP server.")
    parser.add_argument(
        "-l",
        "--listen",
        default="0.0.0.0",
        help="Specify the IP address which server should listen",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port which server should listen",
    )
    args = parser.parse_args()
    start_server(addr=args.listen, port=args.port)


if __name__ == "__main__":
    main()
