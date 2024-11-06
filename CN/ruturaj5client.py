import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '127.0.0.1'
    server_port = 12345
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server at {server_ip}:{server_port}")
    message = "Hello from Client!"
    client_socket.sendall(message.encode())
    print(f"Sent: {message}")
    data = client_socket.recv(1024).decode()
    print(f"Server says: {data}")
    client_socket.close()

if __name__ == "__main__":
    start_client()
