#Joe Young #03/02/2016 #v1.0
#http://www.theorytestadvice.co.uk/driving-test/marking/distance.htm
def weather(conditions, distance_from_car):
    if conditions == "dry":
        return distance_from_car
    elif conditions == "wet" or conditions == "foggy" or conditions == "other":
        return distance_from_car*2
    else:
        print("Please input a vaild weather condition! (Wet, dry, foggy or other)")
        return ("error")
def distance_from_fcar(speed, cartype):
    carl = 4.5
    lorryl = 10
    if cartype == "car":
        if speed < 10:
            return carl
        else:
            distance = (speed//10)*carl
            return distance
    elif cartype == "lorry":
        if speed < 10:
            return lorryl
        else:
            distance = (speed//10)*lorryl
            return distance
    else:
        print("Please input a vaild car type! (Car or lorry)")
        return ("error")   
def equidistant(valuea, valueb):
     me = str((valuea + valueb)/2)
     return me
def main():
    print("- The average car lenth is 4.5m. \n- The average lorry lenth is 10m.\n")
    cara = int(input("How far away is the car in frout in meters?"))
    carb = int(input("How far away is the car behind in meters?"))
    speed = int(input("What is your speed? (MPH)"))
    while True:
        cartype = str(input("What type of car is in frount of you? (Car or Lorry)")).lower()
        distance_from_car = distance_from_fcar(speed, cartype)
        if not(distance_from_car == "error"):
            break
    while True:
        weatheri = str(input("What are the weather conditions? (Wet, dry, foggy or other)")).lower()
        end_distance = weather(weatheri, distance_from_car)
        if not(end_distance == "error"):
            break
    print("You should be "+ equidistant(cara, carb)+ "m away from the car in froutn and behind to be in the middle of both the cars")
    if distance_from_car == end_distance:
        print("You should be", end_distance, "away from the car in frount as you are travling", str(speed) +"MPH" )
    else:
        print("You should be", end_distance,  "away from the car in frount as you are travling", str(speed) + "MPH, as well as the bad weather conditions.")
if __name__ == "__main__":
    main()