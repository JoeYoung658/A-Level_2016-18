"""
Joe Young
V.2
Little Man Computer

- Bugs
    - Fix Assembly reading
    - Add branching
       
"""
import sys
#RAM = ["000" for i in range(100)]
#Populates RAM dictonary with 99 addresses
##for i in range(100):
##    RAM[i] = 0

#Checks RAM dictonary, then replaces with values given
##def update_RAM_instructions(key_to_find, instruction):  
##    for key in RAM.keys():
##        if key == key_to_find:
##            RAM[key] = instruction
##
def mnemonics_file_read(filename):
    """Reads the assembly file, places each mnemonic in a list.
    """
    #counter = 0
    #RAM = ["000" for i in range(100)]
    #print(RAM)
    mnemonic_list = []
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                mnemonic_list.append(word.upper())
##                RAM[counter] = word
##                counter += 1 
                
    return mnemonic_list


def mnemonics_to_instructions(mnemonic_list):
    """Converts mnemonics into instructions to be put into ram
    """
    #Does not convert all mnemonics at this moment in time.
    #print(mnemonic_list)
    RAM = ["000" for i in range(100)]
    instruction_list = []
    counter = 0
    while len(mnemonic_list) != 0:
        if "INP" == mnemonic_list[0]:
            #instruction_list.append("901")
            RAM[counter] = "901"
            counter += 1
            mnemonic_list.pop(0)
            
        elif "STA" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            try:
                RAM_adress = int(mnemonic_list[0])
                #instruction_list.append(int('3%d' % (RAM_adress)))
                #instruction_list.append("3")
                #RAM[counter] = "3"
                #counter += 1
                #instruction_list.append(mnemonic_list[0])
                RAM[counter] = (str('3%d' % (RAM_adress)))
                counter += 1
                mnemonic_list.pop(0)
            except ValueError:
                print("Error: Missing RAM address")
                break   
        elif "ADD" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            try:
                RAM_adress = int(mnemonic_list[0])
                #instruction_list.append(int('1%d' % (RAM_adress)))
                #instruction_list.append("1")
                #RAM[counter] = "1"
                #counter += 1
                #instruction_list.append(mnemonic_list[0])
                RAM[counter] = (str('1%d' % (RAM_adress)))
                counter += 1
                mnemonic_list.pop(0)
            except ValueError:
                print("Error: Missing RAM addresBs")
                break
        elif "SUB" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            try:
                RAM_adress = int(mnemonic_list[0])
                #instruction_list.append(int('1%d' % (RAM_adress)))
                #instruction_list.append("1")
                #RAM[counter] = "1"
                #counter += 1
                #instruction_list.append(mnemonic_list[0])
                RAM[counter] = (str('2%d' % (RAM_adress)))
                counter += 1
                mnemonic_list.pop(0)
            except ValueError:
                print("Error: Missing RAM addresBs")
                break
        elif "OUT" == mnemonic_list[0]:
            #instruction_list.append("902")
            RAM[counter] = "902"
            counter += 1
            mnemonic_list.pop(0)
        elif "HLT" == mnemonic_list[0]:
            #instruction_list.append("000")
            mnemonic_list.pop(0)      
        else:
            print("No mnemonics found.")
    # print(mnemonic_list)
    # print(instruction_list)
    return RAM 
    

def ALU(accumulator, value, operator):
    """Deals with the logical operations
    """
    if operator == "+":
        print("Values have been added together")
        #return valuea + valueb
        accumulator = accumulator + value
    elif operator == "-":
        print("Values have been taken away from each other")
        #return valuea - valueb
        accumulator = accumulator - value
    elif operator == "/":
        print("Values have been divided")
        #return valuea / valueb
        accumulator = accumulator / value
    else:
        return "Error"
    return accumulator


def control_unit(RAM):
    accumulator = ""
    program_counter = 0
    counter = 0
    print("Program Counter =", program_counter)
    #print(instructions)
    #while (len(instructions)) != 0:
    while (RAM[counter] != "000"):
        if RAM[counter] == "901":
            #instructions.pop(0)
            counter += 1
            user_input = float(input("Please input a number!"))
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter][0] == "3":
            #instructions.pop(0)
            #counter += 1
            print("Stores user input ("+ str(user_input) + ") to ram address" + RAM[counter][1:]+";")
            #update_RAM_instructions(int(instructions[counter]), user_input)
            RAM[int(RAM[counter][1:])] = user_input
            #instructions.pop(0)
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter][0] == "1":
            #add
            #instructions.pop(0)
            #counter += 1
            if (accumulator == ""):
                #print (str(RAM[int(instructions[0])])+ "a")
                math = ALU(RAM[int(RAM[counter][1:])], user_input, "+")
                
            else:
                #print (str(RAM[int(instructions[0])]) + "b")
                math = ALU(RAM[int(RAM[counter][1:])], accumulator, "+")
            accumulator = math
            print ("The value in the accumulator is, " + str(accumulator))
            #instructions.pop(0)
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter][0] == "2":
            #add
            #instructions.pop(0)
            #counter += 1
            if (accumulator == ""):
                #print (str(RAM[int(instructions[0])])+ "a")
                math = ALU(RAM[int(RAM[counter][1:])], user_input, "-")
                
            else:
                #print (str(RAM[int(instructions[0])]) + "b")
                math = ALU(RAM[int(RAM[counter][1:])], accumulator, "-")
            accumulator = math
            print ("The value in the accumulator is, ", accumulator)
            #instructions.pop(0)
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter] == "902":
            #instructions.pop(0)
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
            print("The output is, ", accumulator)
        #print(RAM[counter][1:])
        #elif instructions[counter] == "000":
            #instructions.pop(0)
    return "Done"

def main():
    """Deals User interface
    """
    print("-------------------------------------------\n            Little Man Computer\n-------------------------------------------")
    mnemonic_list = mnemonics_file_read(sys.path[0]+'\\Extra\\Assembly.txt')
    print(mnemonic_list)
    RAM = mnemonics_to_instructions(mnemonic_list)
    print(RAM)
    control = control_unit(RAM)
    #if control == "Done":
    #    print("Thank you for using Little Man Computer Python Edition")
    #else:
    #    main()
    
    # update_RAM_instructions(int("99"), 6)
    # math = ALU(int(RAM[int("99")]), 7, "+")
    # print(math)


if __name__ == "__main__":
    main()
