import time
import curses
from os import system
import movment as movment
import sonar as sonar
import lights as lights
import psounds as psounds
## -above this is edit - ##
import RPi.GPIO as GPIO
import os
from time import sleep
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.240.14'  # Change this to your Raspberry Pi IP address
host_port = 8000


class MyServer(BaseHTTPRequestHandler):
    """ A special implementation of BaseHTTPRequestHander for reading data from
        and control GPIO of a Raspberry Pi
    """

    def do_HEAD(self):
        """ do_HEAD() can be tested use curl command
            'curl -I http://server-ip-address:port'
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        """ do_GET() can be tested using curl command
            'curl http://server-ip-address:port'
        """
        html = '''
           <html>
           <body style="width:960px; margin: 20px auto;">
           <h1>MAsh PytAto!</h1>
           <p>Current GPU temperature is {}</p>
           <p><a href="/forward">  -^-</a></p>
           <p><a href="/left"><</a> <a href="/stop">O</a> <a href="/right">></a></p>
           <p><a href="/back">  -V-</a></p>
           <div id="led-status"></div>
           <script>
               document.getElementById("led-status").innerHTML="{}";
           </script>
           </body>
           </html>
        '''
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        power = 100
        if self.path=='/':
            movment.allstop(0)
        elif self.path=='/forward':
            movment.allstop(0)
            movment.forward(0,power)
            status='FORWARD'
        elif self.path=='/back':
            movment.allstop(0)
            movment.backwards(0,power)
            status='BACK'
        elif self.path=='/left':
            movment.allstop(0)
            movment.TurnLeft(0,power)
            status='LEFT'
        elif self.path=='/right':
            movment.allstop(0)
            movment.TurnRight(0,power)
            status='RIGHT'
        elif self.path=='/stop':
            movment.allstop(0)
            status='STOP'
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))


if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
