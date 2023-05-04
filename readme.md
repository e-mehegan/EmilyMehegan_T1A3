# Terminal Application

NOTES: 
- The comments and docstring will be deleted from the code snippits

## <b><u>Code Styling</b></u>

### <ul><u>Identify any code style guide or styling conventions that the application will adhere to</ul></u>

The style guide that was followed through the creation of the application was PEP8. Multiple styling conventions where used to ensure that the code was easy to understand and read for all users. These style conventions with the PEP8 style guide include:

<br>
<br>

<u>DOCSTRINGS AND COMMENTS</u>

- Docstrings have been used through-out the whole application in order to explain and break down what the functions of the applications do. It also assists users of what the functions are needed for, in order for the application to run smoothly. 
- Comments are used to aid in describing the functions and what they do. Further aiding the user of the applications functionality

<br>

<u>CODE LAY-OUT</u>

- Many code-styling elements have been implemented in the lay-out to ensure readability and understanding. These include blank lines, space indentation, imports and wrapped lines. These are the ones that are used the most in the code lay-out.
- Indentation of four spaces is used to help readability.
- Imports are located at the top of the files and separated. This means they are easily seen and helps organise the file.
- Lines are wrapped if they are over 79 characters to help improve with readability and organisation.
- Blank lines are used to help create separation between different functions which aid in organisation and readability of the file.

<br>

<u>WHITESPACE</u>

- Whitespace is avoided through-out to improve readability and prevent errors.

<br>

<u>NAMING CONVENTIONS</u>
- Naming conventions are followed to ensure that the code is understandable and readable. Making sure that function and variable names are in lower case and separated by underscores if need be.

<br>
<br>
<br>

## <u><b>Develop a list of features that will be included in the application. It must include:
- at least THREE features
- describe each feature</b></u>

<br>

### <u><b>CONTACT MENU</u></b>

The contact menu is created in an easy way for the user to input a number from 1 to 5 for whatever task they wish to do in the contact book. 

The user is prompted to enter a number from the number options. The return statement will return the user's input choice, which is then stored in the user choice variable. This local varible is only assigned in the while loop, and is used to determine whether the application will continue to loop or exit, depending on the user input. It will determine which function the application will execute based on the user's input number choice. This will bring the user to thier choosen function which will then play out.

The while loop will continue to bring the user back to the contact menu once it has finish the chosen function. This will only stop unbtil the user chooses to exit the program by choosing '5'

```
def contact_menu():
    print(f"Enter {fg('69')}1{attr('reset')} to {fg('69')}{attr('underlined')}view{attr('reset')} Contact Book")
    print(f"Enter {fg('69')}2{attr('reset')} to {fg('69')}{attr('underlined')}add{attr('reset')} new contact")
    print(f"Enter {fg('69')}3{attr('reset')} to {fg('69')}{attr('underlined')}delete{attr('reset')} a contact")
    print(f"Enter {fg('69')}4{attr('reset')} to {fg('69')}{attr('underlined')}edit{attr('reset')} a contact")
    print(f"Enter {fg('69')}5{attr('reset')} to {fg('69')}{attr('underlined')}exit{attr('reset')} the Contact Book")
    """Asks for user choice and will go to user choice and carry out that function"""
    choice = input(f"Enter your {fg('69')}{attr('underlined')}number{attr('reset')} choice!: ")
    return choice


user_choice = ""

while user_choice != "5":
    user_choice = contact_menu()

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
```
<br>

### <b><u>ERROR HANDLING CONTACT MENU</b></u>

<br>

- To handle any errors, if the user choses an input that is not used, it will output a message that states "Sorry! Invalid Input", prompting them to press enter. This will return them to the contact menu. This will continue to loop back to the contact menu until the user chooses a vaild input.

<br>
<br>

### <b><u>FUNCTIONS</b></u>

<br>

The main features of the application are separated into files, one called 'contact_functions.py' and 'edit_contact_function.py'. This is used to organise the files and to ensure that they are not cluttered in the 'main.py' file. The 'contact_functions.py' and 'edit_contact_function.py' is imported into the 'main.py' to successfully run the application. The edit contact function is separted into its own file since it is bigger than the other functions.

All the functions have the 'file_name' variable is used through-out the applications code.  This is used to create the 'contact_file' and is used to check if this file already exists, if not it will create a new file. This will be stored in the 'file_name', which will then wirte the header row for the file. The varibale names are given in a way that is easy to identify there purpose.

```
from contact_functions import view_contact, add_contact, delete_contact
from edit_contact_function import edit_contact
```

### <b><u>ERROR HANDLING</b></u>

<br>

- In the try block, it will check if the contact list file is already created by opening the file in read mode. If it does open, it will skip creating the file and move onto executing the contact menu function. 

- To avoid the file not found error, if the file doesn't exist the except statement will create a new file. The file will be used to store the contact book information in the 'file_name' variable. This will then open the file and wirte the 'Contacts, Address and phone' heading in a row. This is used done through the write() function. The file is then closed. 

- Without the try and except blocks the program will run into an error and terminate the program without running through any of the functions.

CODE SNIPPIT BELOW:

```
file_name = "contact_list.csv"

try:
    contact_file = open(file_name, "r")
    contact_file.close()

except FileNotFoundError as e:
    contact_file = open(file_name, "w")
    contact_file.write("CONTACTS,ADDRESS,PHONE\n")
    contact_file.close()
```

<br>
	
#### <u>VIEW CONTACT BOOK</u>

- The contact file is opened in read mode which will display the information in the file in the form of a row for the user. A 'for' loop is used to execute this. It will read all the information in the CSV file, skipping the first row which are headers. Using the enumerate function, it will number all the contacts in a list for the user. 

- Once the view contact functions is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file.

```
def view_contact(file_name):
    print(f"{bg('22')}{fg('234')}VIEW CONTACT BOOK{attr('reset')}")

    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        next(reader)

        print(f"{attr('bold')}NAME - ADDRESS - PHONE NUMBER{attr('reset')}")

        for i, row in enumerate(reader, 1):
            print(f"{i}. {row[0]} - {row[1]} - {row[2]}")
```

<br>

#### <u>ADD NEW CONTACT</u>

- The 'Add New Contact' feature asks for input from the user. It will first ask for the name of the new contact, then the address and phone number.

- Once the user has inputed the name, address and phone variables it will store that input in the variables which will be appened in the contact file. This input will be written into there assigned rows in the file and saved. 

- When the user has inputed a new contact they will be able to return to the contact menu and view the new contact through the view contact function. 

- Once the add contact functions is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file.

```
def add_contact(file_name):
    print(f"{bg('22')}{fg('234')}ADD NEW CONTACT{attr('reset')}")

    name = input(f"Enter {fg('69')}Name{attr('reset')}: ")
    address = input(f"Enter {fg('69')}Address{attr('reset')}: ")
    phone = input(f"Enter {fg('69')}Phone Number{attr('reset')}: ")

    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])
```

<br>

#### <u>DELETE CONTACT</u>

- The 'Delete Contact" function asks for the name of the contact that the user wishes to delete. The varible is named 'contact_remove' for this input. 

- The 'contact_name' variable is used to store the information of the users input, except for the contact that is to be removed. The 'contact_file' will be opened in read mode which will then loop through each contact until the 'contact_remove' input finds the corresponding input found in the first colomn of the file.

- The 'lower()' string method is used to make sure the user input is case insensitive to avoid any error in finding the correct 'contact_remove' name.

- After the list has been updated it will print out the 'contact_names' variable information from the CSV file to show that they contact information for the delte name is removed. the 'csv.writer()' function will update the contact list, deleting the chosen contact.

- Once the delete contact functions is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file.

```
def delete_contact(file_name):
    print(f"{bg('22')}{fg('234')}DELETE A CONTACT{attr('reset')}")

    contact_remove = input(f"Enter the {attr('bold')}{attr('underlined')}contact name{attr('reset')} that you want to {fg('9')}remove{attr('reset')}: ")
    contact_names = []

    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        
        for row in reader:
            if(contact_remove.lower() != row[0].lower()):
                contact_names.append(row)
    print(contact_names)

    with open(file_name, "w") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerows(contact_names)
```

<br>

#### <u>EDIT CONTACT</u>

view edit code snippit

- features

<br>

#### <u>EXIT CONTACT BOOK</u>

- The 'Exit Contact Book' feature allows the user to just enter the number '5' which will then close the application. This is done through a looping function and the continue statement. 
	INCLUDE CODE SNIPPIT

- The continue statement makes sure to exit the current loop in the contact menu and move to the next loop. Since the 'user_choice !=5' is not fulfilled the program will break the loop and exit. This is confirmed through the use of the print statement "Closing Contact Book… CLOSED" to confirm to the user that they have successfully closed the application.
