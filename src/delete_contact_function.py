# Imports for this file
import csv

from colored import fg, bg, attr




def delete_contact(file_name):
    """
    Function to delete a contact in the contact book

    Parameters:
    file_name (str): The name of the file where the contacts will
                    stored for the user
    """
    
    print(f"{bg('22')}{fg('234')}DELETE A CONTACT{attr('reset')}")

    # Will load the contacts in the contact file
    contact_names = []
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        for row in reader:
            contact_names.append(row)

    # Print the contact list which will be numbered
    print(f"{attr('bold')}CONTACT LIST{attr('reset')}")
    print(f"{attr('bold')}# - NAME - ADDRESS - PHONE NUMBER{attr('reset')}")
    for i, row in enumerate(contact_names[1:], 1):
        print(f"{i}. {row[0]} - {row[1]} - {row[2]}")

    # Ask user which contact to delete or if they want to return to contact menu
    while True:
        choice = input(f"Enter the {attr('bold')}#number{attr('reset')} of the contact you want to\
                        {fg('9')}remove{attr('reset')} (or enter {fg('4')}'q'{attr('reset')} to return to contact menu): ")
        if choice == "q":
            break
        
        # If error occurs
        try:
            index = int(choice)
            if index < 1 or index > len(contact_names) - 1:
                raise ValueError
        except ValueError:
            print(f"{fg('9')}Invalid Choice{attr('reset')}")
            continue

        #Contact will be removed through popping the contact from the file and updating the file without contact information
        contact_name = contact_names[index][0]
        contact_names.pop(index)
        with open(file_name, "w") as contact_file:
            writer = csv.writer(contact_file)
            writer.writerows(contact_names)

        print(f"{fg('4')}Contact has been deleted!{attr('reset')}")
        break

