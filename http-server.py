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
<image src='./test.png'/>
<form name="input" action="/" method="post">
First name:<input type="text" name="firstname"><br>
<input type="submit" value="submit"> 
</form>
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
    request = conn.recv(1024).decode("ascii")

    method = request.split(" ")[0]
    src = request.split(" ")[1]

    print("connected by ", addr)
    print("requests is ", request)

    if method == "GET":

        if src == "/test.png":
            content = pic
        else:
            content = text
        conn.sendall(content)

    if method == "POST":
        form = request.split("\r\n")
        idx = form.index("")
        entry = form[idx:]

        value = entry[-1].split("=")[-1]
        conn.sendall(text + b"\n<p>" + value.encode('ascii') + b"</p>")

    conn.close()

