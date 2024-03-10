'''
Contains EventHandler class
Will run methods from DirectoryFunctions in a1p1_refactor_ui.py as needed
'''

class EventHandler():
    '''
    Handles commands from main() in a1p1_refactor module
    '''
    def __init__(self):
        pass

    if command_list[0] == "L":
        if len(command_list) == 2:
            L_command()
        elif len(command_list) == 4 and command_list[2] == "-r" and command_list[3] == "-f":
            RF_command()
        elif len(command_list) == 5 and command_list[2] == "-r" and command_list[3] == "-s":
            RS_command()
        elif len(command_list) == 5 and command_list[2] == "-r" and command_list[3] == "-e":
            RE_command()
        elif len(command_list) == 3 and command_list[2] == "-r":
            LR_command()
        elif len(command_list) == 3 and command_list[2] == "-f":
            F_command()
        elif len(command_list) == 4 and command_list [2] == "-s":
            S_command()
        elif len(command_list) == 4 and command_list [2] == "-e":
            E_command()
    elif command_list[0] == "C":
        if len(command_list) == 4 and command_list[2] == "-n":
            CN_command()
        else:
            print("Invalid command, please try again")
    elif command_list[0] == "D":
        del_command()
    elif command_list[0] == "R":
        R_command()