"""INFOZATECH Task 5: Contact Book
Run with: python task5_contact_book.py
Contacts are saved in contacts.json in the same directory.
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("contacts.json")


def load_contacts():
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read contacts file. Starting with an empty contact book.")
        return []


def save_contacts(contacts):
    try:
        DATA_FILE.write_text(json.dumps(contacts, indent=4, ensure_ascii=False), encoding="utf-8")
    except OSError as error:
        print(f"Could not save contacts: {error}")


def show_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n--- CONTACT BOOK ---")
    for number, contact in enumerate(contacts, start=1):
        print(f'{number}. {contact["name"]} | Phone: {contact["phone"]} | Email: {contact["email"]}')


def find_contact_index(contacts, prompt="Enter contact number: "):
    if not contacts:
        print("No contacts available.")
        return None
    show_contacts(contacts)
    try:
        index = int(input(prompt).strip()) - 1
        if 0 <= index < len(contacts):
            return index
    except ValueError:
        pass
    print("Invalid contact number.")
    return None


def get_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def add_contact(contacts):
    name = get_required("Name: ")
    phone = get_required("Phone: ")
    email = input("Email (optional): ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.")


def search_contacts(contacts):
    query = input("Search by name, phone, or email: ").strip().lower()
    if not query:
        print("Search query cannot be empty.")
        return
    matches = [
        contact for contact in contacts
        if query in contact["name"].lower()
        or query in contact["phone"].lower()
        or query in contact["email"].lower()
    ]
    show_contacts(matches)


def update_contact(contacts):
    index = find_contact_index(contacts, "Enter contact number to update: ")
    if index is None:
        return
    contact = contacts[index]
    print("Press Enter to keep the existing value.")
    name = input(f'Name [{contact["name"]}]: ').strip()
    phone = input(f'Phone [{contact["phone"]}]: ').strip()
    email = input(f'Email [{contact["email"]}]: ').strip()
    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    contact["email"] = email if email else contact["email"]
    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    index = find_contact_index(contacts, "Enter contact number to delete: ")
    if index is None:
        return
    removed = contacts.pop(index)
    save_contacts(contacts)
    print(f'Contact "{removed["name"]}" deleted.')


def main():
    contacts = load_contacts()
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Search contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option. Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
