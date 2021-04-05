#!/usr/bin/python
import time
from os import system
import movment as movment
import sonar as sonar
import lights as lights
import psounds as psounds
import os
from time import sleep



from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import socket

PORT_NUMBER = 80
# hostname = socket.gethostname()
# host_name = socket.gethostbyname(hostname)
host_name = os.popen('ip addr show wlan0 | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\'').read().strip()
mainstyle = '''
td {
    text-align:center;
    color: white;
}
img {
    vertical-align:middle;
    max-width: 100%;
    max-height: 100%;
}

.rectangle {
  height: 768px;
  width: 1024px;
  background-color: #46523C;
}

.portrait {
    height: 100%;
    width: 100%;
}

body {
    background-color: #46523C;
}

'''
mainhtml = '''
<html>
<head><style>{0}</style>
<body>
<div class="portait"><img src="http://{11}:8081/0/stream"></div>
</body>
<html>
'''
teststyle = '''
td {
    text-align:center;
    color: white;
}
.mash-button {
    height:50px; 
    width:50px; 
}
table {
    text-align:centre;
}
'''
testhtml = ''' 
<html>
<head><style>{0}</style></head>
<body>
<h1>{1}</h1> 
<br> 2 - PAN:{2} | 3 - TILT:{3}
<br> 4 - FRONT RADAR:{4} | 5 - REAR RADAR:{5}
<br> 6 - LEFT RADAR:{6} | 7 - RIGHT RADAR:{7}
<br> 8 - FRONT LIGHT:{8} | 9 - REAR RADAR:{9}
<br> 10 - POWER:{10} | 11 - IP:{11}
<br>
</body>
</html>
'''
buttonstyle = ''' 
td {
    text-align:center;
    /*color: white;*/
    color: #46523C;
}
/*
.mash-button {
    height:50px; 
    width:50px;
    margin-top:auto;
    margin-bottom:auto;
    text-align:center;
}
*/
table {
    text-align:centre;
}

table.buttons-table {
    background-color: #46523C;
    text-align:center;
    margin-top:auto;
    margin-bottom:auto;
}

a {
    color: #46523C;
    text-align:centre;
}

a:link {
    text-decoration: none;
}

a:visited {
    text-decoration: none;
}

a:hover {
    text-decoration: none;
}

a:active {
    text-decoration: none;
}

body {
    background-color: #46523C;
}

.triangle-up {
	width: 0;
	height: 0;
	border-left: 25px solid transparent;
	border-right: 25px solid transparent;
	border-bottom: 50px solid #cacfd2;
    text-align:center;
    margin-top:auto;
    margin-bottom:auto;
}
.triangle-down {
	width: 0;
	height: 0;
	border-left: 25px solid transparent;
	border-right: 25px solid transparent;
	border-top: 50px solid #cacfd2;
    text-align:center;
    margin-top:auto;
    margin-bottom:auto;
}
.triangle-left {
	width: 0;
	height: 0;
	border-top: 25px solid transparent;
	border-right: 50px solid #cacfd2;
	border-bottom: 25px solid transparent;
    text-align:center;
    margin-top:auto;
    margin-bottom:auto;
}
.triangle-right {
	width: 0;
	height: 0;
	border-top: 25px solid transparent;
	border-left: 50px solid #cacfd2;
	border-bottom: 25px solid transparent;
    text-align:center;
    margin-top:auto;
    margin-bottom:auto;
}

.circle {
  height: 50px;
  width: 50px;
  background-color: #cacfd2;
  border-radius: 50%;
  text-align:center;
  margin-top:auto;
  margin-bottom:auto;
}

.button-fire {
	width: 45px;
	height: 45px;
	background: #cacfd2;
    text-align:center;
}

.display-box {
  width:100%;
  height:100%;
  color: #46523C;
  background-color: #cacfd2;
}


    
'''

buttonshtml = '''
<html><head><style>{0}</style><title></title></head><body>
<table class="buttons-table" cellpadding="0" cellspacing="0">
<tbody>
<tr>
<td><div class="mash-button"><a href="/powerup"><div class="button-fire"><br>P+</div></a></div></td>
<td><div class="display-box">P{10}</div></td>
<td><div class="mash-button"><a href="/forward"><div class="triangle-up"></div></a></div></td>
<td>D1</td>
<td><div class="display-box">{1}</div></td>
</tr>
<tr>
<td><div class="mash-button"><a href="/powerdown"><div class="button-fire"><br>P-</div></a></div></td>
<td><div class="mash-button"><a href="/left"><div class="triangle-left"></div></a></div></td>
<td><div class="mash-button"><a href="/stop"><div class="circle"></div></a></div></td>
<td><div class="mash-button"><a href="/right"><div class="triangle-right"></div></a></div></td>
<td>E2</td>
</tr>
<tr>
<td><div class="mash-button"><a href="/A1"><div class="button-fire">A3</div></a></div></td>
<td>B3</td>
<td><div class="mash-button"><a href="/back"><div class="triangle-down"></div></a></div></td>
<td>D3</td>
<td>E3</td>
</tr>
<tr><td><div class="display-box">-</div></td><td><div class="display-box">FL{8}</div></td><td><div class="display-box">RL{9}</div></td><td><div class="display-box">-</div></td><td><div class="display-box">-</div></td><tr>
<tr>
<td><div class="mash-button"><a href="/A1"><div class="button-fire">A4</div></a></div></td>
<td><div class="display-box">P{2}</div></td></td>
<td><div class="mash-button"><a href="/camup"><div class="triangle-up"></div></div></a></td>
<td><div class="display-box">T{3}</div></td></td>
<td>E4</td>
</tr>
<tr>
<td><div class="mash-button"><a href="/frontlight"><div class="button-fire">Front<br>light</div></a></div></td>
<td><div class="mash-button"><a href="/camleft"><div class="triangle-left"></div></div></a></td>
<td><div class="mash-button"><a href="/camstop"><div class="circle"></div></div></a></td>
<td><div class="mash-button"><a href="/camright"><div class="triangle-right"></div></div></a></td>
<td>E5</td>
</tr>
<tr>
<td><div class="mash-button"><a href="/rearlight"><div class="button-fire">Rear<br>light</div></a></div></td>
<td>B6</td>
<td><div class="mash-button"><a href="/camdown"><div class="triangle-down"></div></div></a></td>
<td>D6</td>
<td>E6</td>
</tr>
<tr>
<td><div class="mash-button"><a href="/radar"><div class="button-fire">Ping<br>Radar</div></a></div></td>
<td><div class="display-box">F{4}</div></td>
<td><div class="display-box">B{5}</div></td>
<td><div class="display-box">L{6}</div></td>
<td><div class="display-box">R{7}</div></td>
</tr>
</tbody>
</table>
</body></html>
'''
indexstyle = '''
.mash-wrapper {
    max-width: 100%;
    position: relitive;
    margin: 0 auto;
    border: 0px solid pink;
    border: 0px solid black;   
}
.main-box-format {
    float: left;
    height: 100%;
    width: 70%;
    border: 0px groove black;
    margin: 0px;
    
}
.buttons-box-format {
    position: relitive;
    float: left;
    height: 100%;
    width: 30%;
    border: 0px groove black;
    margin: 0px;
    
}

iframe {
    width: 100%;
    height: 100%;
}

.clearfix:before,
.clearfix:after {
    content: " "; /* 1 */
    display: table; /* 2 */
}
'''

indexhtml = '''
<html>
<head><style>{0}</style></head>
<body>
<div> 
<div class="mash-wrapper">
<div class="main-box-format">
<iframe id="scaled-frame"  src="/main" name="CamFrame" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen seamless></iframe>
</div>
<div class="buttons-box-format">
<iframe src="/buttons" name="ControlFrame" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen seamless></iframe>
</div>
</div> 
</div> 

</body>
</html>
'''
power = 100
status = 'Potatobot<b>v0.1'
campos = [90,90]
radarping = [999,999,999,999]
lightstatus = [0,0]
msg = "message 1"
testmsg = "mic check"

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        global power
        global status
        global campos
        global radarping
        global lightstatus
        def http_reply(html,css,sstatus,cpos,rping,lstatus,pwr):
            self.wfile.write(html.format(css,sstatus,campos[0],campos[1],radarping[0],radarping[1],radarping[2],radarping[3],lightstatus[0],lightstatus[1],pwr,host_name).encode("utf-8"))
  
        if self.path=="/":
            http_reply(indexhtml,indexstyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=="/buttons":
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=="/test":
            http_reply(testhtml,teststyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=="/main":
            http_reply(mainhtml,mainstyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=='/frontlight':
            fls=lightstatus[0]
            rls=lightstatus[1]
            if fls==0:
                lightstatus=[1,rls]
                status='FLON'
            elif fls==1:
                lightstatus=[0,rls]
                status='FLOFF'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/rearlight':
            fls=lightstatus[0]
            rls=lightstatus[1]
            if rls==0:
                lightstatus=[fls,1]
                status='RLON'
            elif rls==1:
                lightstatus=[fls,0]
                status='RLOFF'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)
            
            
        elif self.path=='/powerup':
            if power < 100:
                status='power+'
                power = power+10
            else:
                status='MAX'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=='/powerdown':
            if power > 0:
                status='power-'
                power = power-10
            else:
                status='MIN'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/radar':
            status='FIRE'
            frontdist = sonar.pingFront()
            reardist = sonar.pingRear()
            leftdist = sonar.pingLeft()
            rightdist = sonar.pingRight()
            radarping = [frontdist,reardist,leftdist,rightdist]
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/forward':
            status='GO^'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)
            movment.allstop(0)
            movment.forward(0,power)
            

        elif self.path=='/back':
            movment.allstop(0)
            movment.backwards(0,power)
            status='GOv'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/left':
            movment.allstop(0)
            movment.TurnLeft(0,power)
            status='GO<'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/right':
            movment.allstop(0)
            movment.TurnRight(0,power)
            status='GO>'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/stop':
            movment.allstop(0)
            status='STOP'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/camstop':
            status='CAM RESET'
            campos.clear()
            campos.insert(0,90)
            campos.insert(1,90)
            movment.servoa(90)
            movment.servob(90)
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/camup':
            pan = campos[0]
            agl = campos[1]
            if agl > 56:
                agl = agl-12
                status='CAM^'
                campos.pop(1)
                campos.insert(1,agl)
                movment.servoa(agl)
            else:
                status='MAX'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        elif self.path=='/camdown':
            pan = campos[0]
            agl = campos[1]
            if agl < 138:
                status='CAMV'
                agl = agl+12
                campos.pop(1)
                campos.insert(1,agl)
                movment.servoa(agl)
            else:
                status='MAX'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=='/camleft':
            pan = campos[0]
            agl = campos[1]
            if pan < 180:
                status='CAM<'
                pan = pan+30
                campos.pop(0)
                campos.insert(0,pan)
                movment.servob(pan)
            else:
                status='MAX'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)
            
        elif self.path=='/camright':
            pan = campos[0]
            agl = campos[1]
            if pan > 0:
                status='CAM>'
                pan = pan-30
                campos.pop(0)
                campos.insert(0,pan)
                movment.servob(pan)
            else:
                status='MAX'
            http_reply(buttonshtml,buttonstyle,status,campos,radarping,lightstatus,power)

        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype='image/jpg'
                sendReply = True
            if self.path.endswith(".png"):
                mimetype='image/png'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it
                f = open(curdir + sep + self.path, 'rb' ) 
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            return


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

try:
    server = HTTPServer((host_name, PORT_NUMBER), myHandler)
    print ("http://{0}:{1}".format(host_name,PORT_NUMBER))
    server.serve_forever()

except KeyboardInterrupt:
    print ("http://{0}:{1} shutting down".format(host_name,PORT_NUMBER))
    server.socket.close()