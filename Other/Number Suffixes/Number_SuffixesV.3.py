#V.2
def number_suffixes(value):
    try:
        value = int(value)
    except ValueError:
        return value

    if value % 10 == 1 and (value % 100) // 10 != 1:
        suffix = "st" 
    elif value % 10 == 2 and value % 100//10 != 1:         
        suffix = "nd"          
    elif value % 10 == 3 and value % 100//10 != 1:          
        suffix = "rd"           
    else:           
        suffix = "th"
        
    return (str(value) + suffix)

##for i in range(1,3000):
##	print(number_suffixes(i))


print(number_suffixes(5))


##print(number_suffixes(112))
#1
