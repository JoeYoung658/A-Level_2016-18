#Joe Young

print("This")
print("is")
print("a")
print("sequence")

for i in range(5):
    print("This is a iteration the", i, "time around")


if 1 == 2:
    print("")
else:
    print("This an example of branching")


GlobalVarible = 2

def testfunction(a,b):
    global GlobalVarible
    return (GlobalVarible * a * b)


print(testfunction(2,2))

def testprocedure():
    test = True

print(testprocedure())



def add_message(name):
##    global name
    name = "Hello, " + name
    print("Inside:", name)

name = "Sam"
add_message(name)
print("Outside:", name)
