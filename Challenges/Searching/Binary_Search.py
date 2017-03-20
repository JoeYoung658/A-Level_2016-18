#Joe Young
#Sourced from - https://github.com/mrGorman/Python/blob/master/Searching/search_algorithms.py

def binary_search(key, array, min, max):
    """ Function to return index of key in array using 
        a recursive binary search
        """
    if max < min:
        return -1 #Standard for when there is an error. i.e retuns -1 when key not found within the list
    else:
        mid_point = int((min + max) / 2) #Finds the mid point of the array.
    
    if array[mid_point] < key: #Checks if the key is below the mid point.
        return binary_search(key, array, mid_point + 1, max) #Recursive, calls it self to look in the new range on the array then sends new values.
    elif array[mid_point] > key:
        return binary_search(key, array, min, mid_point - 1)#Does the same as above but the other away around.
    else:
        return mid_point #Returns if the value is found as it wouldn't be above or below the key.

"""Array needs to be in alphabetical order, if it was a list of ints it would need to go
in numeric order i.e 1 2 3"""
test_array = ["Aardvark", "Beaver", "Bill", "Cat", "Dog", "Elephant", "Frog", "Giraffe", "Hyena", 
              "Iguana", "Jaguar", "Koala", "Lion", "Monkey", "Nyala", "Ostrich", "Parrot", 
              "Quail", "Rhino", "Snake", "Tiger", "Upupa", "Viper", "Worm", "Xenon", "Zebra"] 

#Different test cases which will be put though the sytem - Currently case sensitive
test_cases = ["Buffalo", "Snake", "Panther", "Cat", "Dog", "Kudu", "Wolf", "Jaguar", "bill"]

for case in test_cases:
    position = binary_search(case, test_array, 0, len(test_array) - 1) + 1 #Adds one onto the end otherwise it would start from 0 onwards.
    if position > 0:
        print(case +  " found at position " + str(position))
    else:
        print(case  + " not found")