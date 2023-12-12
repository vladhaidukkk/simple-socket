import socket


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
        client_socket.sendall("Hello world!".encode())


if __name__ == "__main__":
    main()
