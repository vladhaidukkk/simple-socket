import socket

RESOURCES = {
    "/": "<h1>Hello world!</h1>",
    "/blog": "<h1>Blog</h1>",
}


def parse_request(request: str) -> tuple[str, str]:
    method, uri, _ = request.split(" ", 2)
    return method, uri


def generate_status_line(method: str, uri: str) -> tuple[str, int]:
    if method != "GET":
        code, phrase = 405, "Method Not Allowed"
    elif uri not in RESOURCES:
        code, phrase = 404, "Not Found"
    else:
        code, phrase = 200, "OK"

    return f"HTTP/1.1 {code} {phrase}", code


def generate_body(uri: str, code: int) -> str:
    match code:
        case 404:
            return "<h1>404</h1><p>Not Found</p>"
        case 405:
            return "<h1>405</h1><p>Method Not Allowed</p>"
        case _:
            return RESOURCES[uri]


def generate_response(request: str) -> bytes:
    method, uri = parse_request(request)
    status_line, code = generate_status_line(method, uri)
    body = generate_body(uri, code)
    return f"{status_line}\n\n{body}".encode()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 5050))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Client {addr[0]}:{addr[1]} connected")
        request = client_socket.recv(1024)
        print(request.decode("utf-8"))
        response = generate_response(request.decode("utf-8"))
        client_socket.sendall(response)


if __name__ == "__main__":
    main()
