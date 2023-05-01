# Imports for this file
import csv



def view_contact(file_name):
    #Function to view contacts
    """Prints all the contacts that are present in the contact file"""
    print("VIEW CONTACT BOOK")
    """Opens the contact file in read mode, printing the contact file content"""
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        """ This will skip numbering the first row"""
        next(reader)
        """ This will then print the first row with our contact, address and phone number headings"""
        # This will make it clearer for the user
        print("NAME - ADDRESS - PHONE NUMBER")
        """Then print other rows with a number identifier"""
        for i, row in enumerate(reader, 1):
            print(f"{i}. {row[0]} - {row[1]} - {row[2]}")


def add_contact(file_name):
    #Function to add new contacts to the contact book
    """Takes input from the user to create the new contact"""
    print("ADD NEW CONTACT")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    """Opens the contact file in append mode to allow new data to be written into the file.
    This adds to exisiting data and does not overwrite content in the contact file. Print it in a row
    """
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])


def delete_contact(file_name):
    #Function to delete a contact
    """Takes input from the user of which contact they want to delete"""
    print("DELETE A CONTACT")
    contact_remove = input("Enter the contact name that you want to remove: ")
    contact_names = []
    """Reading and saving the data in a list except the one that we want to remove"""
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        """Ensuring no case sensitive issues through using lower. and appends the contact file"""
        for row in reader:
            if(contact_remove.lower() != row[0].lower()):
                contact_names.append(row)
    print(contact_names)
    """Writing the updated contact information to the file"""
    with open(file_name, "w") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerows(contact_names)



