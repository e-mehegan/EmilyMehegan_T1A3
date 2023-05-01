# Imports for this file
import csv



def view_contact(file_name):
    #Function to view contacts
    """Prints all the contacts that are present in the contact file"""
    print("VIEW CONTACT BOOK")
    """Opens the contact file in read mode, printing the contact file content"""
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        """ This will skip numbering the first row"""
        next(reader)
        """ This will then print the first row with our contact, address and phone number headings"""
        # This will make it clearer for the user
        print("NAME - ADDRESS - PHONE NUMBER")
        """Then print other rows with a number identifier"""
        for i, row in enumerate(reader, 1):
            print(f"{i}. {row[0]} - {row[1]} - {row[2]}")


def add_contact(file_name):
    #Function to add new contacts to the contact book
    """Takes input from the user to create the new contact"""
    print("ADD NEW CONTACT")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    """Opens the contact file in append mode to allow new data to be written into the file.
    This adds to exisiting data and does not overwrite content in the contact file. Print it in a row
    """
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])


def delete_contact(file_name):
    #Function to delete a contact
    """Takes input from the user of which contact they want to delete"""
    print("DELETE A CONTACT")
    contact_remove = input("Enter the contact name that you want to remove: ")
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



def edit_contact(file_name):
    # Function to edit a contact
    print("EDIT A CONTACT")
    edit_name = input("Enter name of contact you wish to edit: ")

    contact_names = []
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        contact_names = list(reader)

    for i in range(1, len(contact_names)):
        if contact_names[i][0].lower() == edit_name:
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
                    print("Sorry! Invalid input. Please enter a valid input.\n")
                    continue

            # Write the updated contact information to the file
            with open(file_name, "w", newline="") as contact_file:
                writer = csv.writer(contact_file)
                writer.writerows(contact_names)
                
            print(f"Contact information for {edit_name} has been updated!")
            return

    print("Sorry! Contact not found")
