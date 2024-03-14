import http.server
import sys
import json
from datetime import datetime
from urllib.parse import parse_qs

RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"

class ExtendedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        current_time = datetime.now().strftime("%H:%M:%S")
        client_ip = self.client_address[0]

        sys.stderr.write(f"{CYAN}{current_time}{RESET} {BOLD}{GREEN}{client_ip}{RESET} - {format % args}\n")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        try:
            post_data_dict = {k: v[0] for k, v in parse_qs(post_data).items()}
            post_data_formatted = json.dumps(post_data_dict, indent=4)
        except Exception as e:
            post_data_formatted = post_data  # fallback to raw on error

        print(f"\n{BOLD}{GREEN}Received POST request on:{RESET} {self.path}")
        print(f"{YELLOW}POST request body:{RESET}\n{post_data_formatted}\n")

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = "POST request received."
        self.wfile.write(response.encode('utf-8'))

def run(server_class=http.server.HTTPServer, handler_class=ExtendedHTTPRequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 80
    run(port=port)
