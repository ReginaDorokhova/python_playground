def main_menu():
    print('Main menu')
    menu_list = ['Show all contacts',
                 'Open file',
                 'Save file',
                 'Create contact',
                 'Change contact',
                 'Delete contact',
                 'Quit'
                 ]
    for i in range(len(menu_list)):
        print("      %i   -   %s" %(i, menu_list[i]))
    user_input = int(input('Enter the command :>'))
    return user_input

def show_all(db):
    print("show_all")
    if len(db) == 0:
        print("Contact book is not loaded")
    for i in range(len(db)):
        print(db[i])

def ask_filepath():
    return input("Enter the path of file :>")