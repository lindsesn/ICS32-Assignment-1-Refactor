'''
# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Lindsey Nguyen
# lindsesn@uci.edu
# lindsesn
'''

import a1p1_event_handler as eh
from a1p1_event_handler import EventHandler

def main():
    '''
    takes commands from user
    '''
    not_end = True
    while not_end is True:
        command = input("Enter a command: ")
        command_list = command.split()

        if command_list[0] == "Q":
            break

if __name__ == "__main__":
    main()
