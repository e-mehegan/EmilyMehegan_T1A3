# Imports for this file
import csv

#defs for each functions of the application
# Function to view the contact book as a whole 
def view_contact(file_name):
    print("VIEW CONTACT BOOK")
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        for row in reader:
            print(row)

# Function to add new contacts to the contact book
def add_contact(file_name):
    print("ADD NEW CONTACT")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])

# Function to delete a contact
def delete_contact(file_name):
    print("DELETE A CONTACT")
    contact_remove = input("Enter the contact name that you want to remove: ")
    contact_names = []
    # Reading and saving the data in a list except the one that we want to remove
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
    # Ensuring no case sensitive issues through using .lower
        for row in reader:
            if(contact_remove.lower() != row[0].lower()):
                contact_names.append(row)
    print(contact_names)
    # Writing the updated contact information to the file
    with open(file_name, "w") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerows(contact_names)


def edit_contact(file_name):
    ("Edit a Contact")