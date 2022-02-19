import http.server
import socketserver
import json

PORT = 8080


class RestAPI(http.server.SimpleHTTPRequestHandler):

    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        output_data = {'status': 'OK', 'result': 'HELLO WORLD GET!'}
        output_json = json.dumps(output_data)

        self.wfile.write(output_json.encode('utf-8'))

    def do_POST(self):
        # - request -

        content_length = int(self.headers['Content-Length'])
        # print('content_length:', content_length)

        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None

        print(f'input_data => ', input_data)

        # - response -

        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        output_data = {'status': 'OK', 'result': 'HELLO WORLD!'}
        output_json = json.dumps(output_data)

        self.wfile.write(output_json.encode('utf-8'))


rest_api = RestAPI

try:
    with socketserver.TCPServer(("", PORT), rest_api) as httpd:
        print(f"Starting http://0.0.0.0:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Detener => Ctrl+C")
    httpd.server_close()
