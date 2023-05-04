# Imports for this file
import csv

from colored import fg, bg, attr




def view_contact(file_name):
    """
    Function to view contacts

    Parameters:
    file_name (str): The name of the file where the contacts will
                    stored for the user
    """
    # Prints all the contacts that are present in the contact file
    print(f"{bg('22')}{fg('234')}VIEW CONTACT BOOK{attr('reset')}")

    #Opens the contact file in read mode, printing the contact file content
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        #This will skip numbering of first row
        next(reader)
        
        # This will then print the first row with our contact, address and phone number headings
        print(f"{attr('bold')}NAME - ADDRESS - PHONE NUMBER{attr('reset')}")
        # Print other rows with a number identifier
        for i, row in enumerate(reader, 1):
            print(f"{i}. {row[0]} - {row[1]} - {row[2]}")



def add_contact(file_name):
    """ 
    Function to add new contacts to the contact book

     Parameters:
    file_name (str): The name of the file where the contacts will
                    stored for the user
    """
    #Takes input from the user to create the new contact or exit
    print(f"{bg('22')}{fg('234')}ADD NEW CONTACT{attr('reset')}")
    
    name = input(f"Enter {fg('69')}Name{attr('reset')} ('q' to exit): ")
    if name == "q":
        return
    address = input(f"Enter {fg('69')}Address{attr('reset')} ('q' to exit): ")
    if address == "q":
        return
    phone = input(f"Enter {fg('69')}Phone Number{attr('reset')} ('q' to exit): ")
    if phone == "q":
        return
    
    # Opens the contact file in append mode 
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])










