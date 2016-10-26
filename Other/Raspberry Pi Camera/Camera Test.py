import picamera
import os
from time import *
from PIL import Image



#name = input("Please input your name!").lower()
#names =  (name, ".jpg")
#print(names)

##camera = picamera.PiCamera()
##camera.capture("joe.jpg")
##print("image captured")

##os.system("display " + names)
##sleep(5)
##os.system("killall display")

test1 = os.system("mirage joe.jpg")
test2 = os.system("killall mirage")
##sleep(1)


##image = Image.open("joe.jpg")
##print("image opened")
##image.show()
##print("image displayed")
##sleep(1)
##for close in psutil.process_iter():
##    if close.name() == "display":
##        close.kill()
#image.close()
