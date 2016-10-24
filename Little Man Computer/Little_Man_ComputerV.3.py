"""
Joe Young
V.2
Little Man Computer

- Bugs
        - When user inputs nothing/wrong RAM adress,, takes sees as zero
        - Add try/except onto inputs to avoid input Error
"""
import sys

#Populates RAM dictonary with 99 addresses
RAM = {}
for i in range(100):
    RAM[i] = 0

#Checks RAM dictonary, then replaces with values given
def update_RAM_instructions(key_to_find, instruction):
    for key in RAM.keys():
        if key == key_to_find:
            RAM[key] = instruction

def mnemonics_file_read(filename):
    """Reads the assembly file, places each mnemonic in a list.
    """
    mnemonic_list = []
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                mnemonic_list.append(word)
    return mnemonic_list


def mnemonics_to_instructions(mnemonic_list):
    """Converts mnemonics into instructions to be put into ram
    """
    #Does not convert all mnemonics at this moment in time.
    #print(mnemonic_list)
    instruction_list = []
    while len(mnemonic_list) != 0:
        if "INP" == mnemonic_list[0]:
            instruction_list.append("901")
            mnemonic_list.pop(0)
            
        elif "STA" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            try:
                #RAM_adress = int(mnemonic_list[0])
                #instruction_list.append(int('3%d' % (RAM_adress)))
                instruction_list.append("3")
                instruction_list.append(mnemonic_list[0])
                mnemonic_list.pop(0)
            except ValueError:
                print("Error: Missing RAM address")
                break   
        elif "ADD" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            try:
                #RAM_adress = int(mnemonic_list[0])
                #instruction_list.append(int('1%d' % (RAM_adress)))
                instruction_list.append("1")
                instruction_list.append(mnemonic_list[0])
                mnemonic_list.pop(0)
            except ValueError:
                print("Error: Missing RAM address")
                break
        elif "OUT" == mnemonic_list[0]:
            instruction_list.append("902")
            mnemonic_list.pop(0)
        elif "HLT" == mnemonic_list[0]:
            instruction_list.append("000")
            mnemonic_list.pop(0)      
        else:
            print("No mnemonics found.")
    # print(mnemonic_list)
    # print(instruction_list)
    return instruction_list 
    

def ALU(valuea, valueb, operator):
    """Deals with the logical operations
    """
    
    if operator == "+":
        return valuea + valueb
    elif operator == "-":
        return valuea - valueb
    elif operator == "*":
        return valuea * valueb
    elif operator == "/":
        return valuea / valueb
    else:
        return "Error"


def control_unit(instructions):
    print(instructions)
    while (len(instructions)) != 0:
        if instructions[0] == "901":
            instructions.pop(0)
            user_input = float(input("Please input a number!"))
        elif instructions[0] == "3":
            instructions.pop(0)
            update_RAM_instructions(int(instructions[0]), user_input)
            instructions.pop(0)
        elif instructions[0] == "1":
            #add
            instructions.pop(0)
            math = ALU(RAM[int(instructions[0])], user_input, "+")
            instructions.pop(0)
        elif instructions[0] == "902":
            instructions.pop(0)
            print(math)
        elif instructions[0] == "000":
            instructions.pop(0)
    return "Done"

def main():
    """Deals User interface
    """
    print("-------------------------------------------\n            Little Man Computer\n-------------------------------------------")
    mnemonic_list = mnemonics_file_read(sys.path[0]+'\\Extra\\Assembly.txt')
    instructions = mnemonics_to_instructions(mnemonic_list)
    control = control_unit(instructions)
    if control == "Done":
        print("Thank you for using Little Man Computer Python Edition")
    else:
        main()
    
    # update_RAM_instructions(int("99"), 6)
    # math = ALU(int(RAM[int("99")]), 7, "+")
    # print(math)


if __name__ == "__main__":
    main()