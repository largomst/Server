import socket

# HOST = '49.235.112.129'
HOST = "127.0.0.1"
PORT = 8001

request = b"can you hear me"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# s.sendall(request.encode('utf-8'))
s.sendall(request)
reply = s.recv(1024)
print("replay is ", reply)
s.close()
