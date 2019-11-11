from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi



class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/login"):
            self.send_response(200)
            self.send_header("Content-type", "text-html")
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<form method='POST' enctype='multipart/form-data' action='/login'>"
            output += "<input name='user' type='text'>"            
            output += "<input type='submit' value='submit'>"
            output += "</form></body></html>"
            self.wfile.write(output)
            print output
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

            
    def do_POST(self):
        self.send_response(301)
        self.end_headers()
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            fields=cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('user')            
            
            if messagecontent[0] == 'ahmed':
                output = ""
                output += "<html><body>"
                output += " <h2> Login Successful: </h2>"
                output += "<h1> Hello Mr: %s </h1>" % messagecontent[0]
                output += "<form method='POST' enctype='multipart/form-data' action='/login'>"
                output += "<input name='user' type='text'>"                
                output += "<input type='submit' value='submit'></form>"                
                output += "</html></body>"
                self.wfile.write(output)
                print output
            else:
                output = ""
                output += "<html><body>"
                output += " <h2> Login Failed: </h2>"
                output += "<h3> Sorry Mr: %s  " % messagecontent[0] + "We Don't Has User name '%s' </h3>" % messagecontent[0]                
                output += "<form method='POST' enctype='multipart/form-data' action='/login'>"
                output += "<input name='user' type='text'>"
                output += "<input type='submit' value='submit'></form>"
                output += "</html></body>"
                self.wfile.write(output)
                print output
            
            
            
        else:
            pass







def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Server Is running on port 8080"
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C Entered, Server Is Clossing Now..."
        server.socket.close()


if __name__ == '__main__':
    main()
