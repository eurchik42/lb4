import socket


def handle_client_connection(conn, addr, buffer_size=4096):
    print(f"Connection established with {addr}")

    file_name = conn.recv(buffer_size).decode()
    print(f"Receiving file: {file_name}")

    with open(f"received_{file_name}", "wb") as file:
        while True:
            data = conn.recv(buffer_size)
            if not data:
                break
            file.write(data)

    print(f"File {file_name} successfully saved as received_{file_name}")
    conn.close()
    print(f"Connection with {addr} closed\n")


def start_server(host='127.0.0.1', port=50000, buffer_size=4096):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server started on {host}:{port}, waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        handle_client_connection(conn, addr, buffer_size)


if __name__ == "__main__":
    start_server()