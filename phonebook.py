def load_contacts():
    contacts_list = []

    with open('phonebook.txt') as f:
        for line in f.readlines():
            columns = line.split()

            name = columns[0]
            location = columns[1]
            number = columns [2]
        
            contact = {
                'name': name , 
                'location': location,
                'number': number, 
            }
            contacts_list.append(cotanct)

        return contacts_list

contacts = load_contacts()

while True:
    command = input('availble commands, list or add ')


    # add_contact = input('to add a contact type: name, location, and phone number')

    if command == 'list':
        for contact in contacts:
            print(f" name: {contact['name']} location: {contact['location']} number: {contact['number']}")
    
    
    elif command == 'add':
        name = input("Enter a name: ")
        number = input("Enter a number: ")
        location = input("Enter a location: ")
        new_contact = {
            'name': name , 
            'location': location,
            'number': number, 
        }
        contacts.append(new_contact)
        
        #me.update(contacts)?????????????
        # got to the docs thing for classes and go over dictionaries 
      
        
       
    #still not done sad day 


           
    #    with open('phonebook.txt', 'a') as f:
        
        
        # create a dictionary from name, number, location
        # need to append a new contact to contacts 
        # save to contacts to file 
    
    else:
        print('invalid')
        
print(contacts)





# for contact in contacts_list:
    # print(f" name: {contact['name']} location: {contact['location']} number: {contact['number']}")
  # the above line was version 1 ^^^^^^^


# def phone (path):
#     contacts = []
    
    
#     with open(path, 'r') as order_file:
        
#         for line in f.readlines():
            
#             contacts = line.rstrip().split(',')

#             # Get our data from the columns
#             name  = contacts[name]
#             number = int(contacts[number])
#             location = contacts[location]

#             # Create a human readable dictionary
#             item = {
#                 'item': item_name,
#                 'quantity': quantity,
#             }
#             orders.append(item)

#     return orders