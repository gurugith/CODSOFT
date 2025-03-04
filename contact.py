# Sample Contact Management Application

# Initialize an empty list to hold contacts
contacts = []

def display_menu():
    print("\nContact Management Application")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    return input("Choose an option: ")

def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print(f'Contact "{name}" added.')

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact['name']} - {contact['phone']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")

def update_contact():
    view_contacts()
    if contacts:
        contact_number = int(input("Enter the contact number to update: ")) - 1
        if 0 <= contact_number < len(contacts):
            name = input("Enter the new contact name (leave blank to keep current): ")
            phone = input("Enter the new phone number (leave blank to keep current): ")
            email = input("Enter the new email address (leave blank to keep current): ")
            address = input("Enter the new address (leave blank to keep current): ")
            
            if name:
                contacts[contact_number]['name'] = name
            if phone:
                contacts[contact_number]['phone'] = phone
            if email:
                contacts[contact_number]['email'] = email
            if address:
                contacts[contact_number]['address'] = address
            
            print("Contact updated.")
        else:
            print("Invalid contact number.")

def delete_contact():
    view_contacts()
    if contacts:
        contact_number = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= contact_number < len(contacts):
            removed_contact = contacts.pop(contact_number)
            print(f'Contact "{removed_contact["name"]}" deleted.')
        else:
            print("Invalid contact number.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()