"""
Joe Young
V.1
Little Man Computer

"""
import sys
import math
#Populates RAM dictonary with 99 addresses
RAM = {}
for i in range(100):
    RAM[i] = 0

#Checks RAM dictonary, then replaces with values given
def update_RAM_instructions(key_to_find, instruction):
    for key in RAM.keys():
        if key == key_to_find:
            RAM[key] = definition

def mnemonics_to_instruction(filename):
    """Converts LDA etc into instruction, which can then be stored within the RAM
    """
    
    
    instruction_list = []
    mnemonic_list = []
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                mnemonic_list.append(word)   
    while len(mnemonic_list) != 0:
        if "INP" == mnemonic_list[0]:
            instruction_list.append(901)
            mnemonic_list.pop(0)        
        elif "STA" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            RAM_adress = int(mnemonic_list[0]) 
            if type(RAM_adress) == int:
                instruction_list.append(int('3%d' % (RAM_adress)))  
                mnemonic_list.pop(0)     
            else:
                print("Error: Missing RAM address")
                break
        elif "ADD" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            RAM_adress = int(mnemonic_list[0])      
            if type(RAM_adress) == int:
                instruction_list.append(int('1%d' % (RAM_adress)))     
                mnemonic_list.pop(0)           
            else:
                print("Error: Missing RAM address")
                break
        elif "OUT" == mnemonic_list[0]:
            instruction_list.append(902)
            mnemonic_list.pop(0)  
        elif "HLT" == mnemonic_list[0]:
            instruction_list.append(000)
            mnemonic_list.pop(0)  
        else:
            print("No mnemonics found.")
           
    
    print(mnemonic_list)
    print(instruction_list)
    return instruction_list 
    

def accumulator():
    """Deals with the logical operations
    """
    
    pass


def program_counter():
    """ Contains the address for the next instruction to be executed.
    """
    
    pass

def memory_unit():
    """Deals with fetching/storing instructions from RAM
    """
    pass

def user_input():
    """Deals with user_input.
    """
    pass

def main():
    """Deals User interface
    """
    instruction_list = mnemonics_to_instruction(sys.path[0]+'\\Extra\\Assembly.txt')
    #print(instruction_list)

if __name__ == "__main__":
    main()