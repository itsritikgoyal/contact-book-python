import json

def add_contact(contacts, name, phone):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact already exists")
            return
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"Contact added")


def search_contact(contacts, name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"Name: {name}, Phone: {contact['phone']}")
            return
    print("Contact not found")
    
def show_contacts(contacts):
    if not contacts:
        print("No contacts found")
        return
    for contact in contacts:
        print(f"Name : {contact['name']}, Phone no : {contact['phone']}")
        
def load_contacts():
    try:
        with open("contacts.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_contacts(contacts):
    with open("contacts.json","w") as file:
        json.dump(contacts,file,indent=4)
        
def update_contact(contacts,name,new_phone):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = new_phone
            save_contacts(contacts)
            print("Contact Updates")
            return
    print("Contact not found")
    
def delete_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted")
            return
    print("Contact not found")
    
contacts = load_contacts()

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter Choice in no.")
    
    if choice=="1":
        name = input("Enter name :")
        phone = input("Enter phone :")
        add_contact(contacts,name,phone)
        
    elif choice=="2":
        show_contacts(contacts)
    
    elif choice=="3":
        name = input("Enter name :")
        search_contact(contacts,name)
        
    elif choice=="4":
        name = input("Enter name :")
        new_phone = input("Enter new phone no.")
        update_contact(contacts,name,new_phone)
        
    elif choice=="5":
        name = input("Enter name :")
        delete_contact(contacts,name)
    
    elif choice=="6":
        print("Exit Successful")
        break
    
    else:
        print("Invalid Choice : Enter again")
    
    
    
    
