from pygame import mixer
from os import path
mixer.init()
mixer.music.unload
filedir = (path.dirname(path.realpath(__file__)))

def horn ():
    file = ("{0}/{1}".format(filedir, "sounds/horn.wav"))
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.unload
    
def rocket ():
    file = ("{0}/{1}".format(filedir, "sounds/explosion.wav"))
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.unload

def ping ():
    file = ("{0}/{1}".format(filedir, "sounds/sonar_ping.mp3"))
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.unload

def bark ():
    file = ("{0}/{1}".format(filedir, "sounds/dogbrk.wav"))
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.unload
	
def move ():
    file = ("{0}/{1}".format(filedir, "sounds/Trash_Can.wav"))
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.unload

def stop ():
    file = ("{0}/{1}".format(filedir, "sounds/dryer_door.wav"))
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.unload