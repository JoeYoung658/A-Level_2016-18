def Fibonacci(Max,a,b):
    
    new = a + b
    print(new)

    if a >= Max:
        return 0
    else:
        return Fibonacci(Max,b,new)


Fibonacci(10,0,1)
