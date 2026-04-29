from models import Contact
import json

class ContactBook:
    def __init__(self):
        # Load saved contacts as soon as a ContactBook object is created.
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            # Read contacts from the JSON file and turn each item into a Contact object.
            with open("contacts.json", "r") as file:
                data = json.load(file)
                return [Contact(d["name"], d["phone"]) for d in data]
        except FileNotFoundError:
            # If the file does not exist yet, start with an empty contact list.
            return []

    def add_contact(self, name, phone):
        # Reload first so the latest contacts from the file are used.
        self.contacts = self.load_contacts()
        if not name.strip():
            return {"error": "Name cannot be empty"}
        for contact in self.contacts:
            # Compare names in lowercase so "Ritik" and "ritik" are treated the same.
            if contact.name.lower() == name.lower():
                return {"error": "Contact already exists"}
        new_contact = Contact(name,phone)
        self.contacts.append(new_contact)
        self.save_contacts()
        return {"message": "Contact added"}
        
    def save_contacts(self):
        # Convert Contact objects into dictionaries before saving them as JSON.
        data = []
        for c in self.contacts:
            data.append({"name": c.name, "phone": c.phone})

        try:
            # Save contacts in a readable format using indent=4.
            with open("contacts.json", "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print("Error saving file:", e)
            
    def update_contact(self, name, new_phone):
        # Reload contacts, find the matching name, then replace only the phone number.
        self.contacts = self.load_contacts()
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = new_phone
                self.save_contacts()
                return {"message": "Contact updated"}
        return {"error": "Contact not found"}

    def search_contact(self, name):
        # Reload contacts, then find one contact by name.
        self.contacts = self.load_contacts()
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return {"name": contact.name, "phone": contact.phone}
        return {"error": "Contact not found"}
        
    def delete_contact(self, name):
        # Reload contacts, find the matching name, then remove it from the list.
        self.contacts = self.load_contacts()
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                return {"message": "Contact deleted"}
        return {"error": "Contact not found"}
