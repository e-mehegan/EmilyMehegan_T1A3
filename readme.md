# Terminal Application


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

NOTE: The comments and docstring will be deleted from the code snippits

<br>

### <u><b>CONTACT MENU</u></b>

The contact menu is created in an easy way for the user to input a number from 1 to 5 for whatever task they wish to do in the contact book. 

The user is prompted to enter a number from the number options. The return statement will return the user's input choice, which is then stored in the user choice variable. This local varible is only assigned in the while loop, and is used to determine whether the application will continue to loop or exit, depending on the user input. It will determine which function the application will execute based on the user's input number choice. This will bring the user to thier choosen function which will then play out.

The while loop will continue to bring the user back to the contact menu once it has finish the chosen function. This will only stop unbtil the user chooses to exit the program by choosing '5'.

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

<br>

- The 'view contact' fucntion opend the contact file in read mode which will display the information in the file in the form of a row for the user. A 'for' loop is used to execute this. It will read all the information in the CSV file, skipping the first row which are headers. Using the enumerate function, it will number all the contacts in a list for the user. 

- Once the view contact function is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file.

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

<br>

- The 'Add New Contact' feature asks for input from the user. It will first ask for the name of the new contact, then the address and phone number. There is also to option to exit the function in each input allowing the user to have options if they change thier mind or no longer want to add the contact. It will return each time to the contact menu without saving any of the information they have

- Once the user has inputed the name, address and phone variables it will store that input in the variables which will be appened in the contact file. This input will be written into there assigned rows in the file and saved. 

- When the user has inputed a new contact they will be able to return to the contact menu and view the new contact through the view contact function. 

- Once the add contact function is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file.

```
def add_contact(file_name):
    
    print(f"{bg('22')}{fg('234')}ADD NEW CONTACT{attr('reset')}")
    
    name = input(f"Enter {fg('69')}Name{attr('reset')}('q' to exit): ")
    if name == "q":
        return
    address = input(f"Enter {fg('69')}Address{attr('reset')}('q' to exit): ")
    if address == "q":
        return
    phone = input(f"Enter {fg('69')}Phone Number{attr('reset')}('q' to exit): ")
    if phone == "q":
        return
   
    with open(file_name, "a") as contact_file:
        writer = csv.writer(contact_file)
        writer.writerow([name, address, phone])
```

<br>

#### <u>DELETE CONTACT</u>

<br>

- The 'Delete Contact" function asks for the name of the contact that the user wishes to delete. The varible is named 'contact_remove' for this input. An option to exit the delete contact function is also presented to the user if they change thier mind. If user inputs 'q' it will break from the loop and return back to the contact menu. This helps provide options to the user if the may have pressed the wrong button or have changed thier mind.

- The contacts will be loaded form the contact file and be displayed to the view on the screen. This is done if so that if there are two of the same name contacts they can see the full contact information of the contacts and choose the write one that they want to delete. This will be printed in a row and the first row of the contact list will be skipped since it is just going to be displayed in the contact list CSV file.

- The user is asked to simply enter the number of the contact that they wish to delete. This is displayed in the first colomn in the terminal of the application. If all the input is correct it will use the 'pop' function to remove that contact for the contact file. It will then write the updated contacts without the popped name. Text will be display to let the user know that the contact has been deleted. 

- Once the delete contact function is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file.


### <u>ERROR HANDLING</u>

<br>

- A 'ValueError' is handled by printing 'Invalid Choice' to let the user know that they haven't entered a vaild input. If so, it will loop back to the beginning of the function asking which contact they wish to delete. This will continue to loop until they press 'q' in the 'choice' variable, which will break the loop and go to the contact menu function. 

```
def delete_contact(file_name):

    print(f"{bg('22')}{fg('234')}DELETE A CONTACT{attr('reset')}")

    contact_names = []
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        for row in reader:
            contact_names.append(row)

    print(f"{attr('bold')}CONTACT LIST{attr('reset')}")
    print(f"{attr('bold')}# - NAME - ADDRESS - PHONE NUMBER{attr('reset')}")
    for i, row in enumerate(contact_names[1:], 1):
        print(f"{i}. {row[0]} - {row[1]} - {row[2]}")

    while True:
        choice = input(f"Enter the {attr('bold')}#number{attr('reset')} of the contact you want to {fg('9')}remove{attr('reset')} (or enter 'q' to return to contact menu): ")
        if choice == "q":
            break

        try:
            index = int(choice)
            if index < 1 or index > len(contact_names) - 1:
                raise ValueError
        except ValueError:
            print(f"{fg('9')}Invalid Choice{attr('reset')}")
            continue

        contact_name = contact_names[index][0]
        contact_names.pop(index)
        with open(file_name, "w") as contact_file:
            writer = csv.writer(contact_file)
            writer.writerows(contact_names)

        print(f"{fg('9')}{contact_name} has been deleted!{attr('reset')}")
        break
```

<br>

#### <u>EDIT CONTACT</u>

- The 'edit contact' function as the 'edit_name' variable for the user input. This will ask for the name of the contact that they wish to edit from thier contact file. Once the user inputs a name it will open and read the contact file searching for the corresponding name.

- The 'contact_found' boolean variable will be set to either 'True' if the contact in the current index 'i' is found or 'False' if not. If the contact is found it will print the current contact information of the 'edit_name' contact input. The ' while True:' loop is used to display the options of what information in the contact the user wants to edit. The 'choice' function will then carry out the users 'choice' input. This will allow then to edit the information. It will then open the contact file in write mode and update the changed information. A print statement will then confirm that the changes were made to the file. The 'while True:' loop will begin again until the user chooses the 'Retrun the Contact Book Menu' option.

- If it is 'False' it will throw out an error. To compat this if the contact is not found a statement will be printed to the user saying that the contact was not found. If this happens it will then loop back to the beginning of the function and ask for a contact name again. 

- Once the edit contact function is executed it will prompt the user to press enter, then will return to the main menu due to the loop. This is programmed in the 'main.py' file

```
def edit_contact(file_name):

    print(f"{bg('22')}{fg('234')}EDIT A CONTACT{attr('reset')}")
    edit_name = input(f"Enter {attr('bold')}{attr('underlined')}name{attr('reset')} of contact you wish to edit: ")
    
    contact_names = []
    with open(file_name, "r") as contact_file:
        reader = csv.reader(contact_file)
        contact_names = list(reader)

    contact_found = False
    for i in range(len(contact_names)):
        if contact_names[i][0].strip().lower() == edit_name.strip().lower():
            contact_found = True
            print(f"\n{bg('4')}Current contact information:{attr('reset')} {contact_names[i]}\n")

            while True:
                print("What information would you like to change?")
                print(f"{fg('69')}1.{attr('reset')} Name")
                print(f"{fg('69')}2.{attr('reset')} Address")
                print(f"{fg('69')}3.{attr('reset')} Phone number")
                print(f"{fg('69')}4.{attr('reset')} Return to the Contact Book Menu")
                choice = int(input("Enter your number choice!: "))

                if choice == 1:
                    new_value = input(emoji.emojize("Enter new name:  :pen: "))
                    contact_names[i][0] = new_value
                    break
                elif choice == 2:
                    new_value = input(emoji.emojize("Enter new address:  :house: "))
                    contact_names[i][1] = new_value
                    break
                elif choice == 3:
                    new_value = input(emoji.emojize("Enter new phone number:  :mobile_phone: "))
                    contact_names[i][2] = new_value
                    break
                elif choice == 4:
                    return
                else:
                    print(f"Sorry! {fg('9')}Invalid input.{attr('reset')} Please enter a valid input of {attr('underlined')}1 to 4{attr('reset')}.\n")
                    continue

            with open(file_name, "w", newline="") as contact_file:
                writer = csv.writer(contact_file)
                writer.writerows(contact_names)
                
            print(f"Contact information for {fg('4')}{edit_name}{attr('reset')} has been updated!")
            return

    if not contact_found:
        print(f"Sorry! {fg('9')}Contact not found{attr('reset')}")
```

<br>

#### <u>EXIT CONTACT BOOK</u>

- The 'Exit Contact Book' feature allows the user to just enter the number '5' which will then close the application. This is done through a looping function and the continue statement. 

- The continue statement makes sure to exit the current loop in the contact menu and move to the next loop. Since the 'user_choice !=5' is not fulfilled the program will break the loop and exit. This is confirmed through the use of the print statement "Closing Contact Book… CLOSED" to confirm to the user that they have successfully closed the application.

- If the user inputs an incorrect input choice then to avoid any errors, a 'Sorry! Invalid input' statement will be given to the user, prompting them to press enter which will bring then back to the contact menu fuction.

```
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

# Prompt to bring the user back to the contact menu
    input(f"To continue press {fg('69')}{attr('bold')}Enter{attr('reset')}...")

# Text for closing application
print(f"{fg('4')}Closing Contact Book.... {attr('bold')}CLOSED{attr('reset')}")
```

## <b><u> Implementation Plan</b></u>

My implementation plan of this terminal application was done on Trello

- I broke up each aspect of the assignment and put them onto thier own list. This was done so that it wasn't crowded on one list. This helped with the organisation and execution of the project. Each card as a description overview of what the task entails. The bigger lists have card with the description and a checklist to ensure that all tasks relating to the card are done. Each card outlines what is to be completed for each feature of the application. A checklist is also done for each feature of what need to be included for it to be executed. 

- Deadlines have been given to each card to organise task that need to be done by breaking down what days they are to be completed. This also ensures that I don't fall behind on any of the content that need to be done of each list.

### <b>Terminal Application Plan</b>

![Trello-Plan](./docs/trello_ss.png "Trello plan")

### <b>Code - Functions Plan</b>

![Code-Function](./docs/codefunction_ss.png "Code Functions")

![Code-Function](./docs/main_ss.png "Main Function Code")

![Code-Function](./docs/view_ss.png "View Function Code")

![Code-Function](./docs/add_ss.png "Add Function Code")

![Code-Function](./docs/delete_ss.png "Delete Function Code")

![Code-Function](./docs/edit_ss.png "Edit Function Code")

![Code-Function](./docs/exit_ss.png "Exit Function Code")

### <b>Code - Other Aspects Plan</b>

![Code-Include](./docs/codeother_ss.png "Code Other Aspects")

![Code-Include](./docs/test_ss.png "Design tests")

![Code-Include](./docs/df_ss.png "Developer Functions")

![Code-Include](./docs/commit_ss.png "Git Commits ")


## <b><u>Help Documentation</b></u>

Below is instructions which will describe how to install and use the terminal application

### Steps

### Dependencies of the application

### System/Hardware Requirements

### How to use command line arguments