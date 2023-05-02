import csv



def edit_contact(file_name):
    print("EDIT A CONTACT")
    edit_name = input("Enter name of contact you wish to edit: ")

    contact_names = []
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        contact_names = list(reader)

    for i in range(1, len(contact_names)):
        if contact_names[i][0].lower() == edit_name.lower():
            print(f"\nCurrent contact information: {contact_names[i]}\n")

            while True:
                # Prompt user for what they want to change
                print("What information would you like to change?")
                print("1. Name")
                print("2. Address")
                print("3. Phone number")
                print("4. Return to the Contact Book Menu")
                choice = int(input("Enter your number choice!: "))

                # Update the chosen field
                if choice == 1:
                    new_value = input("Enter new name: ")
                    contact_names[i][0] = new_value
                    break
                elif choice == 2:
                    new_value = input("Enter new address: ")
                    contact_names[i][1] = new_value
                    break
                elif choice == 3:
                    new_value = input("Enter new phone number: ")
                    contact_names[i][2] = new_value
                    break
                elif choice == 4:
                    return
                else:
                    print("Sorry! Invalid input. Please enter a valid input of 1 to 4.\n")
                    continue

            # Write the updated contact information to the file
            with open(file_name, "w", newline="") as contact_file:
                writer = csv.writer(contact_file)
                writer.writerows(contact_names)
                
            print(f"Contact information for {edit_name} has been updated!")
            return

    print("Sorry! Contact not found")
