
def factorial_loop():
    number  = 5
    factorial = 1
    for i in range(2, number+1):
        factorial = factorial * i
    return factorial


def factorial_reccursion(factorial):
    if factorial == 0:
        return []
    else:
        o = factorial
        print(o)
        factorial = factorial * (factorial - 1)
        factorial_reccursion(o-1)
        
    
print(factorial_reccursion(5))

