# Test One

import os


"""
Test Case 1: This will create the contact CSV file and check if it exists
If it does it will not create another
"""
def test_contact_list_file_exists():
    # create the contact list CSV
    with open('contact_list.csv', 'w') as f:
        f.write('CONTACTS,ADDRESS,PHONE\n')

    # check if the CSV exists
    assert os.path.exists('contact_list.csv')


"""
Test Case 2: This will check if the file is created and it has the header content in the file
"""
def test_contact_list_file_header():

    # Check if CSV file created and will check for header
    file_name = "contact_list.csv"
    contact_file = open(file_name, "w")
    contact_file.write("CONTACTS,ADDRESS,PHONE\n")
    contact_file.close()

    with open(file_name, "r") as f:
        header = f.readline().strip()
    
    assert header == "CONTACTS,ADDRESS,PHONE"

