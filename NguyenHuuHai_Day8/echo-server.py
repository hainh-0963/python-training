import socket

BACKLOG = 5 # Maximum number of connections of cubed connections
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(BACKLOG)
    conn, addr = s.accept()
    with conn:
        print('Connected by:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Data received: ", data)
            conn.sendall(data)
