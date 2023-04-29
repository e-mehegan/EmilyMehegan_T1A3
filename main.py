#import packages here

#imported functions from other file
from contact_functions import view_contact, add_contact, delete_contact, edit_contact

# Used as the 'heading' for the application - lets the user know what it is
print("CONTACT BOOK")

# The contact list which will display the input from the user
file_name = "contact_list.csv"

"""Check if contact list is created - if not this will create the list"""
try:
    contact_file = open(file_name, "r")
    contact_file.close()

    """If the file does not exist this will create it"""
except FileNotFoundError as e:
    contact_file = open(file_name, "w")
    contact_file.write("Contacts,Address,Phone\n")
    contact_file.close()


def contact_menu():
    # Contact menu for the application
    print("Enter 1 to view Contact Book")
    print("Enter 2 to add new contact")
    print("Enter 3 to delete a contact")
    print("Enter 4 to edit a contact")
    print("Enter 5 to exit the Contact Book")
    """Asks for user choice and will go to user choice and carry out that function"""
    choice = input("Enter your number choice!: ")
    return choice


user_choice = ""
"""Choices for the user and what the input will do - This will loop until user exits"""


while user_choice != "5":
    user_choice = contact_menu()
    """This is to exit the loop"""

    """User choice input will go to function number the user choses"""
    if (user_choice == "1"):
        view_contact(file_name)
    elif (user_choice == "2"):
        add_contact(file_name)
    elif (user_choice == "3"):
        delete_contact(file_name)
    elif (user_choice == "4"):
        edit_contact(file_name)
    elif (user_choice == "5"):
        continue
    else:
        print("Sorry! Invaild input")

# Prompt to bring the user back to the contact menu
    input("To continue press Enter...")

# Text for closing application
print("Closing Contact Book.... CLOSED")