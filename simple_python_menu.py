#!/usr/bin/env python3
# simple_python_menu.py
# Last updated 202003141015

# Create array of menu items to select from
menu_items = ["First Menu Item"]

# Define the menu items
def get_menu_item(menu_items):
    print("Menu:\n")
    for i in range(len(menu_items)):
        print((i+1), "-", menu_items[i])
    print("Q - Quit\n")
    menu_selection = input("Selection: ")
    print()
    return menu_selection

# Define the main loop
def main(menu_items):
    print("")
    quit_flag = "N"
    while quit_flag == "N":
        selection = get_menu_item(menu_items)
        if selection == "1":
            function_1()
        if selection.upper() == "Q":
            quit_flag = "Y"

# Define function
def function_1():
    print("Hello World.\n")
    return

# If this program is started on it's own, run the main() function
if __name__ == "__main__":
    main(menu_items)
    print("Good bye.\n")
