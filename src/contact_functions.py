# Imports for this file
import csv

from colored import fg, bg, attr




def view_contact(file_name):
    #Function to view contacts
    """Prints all the contacts that are present in the contact file"""
    print(f"{bg('22')}{fg('234')}VIEW CONTACT BOOK{attr('reset')}")
    """Opens the contact file in read mode, printing the contact file content"""
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        """ This will skip numbering the first row"""
        next(reader)
        """ This will then print the first row with our contact, address and phone number headings"""
        # This will make it clearer for the user
        print(f"{attr('bold')}NAME - ADDRESS - PHONE NUMBER{attr('reset')}")
        """Then print other rows with a number identifier"""
        for i, row in enumerate(reader, 1):
            print(f"{i}. {row[0]} - {row[1]} - {row[2]}")



def add_contact(file_name):
    #Function to add new contacts to the contact book
    """Takes input from the user to create the new contact"""
    print(f"{bg('22')}{fg('234')}ADD NEW CONTACT{attr('reset')}")
    name = input(f"Enter {fg('69')}Name{attr('reset')}: ")
    address = input(f"Enter {fg('69')}Address{attr('reset')}: ")
    phone = input(f"Enter {fg('69')}Phone Number{attr('reset')}: ")
    """
    Opens the contact file in append mode to allow new data to be written into the file.
    This adds to exisiting data and does not overwrite content in the contact file. Print it in a row
    """
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])



def delete_contact(file_name):
    #Function to delete a contact
    """Takes input from the user of which contact they want to delete"""
    print(f"{bg('22')}{fg('234')}DELETE A CONTACT{attr('reset')}")
    contact_remove = input(f"Enter the {attr('bold')}{attr('underlined')}contact name{attr('reset')} that you want to {fg('9')}remove{attr('reset')}: ")
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



