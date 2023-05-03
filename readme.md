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

<br>

### <u><b>CONTACT MENU</u></b>

The contact menu is created in an easy why for the user to input a number from 1 to 5 for whatever task they wish to do in the contact book. An overview of the functions are below:

<br>

<b>View contact book (input 1)</b>

- This feature will allow the user to access the whole contact book. They will be able to see all the information for each contact. This will allow the user to look at the contacts book as a whole.

<br>

<b>Add contact (input 2)</b>

- This feature lets the user add a new contact to the contact book, which will save and be able to be viewed with the whole contact book too.

<br>

<b>Delete contact (input 3)</b>

- This feature will let the user delete the contact from the whole contact book. When they choose the view the whole contact book the contact will no longer appear.

<br>

<b>Edit contacts (input 4)</b>

- This feature will allow the user to look for a contact then edit the contact as well if information as changed.

<br>

<b>Exit Contact Book (input 5)</b>

- This feature allows the user to exit the contact book by simply pressing a number. This will exit the application. 

<br>
<br>


### <b><u>ERROR HANDLING & LOOPS IN CONTACT MENU</b></u>

<br>

- To handle any errors, if the user choses an input that is not used, it will output a message that states "Sorry! Invalid Input" prompting them to press enter. This will return them to the contact menu. This process means that it will then loop back to the contact menu. It will continue to loop until the user uses a valid input.

- The contact menu will continue to loop until the user chooses '5' to exit the program. This will then run to the next loop and provide the user with the closing application statement. The other choices will run through there THINGS continuously and will return to the contacts menu until user closes the application. This is carried out after every function until user exits.

<br>
<br>

### <b><u>FUNCTIONS</b></u>

<br>

The features of the application are separated into the files one called 'contact_functions.py' and 'edit_contact_function.py'. This is used to organise the files and to ensure that they are not cluttered in the 'main.py file'. The 'contact_functions.py' and 'edit_contact_function.py' is imported into the 'main.py' to successfully run the application. The edit contact function is separted into its own file since it is bigger than the other functions.

<br>
	
#### <u>VIEW CONTACT BOOK</u>
- The 'View Contact Book' function prints out the contact information in a row for the viewer. This is presented as the name, address and phone number of the contact. This function opens the contact file in read mode then prints the information in the file in the form of a row for the user. 

<br>

#### <u>EDIT CONTACT</u>
- features

<br>

#### <u>ADD NEW CONTACT</u>
- The 'Add New Contact' feature asks for input from the user. It will first ask for the name of the new contact, then the address and phone number. This then opens the contact file in append mode which adds this new information to the contact file in there prospected locations.  

<br>

#### <u>DELETE CONTACT</u>
- The 'Delete Contact" function asks for the name of the contact that the user wished to delete. This will then read the names in the existing contact file and save the data in the file except for the data on the name that they wish to delete. The function will then carry out this deletion and print the appended list of contact names for the user to view. This confirms that the contact and all its information was deleted. The updated file is then written into the file through write mode.
	
ERROR HANDLING: Case sensitive lower case is used

<br>

#### <u>EXIT CONTACT BOOK</u>
- The 'Exit Contact Book' feature allows the user to just enter the number '5' which will then close the application. This is done through a looping function and the continue statement. 
	INCLUDE CODE SNIPPIT

- The continue statement makes sure to exit the current loop in the contact menu and move to the next loop. Since the 'user_choice !=5' is not fulfilled the program will break the loop and exit. This is confirmed through the use of the print statement "Closing Contact Book… CLOSED" to confirm to the user that they have successfully closed the application.
