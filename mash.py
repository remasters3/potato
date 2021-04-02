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
#         html = '''
#            <html>
#            <body style="width:960px; margin: 20px auto;">
#            <h1>MAsh</h1>
#            <p>
#            TEMP{}
#            <br>----<a href="/forward">^</a>----
#            <br><a href="/left"><</a>--<a href="/stop">O</a>--<a href="/right">></a>
#            <br>----<a href="/back">V</a>----
#            </p>
#            <div id="led-status"></div>
#            <script>
#                document.getElementById("led-status").innerHTML="{}";
#            </script>
#            </body>
#            </html>
#         '''
        html = '''
        <html>
        <head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type"><title></title></head>
        <body>
        <table>
        <tbody>
        <tr>
        <td></td>
        <td>TEMP{}</td>
        <td></td>
        </tr>
        <tr>
        <td style="width: 18.7667px; text-align: center;">&nbsp;</td>
        <td style="width: 18.7833px; text-align: center;"><a href="/forward" ><img style="border: 0px solid ; width: 50px; height: 50px;" alt="" src="http://192.168.240.14/potato/images/forward.png"></a></td>
        <td style="width: 27.45px; text-align: center;">&nbsp;</td>
        </tr>
        <tr style="text-align: right;">
        <td style="width: 18.7667px; text-align: center;"><a href="/left"><img style="border: 0px solid ; width: 50px; height: 50px;" src="http://192.168.240.14/potato/images/left.png" alt="" hspace="0" vspace="0"></a></td>
        <td style="width: 18.7833px; text-align: center;"><a href="/stop"><img style="border: 0px solid ; width: 50px; height: 50px;" src="http://192.168.240.14/potato/images/stop.png" alt=""></a></td>
        <td style="width: 27.45px; text-align: center;"><a href="/right"><img style="border: 0px solid ; width: 50px; height: 50px;" src="http://192.168.240.14/potato/images/right.png" alt=""></a></td>
        </tr>
        <tr style="text-align: center;">
        <td style="width: 18.7667px;">&nbsp;</td>
        <td style="width: 18.7833px; text-align: center;"><a href="/back"><img style="border: 0px solid ; width: 50px; height: 50px;" alt="" src="http://192.168.240.14/potato/images/back.png"></a></td>
        <td style="width: 27.45px; text-align: center;">&nbsp;</td>
        </tr>
        <tr>
        <td></td>
        <td>
        <div id="led-status"></div>
        </td>
        <td></td>
        </tr>
        </tbody>
        </table>
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
