import socketserver

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


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        request = self.request.recv(1024).decode("utf-8")
        print("connected by ", self.client_address[0])
        print("request is", request)

        method = request.split(" ")[0]
        src = request.split(" ")[1]

        if method == "GET":
            if src == "/test.png":
                content = pic
            else:
                content = text
            self.request.sendall(content)

        if method == "POST":
            form = request.split("\r\n")
            idx = form.index("")
            entry = form[idx:]

            value = entry[-1].split("=")[-1]
            self.request.sendall(text + b"\n<p>" + value.encode("ascii") + b"</p>")


server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
server.serve_forever()

