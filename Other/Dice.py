import random

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)

if a == b == c:
    score = a + b + c
elif a == b:
    score = (a + b) - c
elif b == c:
    score = (b + c) - a
elif a == c:
    score = (a + c) - b
else:
    score = 0
print(score)
