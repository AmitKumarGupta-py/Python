phonebook = {}


def add_contact(name, phone, email):
    phonebook[name.lower()] = {"phone": phone, "email": email}
    print("Contact added successfully!")


def search_contact(name):
    name = name.lower()
    if name in phonebook:
        print(f"Name: {name}")
        print(f"Phone: {phonebook[name]['phone']}")
        print(f"Email: {phonebook[name]['email']}")
    else:
        print("Contact not found!")


def update_contact(name, phone=None, email=None):
    name = name.lower()
    if name in phonebook:
        if phone:
            phonebook[name]["phone"] = phone
        if email:
            phonebook[name]["email"] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact(name):
    name = name.lower()
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


while True:
    print("\nPhonebook Application")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "3":
        name = input("Enter name to update: ")
        phone = input("Enter new phone number (press enter to skip): ")
        email = input("Enter new email (press enter to skip): ")
        update_contact(name, phone or None, email or None)
    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "5":
        print("\nAll Contacts:")
        for name, details in phonebook.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("--------------------")
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")

