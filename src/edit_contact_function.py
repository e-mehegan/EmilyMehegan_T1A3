#imports for this file
import csv

from colored import fg, bg, attr
import emoji



def edit_contact(file_name):
    """
    Function to edit contacts in the contact book
    
    Parameters: file_name (str): The name of the file where the contacts will
                    stored for the user
    """

    print(f"{bg('22')}{fg('234')}EDIT A CONTACT{attr('reset')}")

    # Read all contacts from the CSV file
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        contact_names = list(reader)
    
    # Show the list of contacts to user
    print("Contacts:")
    for i in range(1, len(contact_names)):
         print(f"{i+1}. {contact_names[i][0]}")
    
    # Contact number input from user
    choice = int(input(f"Enter the {attr('underlined')}number{attr('reset')} of the contact you want to edit: "))

    # Current information of chosen contact
    chosen_contact = contact_names[choice-1]
    print(f"\n{bg('4')}Current contact information:{attr('reset')} {chosen_contact}\n")

    while True:
        # Prompt user for what they want to change. Strip function used for any whitespace
        print("What information would you like to change?")
        print(f"{fg('69')}1.{attr('reset')} Name")
        print(f"{fg('69')}2.{attr('reset')} Address")
        print(f"{fg('69')}3.{attr('reset')} Phone number")
        print(f"{fg('69')}4.{attr('reset')} Return to the Contact Book Menu")
        choice = input("Enter your number choice!: ").strip()
        
        if not choice:
            print(f"{fg('9')}Invalid Choice{attr('reset')}")
            continue

        # Valueerror handled
        try:
            choice = int(choice)
        except ValueError:
            print(f"{fg('9')}Invalid Choice{attr('reset')}")
            continue

        # Update the chosen field or exit back to contact menu
        while True:
            try:
                if choice == 1:
                    new_value = input(emoji.emojize("Enter new name:  :pen: "))
                    chosen_contact[0] = new_value
                    break
                elif choice == 2:
                    new_value = input(emoji.emojize("Enter new address:  :house: "))
                    chosen_contact[1] = new_value
                    break
                elif choice == 3:
                    new_value = input(emoji.emojize("Enter new phone number:  :mobile_phone: "))
                    chosen_contact[2] = new_value
                    break
                elif choice == 4:
                    # Write updated contact information
                    with open(file_name, "w", newline="") as contact_file:
                        writer = csv.writer(contact_file)
                        writer.writerows(contact_names)
                    return
                else:
                    print(f"Sorry! {fg('9')}Invalid input.{attr('reset')} Please enter a valid input of {attr('underlined')}1 to 4{attr('reset')}.\n")
                    choice = int(input("Enter your number choice!: "))

            #Value Error Handled
            except ValueError:
                print(f"{fg('9')}Invalid Choice{attr('reset')}")

        # Write updated contact information
        with open(file_name, "w", newline="") as contact_file:
            writer = csv.writer(contact_file)
            writer.writerows(contact_names)
            
        print(f"Contact information for has been updated!")
