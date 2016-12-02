def factorial_loop(number):
    factorial = 1
    for i in range(2, number+1):
        factorial = factorial * i
    return factorial


def factorial_reccursion(factorial):
    if factorial == 0:
        return 1
    else:
        #new_factorial = factorial
        #print(factorial)
        #factorial = factorial * (new_factorial - 1)
        return (factorial * factorial_reccursion(factorial - 1))
def main():        
    number = 5
    print(factorial_reccursion(number)) 
    print(factorial_loop((number)))

if __name__ == "__main__":
    main()