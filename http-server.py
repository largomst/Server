import socket

HOST = ""
PORT = 8001
text = b"""HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python server</p>
</html>
"""

f = open("test.png", "rb")
pic = b"""
HTTP/1.x 200 OK
Content-Type: image/png

"""

pic = pic + f.read()
f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = request.decode("ascii")

    method = request.split(" ")[0]
    src = request.split(" ")[1]

    if method == "GET":

        if src == "/test.png":
            content = pic
        else:
            content = text
        conn.sendall(content)

        print("connected by ", addr)
        print("requests is ", request)

    conn.close()

