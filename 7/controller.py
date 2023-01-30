from model import ContactBook
import view

class Controller:
    def __init__(self):
        self.model = ContactBook()

    def input_handler(self, inp):
        match inp:
            case 'a':
                view.show_all(self.model.get_data())
            case 'o':
                path = view.ask_filepath()
                if self.model.read_db(path):
                    view.show_msg("The contact book loaded")
                else:
                    view.show_msg("Error: the contact book is not loaded")
            case 's':
                path = view.ask_filepath()
                if len(path) > 0 :
                    self.model.save_file(path)
            case 'n':
                contact_data = []
                name = view.ask_name()
                contact_data.append(name)
                contact_data.append(view.ask_surname())
                contact_data.append(view.ask_phone())
                contact_data.append(view.ask_comment())
                self.model.addContact(contact_data)
            case 'f':
                find_inp = view.find_menu()
                self.find_menu_handler(find_inp)
            case 'c':
                id = view.ask_id()
                contact_info = self.model.get_data_by_id(id)
                if len(contact_info) > 0:
                    view.show_msg(contact_info)
                    self.change_menu_handler(view.change_menu(), id)
                else:
                    view.show_msg('The contact with id = {id} does not exist')
            case 'd':
                id = view.ask_id()
                contact_info = self.model.get_data_by_id(id)
                if len(contact_info) > 0:
                    view.show_msg(contact_info)
                    self.delete_menu_handler(view.delete_menu(), id)
                else:
                    view.show_msg("The contact with id = %i doesn't exist", id)
            case "q":
                quit()
            case _:
                view.show_msg("Incorrect command")

    def find_menu_handler(self, find_inp):
        match find_inp:
            case 'n':
                name = view.ask_name()
                view.show_all(self.model.find_contact_by_name(name))
            case 's':
                surname = view.ask_surname()
                view.show_all(self.model.find_contact_by_surname(surname))
            case 'p':
                phone = view.ask_phone()
                view.show_all(self.model.find_contact_by_phone(phone))
            case 'c':
                phone = view.ask_comment()
                view.show_all(self.model.find_contact_by_comm)
            case 'r':
                self.input_handler(view.main_menu())
            case _:
                view.show_msg("Incorrect command")

    def change_menu_handler(self, change_inp, id):
        match change_inp:
            case 'n':
                name = view.ask_name()
                self.model.change_contact_name(id, name)
            case 's':
                surname = view.ask_surname()
                self.model.change_contact_surname(id, surname)
            case 'p':
                phone = view.ask_phone()
                self.model.change_contact_phone(id, phone)
            case 'c':
                comment = view.ask_comment()
                self.model.change_contact_comment(id, comment)
            case 'r':
                self.input_handler(view.main_menu())
            case _:
                view.show_msg("Incorrect command")
    
    def delete_menu_handler(self, inp, id):
          match inp:
            case 'y':
                self.model.remove_contact(id)
            case 'n':
                self.model.remove_contact(id)
            case _:
                view.show_msg("Incorrect command")      


    def start(self):
        while True:
            self.input_handler(view.main_menu())