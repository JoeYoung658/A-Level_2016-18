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
    if (plate_length != 7):
        return "Incorrect length"
    for i in range (0, plate_length):
        if (i == 2 or i == 3):
            try:
                validate = int(plate[i])
            except ValueError:
                return ("Position " + str(i) + " should be a number not " + plate[i])
        else:
            try:
                validate = int(plate[i])
                return ("Position " + str(i) + " should be a string not " + plate[i])
            except ValueError:
                pass
    return "Passed"
        
def check_speed(speed):
    if speed < 70:
        return "Under Speed limit"
    else:
        return "Over Speed limit"
        


#Testing----------------------

a = time.time()
b = time.time() + 10
Speed = calculate_speed(DISTANCE,a,b)
print (a,b)
print(Speed)

#Testing.2---------------------

print(validate_number_plate("SA54LAA"))

#Testing 3 --------------------

print(check_speed(Speed))