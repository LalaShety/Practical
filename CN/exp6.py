import socket

# Server details
host = "127.0.0.1"
port = 12000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

# Open a file to write the received data
f = open('Myfile2.txt', 'wb')
print('New file created')

while True:
    # Receive data
    data, addr = sock.recvfrom(1024)
    
    if not data:
        # If no data, file transfer is complete
        break
    
    # Write the received data into the file
    f.write(data)
    print(f"[RECEIVING] {data}")

# Close the file after the transfer is done
print('File is successfully received!!!')
f.close()

# Read and print the file content
f = open('server.txt', 'r')
print(f.read())
f.close()

# Close the server socket
sock.close()
print('Connection closed!')
