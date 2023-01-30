def main_menu():
    print('Main menu')
    menu_list = ['a   -  Show all contacts',
                 'o   -  Open file',
                 's   -  Save file',
                 'n   -  Create contact',
                 'f   -  Find contact',
                 'c   -  Change contact',
                 'd   -  Delete contact',
                 'q   -  Quit'
                 ]
    for item in menu_list:
        print(item)
    user_input = input('Enter the command :>')
    return user_input

def show_all(db):
    if len(db) == 0:
        print("Contact book is not loaded")
    for i in range(len(db)):
        print(db[i])

def show_msg(msg):
    print(msg)

def ask_data(msg):
    return input(msg)

def ask_filepath():
    return input("Enter the path of file :>")

def ask_name():
    return input("Enter the name: ")

def ask_surname():
    return input("Enter the surname: ")

def ask_phone():
    return input("Enter the phone number: ")

def ask_comment():
    return input("Enter the comment: ")

def ask_id():
    return int(input("Enter the ID: "))

def find_menu():
    find_menu = ['n   -   Find by name',
                 's   -   Find by surname',
                 'p   -   Find by phone ',
                 'c   -   Find by comment',
                 'r   -   Return to main menu']

    for item in find_menu:
        print(item)
    user_input = input('Enter the command :>')
    return user_input

def change_menu():
    find_menu = ['n   -   name',
                 's   -   surname',
                 'p   -   phone ',
                 'c   -   comment',
                 'r   -   Return to main menu']
    print("What field do you want to change?")
    for item in find_menu:
        print(item)
    return input('Enter the command :>')

def delete_menu():
    delete_menu = ['y   -   yes',
                   'n   -   no']
    print("Are you sure you want to delete a contact?")
    for item in delete_menu:
        print(item)
    return input('Enter the command :>')    