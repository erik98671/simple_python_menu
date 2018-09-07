# Create array of menu items to select from
menu_items = ['First Menu Item']

# Define the menu items
def get_menu_item():
    print('Menu:')
    print()
    for i in range(len(menu_items)):
        print(str(i + 1) + ' - ' + menu_items[i])
    print('Q - Quit')
    print()
    menu_selection = input('Selection: ')
    print()
    return menu_selection

# Define the main loop
def main_loop():
    quit_flag = 'N'
    while quit_flag == 'N':
        selection = get_menu_item()
        if selection == '1':
            function_1()
        if selection.upper() == 'Q':
            quit_flag = 'Y'

# Define function(s)
def function_1():
    return

# Run the main loop
main_loop()
