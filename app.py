from flask import Flask, request, jsonify
from contact_book import ContactBook

# Create the Flask app and one ContactBook object to handle contact actions.
app = Flask(__name__)
cb = ContactBook()

# GET is used to read all saved contacts.
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = cb.load_contacts()

    # Convert each Contact object into a dictionary so Flask can return JSON.
    return jsonify([
        {"name": c.name, "phone": c.phone}
        for c in contacts
    ])

# POST is used to create a new contact.
@app.route('/contacts', methods=['POST'])
def add_contact():
    # Read JSON data sent by the user, for example: {"name": "Ritik", "phone": "123"}.
    data = request.get_json()
    result = cb.add_contact(data.get("name"), data.get("phone"))

    # Return a bad request status if ContactBook sends back an error.
    if "error" in result:
        return jsonify(result), 400
    return jsonify(result), 201

# GET is used to search one saved contact by name.
@app.route('/contacts/search/<string:name>', methods=['GET'])
def search_contact(name):
    result = cb.search_contact(name)

    # Return 404 when the contact name is not found.
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result)

# PUT is used to update the phone number for an existing contact name.
@app.route('/contacts/<string:name>', methods=['PUT'])
def update_contact(name):
    data = request.get_json()
    result = cb.update_contact(name, data.get("phone"))

    # Return 404 when the contact name is not found.
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result)

# DELETE is used to remove one contact by name.
@app.route('/contacts/<string:name>', methods=['DELETE'])
def delete_contact(name):
    result = cb.delete_contact(name)

    # Return 404 when there is no matching contact to delete.
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result)

# Start the Flask development server when this file is run directly.
if __name__ == "__main__":
    app.run(debug=True)
