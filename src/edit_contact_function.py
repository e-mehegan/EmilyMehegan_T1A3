import csv

from colored import fg, bg, attr


def edit_contact(file_name):
    print(f"{bg('22')}{fg('234')}EDIT A CONTACT{attr('reset')}")
    edit_name = input(f"Enter {attr('bold')}{attr('underlined')}name{attr('reset')} of contact you wish to edit: ")

    contact_names = []
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        contact_names = list(reader)

    for i in range(1, len(contact_names)):
        if contact_names[i][0].lower() == edit_name.lower():
            print(f"\n{bg('4')}Current contact information:{attr('reset')} {contact_names[i]}\n")

            while True:
                # Prompt user for what they want to change
                print("What information would you like to change?")
                print(f"{fg('69')}1.{attr('reset')} Name")
                print(f"{fg('69')}2.{attr('reset')} Address")
                print(f"{fg('69')}3.{attr('reset')} Phone number")
                print(f"{fg('69')}4.{attr('reset')} Return to the Contact Book Menu")
                choice = int(input("Enter your number choice!: "))

                # Update the chosen field
                if choice == 1:
                    new_value = input(f"Enter new {attr('bold')}name{attr('reset')}: ")
                    contact_names[i][0] = new_value
                    break
                elif choice == 2:
                    new_value = input(f"Enter new {attr('bold')}address{attr('reset')}: ")
                    contact_names[i][1] = new_value
                    break
                elif choice == 3:
                    new_value = input(f"Enter new {attr('bold')}phone number{attr('reset')}: ")
                    contact_names[i][2] = new_value
                    break
                elif choice == 4:
                    return
                else:
                    print(f"Sorry! {fg('9')}Invalid input.{attr('reset')} Please enter a valid input of {attr('underlined')}1 to 4{attr('reset')}.\n")
                    continue

            # Write the updated contact information to the file
            with open(file_name, "w", newline="") as contact_file:
                writer = csv.writer(contact_file)
                writer.writerows(contact_names)
                
            print(f"Contact information for {fg('4')}{edit_name}{attr('reset')} has been updated!")
            return

    print(f"Sorry! {fg('9')}Contact not found{attr('reset')}")
