#Joe Young 26/03/2016
import time

DISTANCE = 1
SPPED_LIMIT = 70

def calculate_speed(distance, time_a, time_b):
    """Speed = distance / time"""
    diff = time_b - time_a
    MPH = (distance/diff) * 60 *60
    return MPH

def validate_number_plate(plate):
    """vaildates if the number plate is in the corrent format"""
    plate_length = len(plate)
    
    for i in range (0, plate_length):
        if (plate_length != 8):
            if (not(plate[i] == "")):
                return -1
        if (i == 2 or i == 3):
            try:
                validate = int(plate[i])
            except ValueError:
                #return ("Position " + str(i) + " should be a number not " + plate[i])
                return -1
        else:
            try:
                validate = int(plate[i])
                #return ("Position " + str(i) + " should be a string not " + plate[i])
                return -1
            except ValueError:
                pass
    return 0
        
def check_speed(speed):
    if speed < 70:
        #return "Under Speed limit"
        return 0
    else:
        return -1
        


#Testing----------------------

a = time.time()
b = time.time() + 10
Speed = calculate_speed(DISTANCE,a,b)
print (a,b)
print(Speed)

#Testing.2---------------------

validate_number_plate = (validate_number_plate("SA54 LAA"))

if (validate_number_plate == -1):
    print("Failed")
else:
    print("Passed")

#Testing 3 --------------------

if (check_speed(Speed) == -1):
    print("Speeding")
else:
    print("Underspeed limit")


#Testing 4 --------------------

