"""
Joe Young
V.1
Little Man Computer

"""
from time import sleep

#Populates RAM dictonary with 99 addresses
RAM = {}
for i in range(100):
    RAM[i] = 0

#Checks RAM dictonary, then replaces with values given
def update_RAM_instructions(key_to_find, instruction):
    for key in RAM.keys():
        if key == key_to_find:
            RAM[key] = definition

sleep(50)


