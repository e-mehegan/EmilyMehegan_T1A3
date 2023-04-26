#import packages here

#import other pages here

#add different colors here

print("CONTACT BOOK")


#need to put the list.csv here to generate the contact book

#if it doesn't exist need code to create

# Contact menu for the application
def contact_menu():
    print("Enter 1 to view Contact Book")
    print("Enter 2 to add new contact")
    print("Enter 3 to delete a contact")
    print("Enter 4 to edit a contact")
    print("Enter 5 to exit the Contact Book")
    choice = input("Enter your number choice!")
    return choice


# Choices for the user and what the input will do

user_choice = ""

while user_choice != "5":
    user_choice = contact_menu()

#Add to brackets

    if (user_choice == "1"):
        view_contact()
    elif (user_choice == "2"):
        add_contact()
    elif (user_choice == "3"):
        delete_contact()
    elif (user_choice == "4"):
        edit_contact()
    elif (user_choice == "5"):
        continue
    else:
        print("Sorry! Invaild input")
    
    input("To continue press Enter...")

# Text for closing application
print("Closing Contact Book")