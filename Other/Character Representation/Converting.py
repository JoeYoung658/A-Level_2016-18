

List = ["01001000", "01100101", "01101100", "01101100", "01101111"]



for i in range(len(List)):
    ordinal = int(List[i], 2)

    charcter = chr(ordinal)

    print(charcter)


List2 = "00100000", "01010111", "01101111", "01110010", "01101100", "01100100", "00100001"

for i in range(len(List2)):
    ordinal = int(List2[i], 2)
    charcter = chr(ordinal)

    print(charcter)

BigList = ["01001000", "01100101", "01101100", "01101100", "01101111", "00100000", "01010111", "01101111", "01110010", "01101100", "01100100", "00100001"]

text = ""
for byte in BigList:
    text += chr(int(byte,2 ))
print(text)



print("------------------------------------------")
print("C")
test = (ord("C")+1)
print(chr(test))
