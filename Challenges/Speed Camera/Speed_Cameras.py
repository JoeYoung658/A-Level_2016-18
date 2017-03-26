#Joe Young 26/03/2016

import time




def calculate_speed(distance, time_a, time_b):
    """Speed = distance / time"""
    diff = time_b - time_a
    MPH = (distance/diff) * 60 *60
    return MPH




#Testing----------------------
DISTANCE = 1
a = time.time()
b = time.time() + 100
Speed = calculate_speed(DISTANCE,a,b)
print (a,b)
print(Speed)
