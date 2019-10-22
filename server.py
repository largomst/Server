import socket

HOST = ""
PORT = 8001
reply = b"Yes"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP 协议
s.bind((HOST, PORT))
s.listen(3)
conn, addr = s.accept()
request = conn.recv(1024)

print("request is ", request)
print("connect by", addr)
# conn.sendall(reply.encode('utf-8'))
conn.sendall(reply)
conn.close()
