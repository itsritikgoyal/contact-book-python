# Contact Book (Python Flask API)

This is a simple contact management system built using Python and Flask. It stores contacts in a `contacts.json` file and provides API routes to add, view, search, update, and delete contacts.

The project currently runs locally on your system. After starting the Flask server, the API base URL is:

```text
http://127.0.0.1:5000
```

## Features

* Add a new contact
* View all contacts
* Search a contact by name
* Update a contact's phone number
* Delete a contact
* Store data using JSON

## Technologies Used

* Python
* Flask
* JSON (for storage)

## Project Structure

```text
contact-book-python/
|-- app.py
|-- contact_book.py
|-- models.py
|-- contacts.json
`-- README.md
```

## How to Run

1. Clone or download this project.

2. Open the project folder in terminal.

3. Install Flask if it is not already installed:

   ```bash
   pip install flask
   ```

4. Run the Flask app:

   ```bash
   python app.py
   ```

5. Test the API using Postman, browser, or another API testing tool:

   ```text
   http://127.0.0.1:5000
   ```

## API Routes

### View Contacts

```text
GET /contacts
```

Returns all contacts saved in `contacts.json`.

Example URL:

```text
http://127.0.0.1:5000/contacts
```

### Search Contact

```text
GET /contacts/search/<name>
```

Example:

```text
GET /contacts/search/Ritik
```

Returns one contact if the name is found.

Example response:

```json
{
    "name": "Ritik",
    "phone": "8445366583"
}
```

### Add Contact

```text
POST /contacts
```

Example JSON body:

```json
{
    "name": "Ritik",
    "phone": "8445366583"
}
```

Example success response:

```json
{
    "message": "Contact added"
}
```

### Update Contact

```text
PUT /contacts/<name>
```

Example JSON body:

```json
{
    "phone": "9999999999"
}
```

Example success response:

```json
{
    "message": "Contact updated"
}
```

### Delete Contact

```text
DELETE /contacts/<name>
```

Deletes the contact with the given name.

Example success response:

```json
{
    "message": "Contact deleted"
}
```

## Status Codes

* `200 OK` - Request completed successfully
* `201 Created` - Contact added successfully
* `400 Bad Request` - Invalid request or duplicate contact
* `404 Not Found` - Contact not found

## File Details

* `app.py` - Starts the Flask app and defines API routes.
* `contact_book.py` - Contains the main contact book logic.
* `models.py` - Contains the `Contact` class.
* `contacts.json` - Stores contact data.

## Notes

* `contacts.json` is used as the current storage file.
* Contact names are compared in lowercase, so `Ritik` and `ritik` are treated as the same name.
* This is a local API. It will only run while the Flask server is running on your system.

## Future Improvements

* Add phone number validation
* Add better error handling for missing or invalid request data
* Move storage from JSON to SQLite
* Use contact IDs for update, delete, and search routes
* Add a simple frontend or GUI
