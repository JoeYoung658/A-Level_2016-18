#Joe Young 06/10/2016 Re-write of Mnemonics to high level code.


loop = True
one = 1
ten = 10
count = 0

while loop:
    count += 1
    print(count)
    if count - ten == 0:
        loop = False