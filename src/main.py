#imports for this file
from colored import fg, bg, attr
import emoji

from contact_functions import view_contact, add_contact
from edit_contact_function import edit_contact
from delete_contact_function import delete_contact




# Used as the 'heading' for the application - lets the user know what it is
print(emoji.emojize('CONTACT BOOK :telephone_receiver:'))

# The contact list which will display the input from the user
file_name = "contact_list.csv"

#Check if contact list is created - if not this will create the list
try:
    contact_file = open(file_name, "r")
    contact_file.close()

#If the file does not exist this will create it
except FileNotFoundError as e:
    contact_file = open(file_name, "w")
    contact_file.write("CONTACTS,ADDRESS,PHONE\n")
    contact_file.close()


def contact_menu():
    """
    Contact menu function for the application
    
    """
    print(f"{fg('4')}_________________________________{attr('reset')}")
    print(f"Enter {fg('69')}1{attr('reset')} to {fg('69')}{attr('underlined')}view{attr('reset')} Contact Book")
    print(f"Enter {fg('69')}2{attr('reset')} to {fg('69')}{attr('underlined')}add{attr('reset')} new contact")
    print(f"Enter {fg('69')}3{attr('reset')} to {fg('69')}{attr('underlined')}delete{attr('reset')} a contact")
    print(f"Enter {fg('69')}4{attr('reset')} to {fg('69')}{attr('underlined')}edit{attr('reset')} a contact")
    print(f"Enter {fg('69')}5{attr('reset')} to {fg('69')}{attr('underlined')}exit{attr('reset')} the Contact Book")
    print(f"{fg('4')}_________________________________{attr('reset')}")

    #Asks for user choice and will go to user choice and carry out that function
    choice = input(f"Enter your {fg('69')}{attr('underlined')}number{attr('reset')} choice!: ")
    return choice


user_choice = ""

# Will loop until the user enters 5
while user_choice != "5":
    user_choice = contact_menu()
    
    #User choice input will go to function number the user choses
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
        print(f"Sorry! {fg('9')}Invaild input{attr('reset')}")

# Prompt to bring the user back to the contact menu
    input(f"To continue press {fg('69')}{attr('bold')}Enter{attr('reset')}...")

# Text for closing application
print(f"{fg('4')}Closing Contact Book.... {attr('bold')}CLOSED{attr('reset')}")