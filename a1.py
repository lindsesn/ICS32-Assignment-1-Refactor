# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lindsey Nguyen
# lindsesn@uci.edu
# lindsesn

from os import listdir, walk, remove, stat
from io import UnsupportedOperation

def L_command():
    try:
        L_list = listdir(command_list[1])
        for file in L_list:
            print(file)
        # with open(f"{command_list[1]}", "r") as my_dir:
        #     for file in my_dir:
        #         print(file)
    except FileNotFoundError:
        print("File not found, please try again")
    except PermissionError:
        print("Permission was denied, please try again")


def LR_command():
    for (root, dirs, files) in walk(command_list[1], topdown=True):
        print(root)
        for i in files:
            print(i)


def RF_command():
    for (root, dirs, files) in walk(command_list[1], topdown=True):
        for i in files:
            print(i)


def RS_command():
   for (root, dirs, files) in walk(command_list[1], topdown=True):
        for i in files:
            if command_list[4] in i:
                print(i)


def RE_command():
   for (root, dirs, files) in walk(command_list[1], topdown=True):
        for i in files:
            ext_len = 0 - len(command_list[4])
            if i[ext_len:] == command_list[4]:
                print(i)

def F_command():
    F_list = listdir(command_list[1])
    for file in F_list:
        try:
            subdirect = listdir(command_list[1] + "\\" + file)
        except NotADirectoryError:
            print(file)
        else:
            for file2 in subdirect:
                print(file2)


def S_command():
    S_list = listdir(command_list[1])
    for file in S_list:
        if command_list[3] in file:
            print(file)


def E_command():
    E_list = listdir(command_list[1])
    for file in E_list:
        file_str = list(file)
        ext_len = 0 - len(command_list[3])
        if "".join(file_str[ext_len:]) == command_list[3]:
            print(file)


def CN_command():
    if "." not in command_list[3]:
        with open(f'{command_list[3]}.dsu', "w") as my_file:
            try:    
                for line in my_file:
                    print(line)
            except UnsupportedOperation:
                pass
            except NameError:
                pa
        print(f"{command_list[3]}.dsu created")
    else:
        ext_dot = command_list[3].index('.')
        ext = command_list[3][ext_dot:]
        if ext in command_list[3]:
            with open(f'{command_list[3]}', "w") as my_file:
                try:    
                    for line in my_file:
                        print(line)
                except UnsupportedOperation: # reason why "import io" was placed in line 2
                    pass
                except NameError:
                    pass
            print(f"{command_list[3]} created")


def del_command():
    try:
        remove(command_list[1])
    except FileNotFoundError:
        print("File not found, please try again")
    except PermissionError:
        print("Permission denied, please try again")
    else: 
        print(f"{command_list[1]} deleted")


def R_command():
    req_ext = ".dsu"
    try:
        if req_ext not in command_list[1][-4:]:
            print("Error: please use a .dsu file")
        elif stat(command_list[1]).st_size == 0:
            print("EMPTY")
    except FileNotFoundError:
        print("File not found, please try again")
    else:
        with open(f'{command_list[1]}') as my_file:
            for line in my_file:
                print(line)


def main():
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

if __name__ == "__main__":
    not_end = True
    while not_end is True:
        command = input("Enter a command: ")
        command_list = command.split()
        if command_list[0] == "Q":
            break
        else:
            main()
