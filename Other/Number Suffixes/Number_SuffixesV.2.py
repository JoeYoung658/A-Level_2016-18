#V.2



def number_suffixes(value):
    try:
        value = int(value)
    except ValueError:
        return value

    if value % 100//10 != 1:
        """checks if the number is at a value with does not follow the normal rules
for example "212th or "17th" etc " """
        if value % 10 == 1: 
            """checks if number ends in 1 and if it does the
    number must need a "st" on the end of it"""
            number_with_suffix = (str(value)+ "st")
            
        elif value % 10 == 2:
            
            number_with_suffix = (str(value)+ "nd")
            
        elif value % 10 == 3:
            
            number_with_suffix = (str(value)+  "rd")
            
        else:
            
            number_with_suffix = (str(value) +  "th")
    else:
        
        number_with_suffix = (str(value),  "th")

    return number_with_suffix


for i in range(1,50000):
	print(number_suffixes(i))
