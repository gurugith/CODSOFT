def add_contact(name, phone, email, address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)

def view_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    return results

def update_contact(old_name, new_name, new_phone, new_email, new_address):
    for contact in contacts:
        if contact['name'] == old_name:
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            break

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]

while True:
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Enter Store Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        add_contact(name, phone, email, address)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        results = search_contact(query)
        for result in results:
            print(result)
    elif choice == '4':
        old_name = input("Enter the name of the contact to update: ")
        new_name = input("Enter new Store Name: ")
        new_phone = input("Enter new Phone Number: ")
        new_email = input("Enter new Email: ")
        new_address = input("Enter new Address: ")
        update_contact(old_name, new_name, new_phone, new_email, new_address)
    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        delete_contact(name)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
