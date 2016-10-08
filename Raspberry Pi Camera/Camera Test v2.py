import subprocess
import picamera
import os
from time import *

running = True
while running:
    name = raw_input("Please input your name!").lower()
    camera = picamera.PiCamera()
    camera.capture("joe.jpg")
    print("image captured")
    sleep(1)
    subprocess.Popen(["mirage", "--fullscreen", "joe.jpg" ])
    sleep(10)
    os.system("killall mirage")
