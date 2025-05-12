from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <center>
    <h1>Welcome</h1>
    
    <h2>TCP/IP Protocols </h2>
    </center
</head>
<body>

    
        

        <h2>1. Application Layer</h2>
        <ul>
            <li>HTTP</li>
            <li>HTTPS</li>
            <li>FTP</li>
            <li>SMTP</li>
            <li>DNS</li>
            
        </ul>

        <h2>2. Transport Layer</h2>
        <ul>
            <li>TCP </li>
            <li>UDP</li>
        </ul>

        <h2>3. Internet Layer</h2>
        <ul>
            <li>IP</li>
            <li>ICMP</li>
            <li>ARP</li>
            <li>RARP</li>
        </ul>

        <h2>4. Network Access Layer</h2>
        <ul>
            <li>Ethernet</li>
            <li>Wi-Fi</li>
            <li>PPP (Point-to-Point Protocol)</li>
            <li>MAC</li>
        </ul>
    

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()


