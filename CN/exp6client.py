import socket

# Server details
host = "127.0.0.1"
port = 12000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# File to be sent
filename = "server.txt"
with open(filename, 'rb') as f:
    data = f.read(1024)
    while data:
        # Send the file data in chunks
        sock.sendto(data, (host, port))
        data = f.read(1024)

# After sending the file, send an empty message to signify the end
sock.sendto(b"", (host, port))
print('File sent successfully!')

# Close the socket
sock.close()
