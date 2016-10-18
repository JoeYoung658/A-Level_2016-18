"""
Joe Young
V.1
Little Man Computer

"""
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
    pass

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

if __name__ == "__main__":
    main()