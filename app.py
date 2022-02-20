import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs
from services import properties_habi as habi_services

PORT = 8081


class RestAPI(http.server.SimpleHTTPRequestHandler):

    def do_GET(self) -> None:
        query_components = parse_qs(urlparse(self.path).query)
        print(f'queryParams ==> ', query_components)
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

        output_data = {'status': 'OK', 'result': 'Hola Mundo GET!'}
        output_json = json.dumps(output_data)

        self.wfile.write(output_json.encode('utf-8'))

    def do_POST(self) -> None:
        # - request -
        print(f"api call ==> ", self.path)
        output_data = "{'status': 'ERROR', 'result': 'API_NOT_FOUND'}"
        content_length = int(self.headers['Content-Length'])
        # print('content_length:', content_length)

        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None

        print(f'payload json => ', input_data)

        if not self.path != '/habi' or not self.path != '/habi/':
            output_data = habi_services.get_habi_property_list(input_data)

        # - response -

        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

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
