import sys

class Contact:
    def __init__(self, data):
        self._name = data[0]
        self._lastname = data[1]
        self._phone = data[2]
        self._comment = data[3]

    def __repr__(self):
        return f"{self._name} {self._lastname} {self._phone} {self._comment}"

    def repr_in_custom_format(self):
        return f"{self._name};{self._lastname};{self._phone};{self._comment}\n"

class ContactBook:
    def __init__(self):
        self.contact_dict = {}
        self.max_id = 0

    def addContact(self, data):
        self.max_id = self.max_id + 1
        contact = Contact(data)
        self.contact_dict[self.max_id] = contact

    def read_db(self, path):
        success = True 
        try:
            with open(path, 'r', encoding='UTF-8') as file:
                self.contact_dict.clear()
                my_list = file.readlines()
                for line in my_list:
                    line = line.strip().split(";")
                    if len(line) == 4:
                        self.addContact(line)
                    else:
                        success = False
                file.close()
        except Exception as e:
            success = False
        return success

    def save_file(self, path):
        with open(path, 'w', encoding='UTF-8') as file:
            for contact in self.contact_dict.values():
                file.writelines(contact.repr_in_custom_format())
            file.close()         

    def get_data_repr(self, dict):
        data = []
        for id in dict.keys():
            line = str(id) + ". " + dict[id].__repr__()
            data.append(line)
        return data

    def get_data(self):
        data = self.get_data_repr(self.contact_dict)
        return data

    def find_contact_by_name(self, name):
        filter_dict = {id: contact for id, contact in self.contact_dict.items() if contact._name == name}
        return self.get_data_repr(filter_dict)

    def find_contact_by_surname(self, surname):
        filter_dict = {id: contact for id, contact in self.contact_dict.items() if contact._surname == surname}
        return self.get_data_repr(filter_dict)

    def find_contact_by_phone(self, phone):
        filter_dict = {id: contact for id, contact in self.contact_dict.items() if contact._phone == phone}
        return self.get_data_repr(filter_dict)
    
    def find_contact_by_comment(self, comment):
        filter_dict = {id: contact for id, contact in self.contact_dict.items() if contact._comment == comment}
        return self.get_data_repr(filter_dict)

    def change_contact_name(self, id, name):
        self.contact_dict[id]._name = name
    
    def change_contact_surname(self, id, surname):
        self.contact_dict[id]._surname = surname
    
    def change_contact_phone(self, id, phone):
        self.contact_dict[id]._phone = phone

    def change_contact_comment(self, id, comment):
        self.contact_dict[id]._comment = comment

    def get_data_by_id(self, id):
        data = ''
        if id in self.contact_dict:
            data = self.contact_dict[id].__repr__()
        return data
    
    def remove_contact(self, id):
        self.contact_dict.pop(id)
   

