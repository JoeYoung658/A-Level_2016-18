
def factorial_loop():
    number  = 5
    factorial = 1
    for i in range(2, number+1):
        factorial = factorial * i
    return factorial


def factorial_reccursion(factorial):
    if factorial == 0:
        return factorial
    else:
        new_factorial = factorial
        print(new_factorial)
        factorial = factorial * (new_factorial - 1)
        return (factorial_reccursion(new_factorial- 1))
        
    
print(factorial_reccursion(5))

