from model import ContactBook
import view


    # menu_list = ['Show all contacts',
    #              'Open file',
    #              'Save file',
    #              'Create contact',
    #              'Change contact',
    #              'Delete contact',
    #              'Quit'
    #              ]
#model.read_db("dataset.txt")
model = ContactBook()

def input_handler(inp):
    match inp:
        case 0:
            view.show_all(model.get_data())
        case 1:
            path = view.ask_filepath()
            model.read_db(path)

        case 6: 
            quit()
        case _: 
            print("Incorrect command")


def start():
    while True:
        input_handler(view.main_menu())