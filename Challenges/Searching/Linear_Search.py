#Joe Young
#Sourced from - https://github.com/mrGorman/Python/blob/master/Searching/search_algorithms.py


def linear_search(key, array, index):
    """ Function to return index of key in array using
        a recursive linear search
        """
    if index == len(array):#Checks if the whole list has been checked. If no value found, -1 is returned
        return -1
    elif array[index] != key: # If the key does not equal the current index
        return linear_search(key, array, index + 1) #Recursive - Retuens the same, with an increased index
    else:
        return index #Returns the position when the value is found


test_array = ["Aardvark", "Beaver", "Cat", "Dog", "Elephant", "Frog", "Giraffe", "Hyena", 
              "Iguana", "Jaguar", "Koala", "Lion", "Monkey", "Nyala", "Ostrich", "Parrot", 
              "Quail", "Rhino", "Snake", "Tiger", "Upupa", "Viper", "Worm", "Xenon", "Zebra"]
test_cases = ["Buffalo", "Snake", "Panther", "Cat", "Dog", "Kudu", "Wolf", "Jaguar"]

for case in test_cases:
    position = linear_search(case, test_array, 0) + 1
    if position > 0:
        print(case, "found at position", position)
    else:
        print(case, "not found")