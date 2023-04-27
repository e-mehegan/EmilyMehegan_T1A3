# Imports for this file
import csv

#defs for each functions of the application
def view_contact(file_name):
    print("VIEW CONTACT BOOK")
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        for row in reader:
            print(row)


def add_contact(file_name):
    print("ADD NEW CONTACT")
    name = input("Enter Name: ")
    address = input("Enter Address: ")
    phone = input("Enter Phone Number: ")
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])


def delete_contact(file_name):
    print("Delete a Contact")


def edit_contact(file_name):
    ("Edit a Contact")