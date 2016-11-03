"""
Joe Young
V.2
Little Man Computer

- Bugs
    - Fix Assembly reading
    - Add branching
       
"""
import sys

def mnemonics_file_read(filename):
    """Reads the assembly file, places each mnemonic in a list.
    """
    
    mnemonic_list = []
    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                mnemonic_list.append(word.upper())

                
    return mnemonic_list


def mnemonics_to_instructions(mnemonic_list):
    """Converts mnemonics into instructions to be put into ram
    """
    
    RAM = ["000" for i in range(100)]
    instruction_list = []
    counter = 0
    while len(mnemonic_list) != 0:
        if "INP" == mnemonic_list[0]:
            
            RAM[counter] = "901"
            counter += 1
            mnemonic_list.pop(0)
            
        elif "STA" == mnemonic_list[0]:
            mnemonic_list.pop(0)
            try:
                RAM_adress = int(mnemonic_list[0])
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
                RAM[counter] = (str('2%d' % (RAM_adress)))
                counter += 1
                mnemonic_list.pop(0)
            except ValueError:
                print("Error: Missing RAM addresBs")
                break
        elif "OUT" == mnemonic_list[0]:
            RAM[counter] = "902"
            counter += 1
            mnemonic_list.pop(0)
        elif "HLT" == mnemonic_list[0]:
            mnemonic_list.pop(0)      
        else:
            print("No mnemonics found.")
    return RAM 
    

def ALU(accumulator, value, operator):
    """Deals with the logical operations
    """
    if operator == "+":
        print("Values have been added together")
        accumulator = accumulator + value
    elif operator == "-":
        print("Values have been taken away from each other")
        accumulator = accumulator - value
    elif operator == "/":
        print("Values have been divided")
        accumulator = accumulator / value
    else:
        return "Error"
    return accumulator


def control_unit(RAM):
    accumulator = ""
    program_counter = 0
    counter = 0
    print("Program Counter =", program_counter)
    while (RAM[counter] != "000"):
        if RAM[counter] == "901":

            counter += 1
            user_input = float(input("Please input a number!"))
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter][0] == "3":
            print("Stores user input ("+ str(user_input) + ") to ram address" + RAM[counter][1:]+";")
            RAM[int(RAM[counter][1:])] = user_input
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter][0] == "1":
            if (accumulator == ""):
                math = ALU(RAM[int(RAM[counter][1:])], user_input, "+")
                
            else:
                math = ALU(RAM[int(RAM[counter][1:])], accumulator, "+")
            accumulator = math
            print ("The value in the accumulator is, " + str(accumulator))
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter][0] == "2":
            if (accumulator == ""):
                math = ALU(RAM[int(RAM[counter][1:])], user_input, "-")
                
            else:
                math = ALU(RAM[int(RAM[counter][1:])], accumulator, "-")
            accumulator = math
            print ("The value in the accumulator is, ", accumulator)
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
        elif RAM[counter] == "902":
            counter += 1
            program_counter += 1
            print("Program Counter =", program_counter)
            print("The output is, ", accumulator)
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

if __name__ == "__main__":
    main()
