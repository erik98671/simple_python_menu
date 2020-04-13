#!/usr/bin/env python3
# simple_python_menu.py
# Last Updated 202004130900

# Create array of menu items to select from
menu_items = ["First Menu Item"]

# Define the main loop
def main():
    quit_flag = "N"
    while quit_flag == "N":
        selection = get_menu_item()
        if selection == "1":
            function_1()
        if selection.upper() == "Q":
            quit_flag = "Y"

# Define the menu items
def get_menu_item():
    print("Menu:\n")
    for i in range(len(menu_items)):
        print((i+1), "-", menu_items[i])
    print("Q - Quit\n")
    menu_selection = input("Selection: ")
    print()
    return menu_selection

# Define function_1()
def function_1():
    return

# If this program is started on it's own, run the main() function.
if __name__ == "__main__":
    main()
