import sys

class Contact:
    def __init__(self, data, id):
        self._id = id
        self._name = data[0]
        self._lastname = data[1]
        self._phone = data[2]
        self._comment = data[3]
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name

    def getPhone(self):
        return self._phone

    def __repr__(self):
        return f"({self._id}. {self._name} {self._lastname} {self._phone} {self._comment})"



class ContactBook:
    contact_list = []
    def __init__(self):
        self.contact_list = []

    def addContact(self, data):
        contact_id = len(self.contact_list)
        contact = Contact(data, id)
        self.contact_list.append(contact)

    def read_db(self, path):
        success = True 
        try:
            with open('7/dataset.txt', 'r', encoding='UTF-8') as file:
                my_list = file.readlines()
                curId = 0 
                for line in my_list:
                    line = line.strip().split(";")
                    if len(line == 4):
                        contact = Contact(line, curId)
                        self.contact_list.append(contact)
                        urId = curId + 1
                        print(line)
                    else:
                        success = False
        except:
            success = False



    def get_data(self):
        data = []
        for contact in self.contact_list:
            data.append(contact.__repr__())
        return data

   

