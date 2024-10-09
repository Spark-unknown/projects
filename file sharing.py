import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

PORT = 8010

# Get the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# Create a QR code with the IP address
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)

# Open the QR code in the web browser
webbrowser.open('myqr.svg')

# Create an HTTP server to serve the files
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your browser:", IP)
    print("or Use the QR Code")
    httpd.serve_forever()