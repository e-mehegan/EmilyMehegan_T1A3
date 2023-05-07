# Test Two

import csv
import os

from delete_contact_function import delete_contact

# Test file
TEST_FILE_NAME = "test_file.csv"

"""Tests if the name is deleted from the contact file
"""
def setup_module():
    # Create test file and test names
    with open(TEST_FILE_NAME, "w", newline="") as test_file:
        writer = csv.writer(test_file)
        writer.writerow(["Name", "Address", "Phone Number"])
        writer.writerow(["Nikki", "65 Giggle St", "18008008"])
        writer.writerow(["Chad", "41 Sad Ave", "1800433"])


def teardown_module():
    # After test complete remove file
    os.remove(TEST_FILE_NAME)


def test_delete_contact():
    # Testing delete contact by deleting chosen test contact
    delete_contact(TEST_FILE_NAME)

    # Check if contact has been removed from the file
    with open(TEST_FILE_NAME, "r") as test_file:
        reader = csv.reader(test_file)
        assert ["Nikki", "65 Giggle St", "18008008"] not in reader

