#import packages here

#imported functions from other file
from contact_functions import view_contact, add_contact, delete_contact, edit_contact

# Used as the 'heading' for the application - lets the user know what it is
print("CONTACT BOOK")

# The contact list which will display the input from the user
file_name = "contact_list.csv"

# Check if contact list is created - if not this will create the list
try:
    contact_file = open(file_name, "r")
    contact_file.close()

# If does not exist this will create it
except FileNotFoundError as e:
    contact_file = open(file_name, "w")
    contact_file.write("Contacts,Information")
    contact_file.close()

# Contact menu for the application
def contact_menu():
    print("Enter 1 to view Contact Book")
    print("Enter 2 to add new contact")
    print("Enter 3 to delete a contact")
    print("Enter 4 to edit a contact")
    print("Enter 5 to exit the Contact Book")
    choice = input("Enter your number choice!: ")
    return choice


# Choices for the user and what the input will do - This will loop until user exits
user_choice = ""

# This is to exit the loop
while user_choice != "5":
    user_choice = contact_menu()

#Add to brackets

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

# Brings the user back to the menu
    input("To continue press Enter...")

# Text for closing application
print("Closing Contact Book.... CLOSED")