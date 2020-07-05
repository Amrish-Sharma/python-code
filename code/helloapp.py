from wsgiref.simple_server import make_server

def hello_app(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return["Hello Foothill!".encode("utf-8")]

server = make_server('localhost', 8080, hello_app)

server.serve_forever()