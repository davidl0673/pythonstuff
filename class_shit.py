# contacts = []

class Contact:
    def __init__(self, name, phone, location):
        self.name = name
        self.phone = phone

        if ',' in location:
            raise TypeError("Invalid location: no commas allowed!")
        self.location = location

    def to_str(self):
        return ','.join([self.name, self.phone, self.location])

    @staticmethod
    def from_str(string):
        rows = string.split(',')
        name = rows[0]
        phone = rows[1]
        location = rows[2]
        return Contact(rows[0], rows[1], rows[2])

class ContactList:
    def __init__(self):
        self.contacts = list()
    
    def add(self, contact):
        self.contacts.append(contact)

    def remove(self, contact):
        self.contacts.remove(contact)

    def convert_to_file(self):
        contact_file = str() # ''
        for contact in self.contacts:
            contact_file += contact.to_str() + "\n"
        return contact_file
    
    def write(self, path):
        with open(path, 'w') as f:
            f.write(self.convert_to_file())

    def read(self, path):
        with open(path, 'r') as f:
            for line in f:
                contact = Contact.from_str(line)
                self.contacts.append(contact)
    
# zack = Contact(name='Zack', phone='666-666-6661', location='Hell MI')
# mike = Contact(name='Mike', phone='392019402913', location='Portland MI')

contact_list = ContactList()
contact_list.read('hello.txt')
print(contact_list.contacts)
# contact_list.add(zack)
# contact_list.add(mike)

# contact_list.write('hello.txt')