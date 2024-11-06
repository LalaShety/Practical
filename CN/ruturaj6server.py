import socket

# Server details
host = "127.0.0.1"
port = 12000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

print("Server is listening...")

# File to be saved
filename = "received_file.txt"

with open(filename, 'wb') as f:
    while True:
        # Receive data from the client
        data, addr = sock.recvfrom(1024)

        # Check for the end signal
        if not data:
            print("End of file received.")
            break

        # Write the received data to the file
        f.write(data)

print(f"File received and saved as '{filename}'.")

# Close the socket
sock.close()
