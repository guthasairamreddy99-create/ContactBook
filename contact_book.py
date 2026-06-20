import os

FILE_NAME = "contacts.txt"

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print("\nContact Added Successfully!")

# View Contacts
def view_contacts():
    if not os.path.exists(FILE_NAME):
        print("\nNo contacts available.")
        return

    with open(FILE_NAME, "r") as file:
        contacts = file.readlines()

    if len(contacts) == 0:
        print("\nNo contacts available.")
        return

    print("\n----- CONTACT LIST -----")
    for contact in contacts:
        name, phone, email = contact.strip().split(",")
        print(f"Name  : {name}")
        print(f"Phone : {phone}")
        print(f"Email : {email}")
        print("------------------------")

# Search Contact
def search_contact():
    search = input("Enter Name to Search: ").lower()

    if not os.path.exists(FILE_NAME):
        print("\nNo contacts found.")
        return

    found = False

    with open(FILE_NAME, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")

            if search in name.lower():
                print("\nContact Found")
                print("Name :", name)
                print("Phone:", phone)
                print("Email:", email)
                found = True

    if not found:
        print("\nContact Not Found.")

# Main Program
while True:
    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")