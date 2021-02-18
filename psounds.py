from pygame import mixer
from os import path
import glob
import random
mixer.init()
mixer.music.unload
filedir = (path.dirname(path.realpath(__file__)))

def psoundplay (psoundfile):
    mixer.music.load(psoundfile)
    mixer.music.play()
    mixer.music.unload

def randomvoice (seachstring):
    string = ("{0}/{1}".format(filedir, seachstring))
    list = (glob.glob(string))
    file = (random.choice(list))
    return str(file)
    
def yes():
    psoundplay((randomvoice(("sounds/voice/yes/*.wav"))))

def no():
    psoundplay((randomvoice(("sounds/voice/no/*.wav"))))
 
def thanks ():
    psoundplay((randomvoice(("sounds/voice/thanks/*.wav"))))

def uwelcome ():
    psoundplay((randomvoice(("sounds/voice/uwelcome/*.wav"))))

def hello ():
    psoundplay((randomvoice(("sounds/voice/hello/*.wav"))))

def bye ():
    psoundplay((randomvoice(("sounds/voice/bye/*.wav"))))

def horn ():
    psoundplay((randomvoice(("sounds/horn/*.wav"))))
    
def shoot ():
    psoundplay((randomvoice(("sounds/shoot/*.wav"))))

def ping ():
    psoundplay((randomvoice(("sounds/sonar/*.mp3"))))

def bark ():
    psoundplay((randomvoice(("sounds/woof/*.wav"))))
	
def move ():
    psoundplay((randomvoice(("sounds/movment/*.wav"))))

def stop ():
    psoundplay((randomvoice(("sounds/movment/*.wav"))))