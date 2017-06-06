import string




##table = [[i for i in range(0,6)],list(string.ascii_uppercase)]
##table[1].pop(10)

table = [[chr(x) for x in range(y, y + 5)] for y in range(65, 91, 5)]

for y in range(5): if x < 91: for x in range(y, y + 5): chr(x)

for row in table:
    for col in row:
        print(col, end=" ")
    print()
