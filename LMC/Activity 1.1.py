#Joe Young 06/10/2016 Re-write of Mnemonics to high level code.

"""
        LDA ONE
        STA COUNT
        OUT
LOOPTOP LDA COUNT 
        ADD ONE 
        OUT 
        STA COUNT 
        SUB TEN 
        BRP ENDLOOP
        BRA LOOPTOP 
ENDLOOP HLT
ONE     DAT 1
TEN     DAT 10
COUNT   DAT 0

"""

loop = True
one = 1
ten = 10
count = 0

while loop: 
    count += 1
    print(count)
    if count - ten == 0:
        loop = False