#!/usr/bin/env python3
# simple_python_menu.py
# Last Updated 202011071200

# Define the Simple_Menu class
class Simple_Menu:    
    def __init__(self, menu_items):
        self.menu_items = menu_items

    def get_menu_item(self):
        print("Menu: \n")
        for item in self.menu_items: 
            print(self.menu_items.index(item)+1, "-", item)
        print("Q - Quit \n")
        menu_selection = input("Selection: ")
        print()
        return menu_selection

    def main(self):
        quit_flag = "N"
        while quit_flag == "N":
            selection = self.get_menu_item()
            if selection == "1":
                self.function_1()
            if selection.upper() == "Q":
                quit_flag = "Y"

    def function_1(self):
        print("Hello.")

if __name__ == "__main__":
    menu_items = ["Function 1",
                  "Function 2"]
    
    menu = Simple_Menu(menu_items)
    menu.main()
    

