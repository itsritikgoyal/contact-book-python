import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name: {self.name}, Phone: {self.phone}")


class ContactBook:
    def __init__(self):
        self.contacts = self.load_contacts()

    def add_contact(self, name, phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact already exists")
                return
        if not name.strip():
            print("Name cannot be empty")
            return
        new_contact = Contact(name,phone)
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added")


    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.display()
                return
        print("Contact not found")
        
    def show_contacts(self):
        if not self.contacts:
            print("No contacts found")
            return
        
        print("\n--- Contact List ---")
        for contact in self.contacts:
            contact.display()
            
    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                data = json.load(file)
                return [Contact(d["name"], d["phone"]) for d in data]
        except FileNotFoundError:
            return []
        
    def save_contacts(self):
        data = []
        for c in self.contacts:
            data.append({"name": c.name, "phone": c.phone})

        try:
            with open("contacts.json", "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print("Error saving file:", e)
            
    def update_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                self.save_contacts()
                print("Contact updated")
                return
        print("Contact not found")
        
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted")
                return
        print("Contact not found")
    
    def count_contacts(self):
        print(f"Total contacts: {len(self.contacts)}")
    
cb = ContactBook()

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        cb.add_contact(name, phone)

    elif choice == "2":
        cb.show_contacts()

    elif choice == "3":
        name = input("Enter name: ")
        cb.search_contact(name)

    elif choice == "4":
        name = input("Enter name: ")
        phone = input("Enter new phone: ")
        cb.update_contact(name, phone)

    elif choice == "5":
        name = input("Enter name: ")
        cb.delete_contact(name)

    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    
    else:
        print("Invalid Choice : Enter again")
    
    
    
    
