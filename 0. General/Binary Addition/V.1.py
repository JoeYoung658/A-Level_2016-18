"""
Contains logical errors

Does not take into account overflow errors

Logic for denary to binary flawed
"""

waiting_line = [128,64,32,16,8,4,2,1]

def binary_to_denary(a):
    sum = 0
    for i in range(len(a)):
        if a[i] == "1":
            sum += waiting_line[i]
    return sum

def denary_to_binary(a):
    binary = ""
    for i in waiting_line:
        if (a-i) >= 0:
            a -= i
            binary += "1"
        else:
            binary += "0"
    return binary

def binary_sum(a,b):
    asum = binary_to_denary(a)
    bsum = binary_to_denary(b)
    print(denary_to_binary(asum + bsum))

binary_sum("00000010","00000001")

print(denary_to_binary(127))