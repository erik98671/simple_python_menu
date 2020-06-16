#!/usr/bin/env python3
# simple_python_menu.py
# Last Updated 202006161300

# Define the main loop
def main(menu_items):
    quit_flag = "N"
    while quit_flag == "N":
    
        selection = get_menu_item(menu_items)
        
        if selection == "1":
            function_1()
            
        if selection.upper() == "Q":
            quit_flag = "Y"

# Define the menu items
def get_menu_item(menu_items):
     
    print("Menu:\n")
    
    for item in menu_items: 
        print(menu_items.index(item)+1, "-", item)

    print("Q - Quit\n")

    menu_selection = input("Selection: ")
    print()
    
    return menu_selection

# Define function_1()
def function_1():
    return

# If this program starts on its own, run the main() function.
if __name__ == "__main__":
    
    # Create list of menu items to select from
    menu_items = ["First Menu Item"]

    # Run the main program
    main(menu_items)
