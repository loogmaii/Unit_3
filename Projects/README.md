# Kris' Fridge Manager (Unit 3 project)

![fridge phone](https://user-images.githubusercontent.com/111941936/221760786-ab80eca0-ab94-4039-a442-f05c970ddca2.jpeg)

<sub> Fig.1 shows @coen_pohl_design's illustration on instagram

# Criteria A: Planning

## Problem definition

My proposed application will be a Refrigerator Manager that will enable each housemate to record details of the food they store in the fridge. The application will have a user-friendly interface that will allow users to add and remove food items easily, as well as search for specific items they are looking for from a presented table. This solution will provide a reliable and efficient tool for managing the fridge and preventing disputes among housemates over food ownership, ensuring a more harmonious living environment. The application will be constructed using Pycharm, the Python language, and the KivyMD Language. This project will take 6 weeks and will be evaluated according to the criteria set above.

## Success Criteria

1. A secure registration system will be implemented in the application.
2. The application will require a password for access.
3. The client will have the ability to input information about the food item such as the owner, type of food, location within the fridge, expiration date, and any additional notes.
4. The client will be able to add and remove food items from the database, as well as check the updated inventory.
5. The client will have a search function available to locate specific items within the presented table.
6. The application will display the amount of remaining space in the refrigerator.

## Aproval from the client
  
<img width="1029" alt="Screen Shot 2566-03-09 at 12 58 30" src="https://user-images.githubusercontent.com/111941936/223913217-136310a3-c9c6-4ae1-9643-1016c292b369.png">  
  
<sub> Fig.2 shows an email sent to the client in regards to the success criteria
  
  
<img width="1029" alt="Screen Shot 2566-03-09 at 13 00 04" src="https://user-images.githubusercontent.com/111941936/223913400-e02f7836-cc72-42d3-ab77-1c77f054f5d5.png">

<sub> Fig.3 shows the client approving
  
  
## Proposed Solution

My proposed application will be a Refrigerator Manager that will enable each housemate to record details of the food they store in the fridge. The application will have a user-friendly interface that will allow users to add and remove food items easily, as well as search for specific items they are looking for from a presented table. This solution will provide a reliable and efficient tool for managing the fridge and preventing disputes among housemates over food ownership, ensuring a more harmonious living environment. The application will be constructed using Pycharm, the Python language, and the KivyMD Language. This project will take 6 weeks and will be evaluated according to the criteria set above.

## Rationale for proposed solution

I propose developing a Refrigerator Manager application using Python, KivyMD, and SQLite. This solution will allow each housemate to record important details about the food they store in the fridge, including the food's owner, type, location, and expiration date. The application's user-friendly interface will make it easy for users to add and remove food items, search for specific items, and view a presented table of all stored food items. To ensure the privacy and security of the housemates' information, the app will have a secure registration system.

I chose to use the Python language to develop the application because it is a popular and commonly used programming language that is growing in the tech industry. Its widespread use makes it easier for many developers to understand compared to other languages like C or Javascript, which would benefit the application's development [^1]. Additionally, Python has a wide range of libraries available that can be easily accessed using basic syntax. Overall, the Python programming language is suitable for developing the client's desired application [^2].

Furthermore, I will use KivyMD as the framework for its graphical user interface. KivyMD is a multi-platform application development framework that is easy to learn and work with [^3]. Its pre-built user-interface elements and styles can be easily customized and integrated into Kivy-based applications, saving time and effort in developing the application's interface [^4]. While there are other alternatives such as Flutter or PyQt, I have chosen KivyMD for its ease of use, customizability, and compatibility [^5].

For the application's database management system, I have selected SQLite. SQLite is a free database that requires no additional server process and is implemented on a single file [^6]. It is designed to handle large amounts of data efficiently, making it suitable for storing all kinds of information related to the stored food items . SQLite continuously updates its content, minimizing the risk of lost data in the event of a power failure or crash. Its cross-platform compatibility will enable future developers to expand the program to other platforms [^7]. In comparison to other databases available, SQLite is reliable, efficient, cost-friendly, and easy to use [^8].
  
Overall, the proposed Refrigerator Manager application will provide an efficient and reliable tool for managing the fridge and preventing disputes among housemates over food ownership, ensuring a more harmonious living environment.

# Criteria B: Design

## System diagram
  
<img width="904" alt="Screen Shot 2566-03-09 at 22 44 23" src="https://user-images.githubusercontent.com/111941936/224043072-a27ab6bd-d805-4b9c-9198-622809ad2006.png">

<sub> Fig.4 shows the system diagram
  
A visual representation of the system, its parts, and how they relate to one another is provided by the system diagram. This displays the input (keyboard) to the output (various systems used in this project, including versions of the programming language (Python and KivyMD), the computer version and detail (Processor, version, memory, etc.), the module and database, and the output screen (application interface on the computer screen).
  
## Wireframe diagram
  
![Diagrams-4](https://user-images.githubusercontent.com/111941936/224073234-737e51b1-c4f5-4f75-bb9b-a01544852f52.jpg)

<sub> Fig.5 shows the Wireframe diagram
  
This wireframe diagram's objective is to provide a visual representation of the user interface design that outlines the application's structure and layout. The wireframe also shows how various screens will be accessed via various buttons. The user can see which screen will open when they touch and release the button according to the arrows that extend from the button to the screen.
  
## Flow diagrams

<img width="413" alt="Screen Shot 2566-03-10 at 01 32 32" src="https://user-images.githubusercontent.com/111941936/224089634-2dfa6e78-bcf4-469e-9af5-916ff8e8f9e3.png">
  
<sub> Fig.6 shows the flow diagram for the try_login function
  
This function validates the username and password inputted by the user to login. It retrieves the username and password from the textfields, creates an query to search the "users" table of the database "project3.db" for a record that matches the inputted username and password. If the query returns exactly one result, the function direct the current screen to "HomeScreen" and prints "Login successful". Otherwise, the function sets error messages on the textfields and displays a pop-up message informing the user that the provided username does not have an account in the system.

<img width="200" alt="Screen Shot 2566-03-10 at 01 58 22" src="https://user-images.githubusercontent.com/111941936/224099904-aa5b9d0b-d157-4a0f-9673-741ce45ec95f.png">

<sub> Fig.7 shows the flow diagram for the delete function  
  
This function delete records from the "items" table from "project3.db" based on the checked rows in a user interface data table. The function retrieves the selected rows from the data table to then obtain the "id" value from each row and creating a query to delete the corresponding record from the database. After deleting the selected rows from the database, the data table was then updated, and then a pop-up message confirms that the item(s) have been deleted.
  
<img width="658" alt="Screen Shot 2566-03-10 at 02 26 47" src="https://user-images.githubusercontent.com/111941936/224107323-46f55e86-3a71-4c0e-aa2f-9137af07de94.png">

<sub> Fig.8 shows the flow diagram for the show_occupancy function
  
This function calculates and displays the occupancy rate of the fridge based on the number of items stored in the "project3.db" database by running it through an equation. It sets the screen based on the occupancy rate, with different screens associated with different ranges of occupancy percentage. 
  
## ER diagram
  
<img width="1116" alt="Screen Shot 2566-03-10 at 03 00 02" src="https://user-images.githubusercontent.com/111941936/224115135-51248dd6-370d-4d73-a8d0-4d36131e4c37.png">
  
<sub> Fig.9 shows the ER diagram

This is the ER diagram for the database illustrating the relationship between the items table and users table from the "project3.db" database. In the items table, there are 7 different columns including id, owner, title, exp_date, location, type, and notes(shown above) which each column will have the specific data type after the column name. The second table has 3 columns which are username, id, and password. This diagram also shows that 1 user can have multiple items. The underlined column name is the primary key which have to be unique and for these 2 tables the primary key will be the id.
  
## UML diagram 
  
<img width="1216" alt="Screen Shot 2566-03-10 at 19 23 31" src="https://user-images.githubusercontent.com/111941936/224291708-1aa86b27-72a2-4180-96f1-769de53d2734.png">

<sub> Fig.10 shows the UML diagram

This UML diagram for the OOP classes illustrates the classes and methods utilized during the development of the application. It showcases two primary parent classes, namely MDApp and MDScreen. All the classes inherit the methods and attributes of these parent classes, which is demonstrated by the arrows displayed on the diagram.
  
## Test plan
| Description         | Test Type                    | Input                                                                                                                                                                                                               | Expected output                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Registration System | Functional: Unit test        | 1. Run the program 2. Click the "Register" button 3.Input username 4. Input password 5. Confirm password 6. Click register                                                                                          | After entering all of the relevant data in each textfields and clicking the register button, the user information should be stored into the database, and stored in the 'users' table. The user will then be directed to the login  screen along with a pop-up message indicating that the user is registered. If the user already exists, a pop-up  will show informing the user that the username is already in use.      |
| Login System        | Functional: Unit test        | 1. Run the program 2. Click the "Login" button 3.Input username 4. Input password 6. Click login                                                                                                                    | If the username and password input is correct, the user will be directed to the Home screen, if not, the helper text for both the username and password will show up telling the user to re-check their input again.                                                                                                                                                                                                        |
| Logout System       | Functional: Unit test        | 1. Run the program 2. Click the "Logout" button                                                                                                                                                                     | After clicking the "Log out", the user will be directed to the Home screen                                                                                                                                                                                                                                                                                                                                                  |
| Add Item System     | Functional: Unit test        | 1. Run the program 2. Login 3. Click "Add item" button 4. Input owner, title 5. Select type of food 6. Input any additional notes 7. Select expiration date 8. Click add item                                       | After entering all of the relevant data, the user will then be directed  to the Home screen along with a pop-up message indicating that the item has been added.                                                                                                                                                                                                                                                            |
| Food items database | Functional: Integration test | 1. Run the program 2. Login 3. Click "Add item" button 4. Input owner, title 5. Select type of food 6. Input any additional notes 7. Select expiration date 8. Click add item 9. Check 'items' table in project3.db | All relevant data regarding the food information should be stored in the database, and stored in the 'items' table.  The table in the database should be updated whenever a new item is added or removed.                                                                                                                                                                                                                   |
| List Screen         | Functional: Unit test        | 1. Run the program 2. Login 3. Click "view list" button                                                                                                                                                             | From clicking the "view list" button, the user will be directed to a screen that displays a table of all previous  and latest food items data entered from all users in chronological order.                                                                                                                                                                                                                                |
| Delete Item System  | Functional: Unit test        | 1. Run the program 2. Login 3. Click "view list" button 4. Click on checkboxes  of the item(s) that the user wants to delete 5. Click "delete item" button                                                          | A checkmark will show up inside the box when the user selects the checkbox next to the item. The selected item(s)  should then be deleted from the table when they click the delete item button.                                                                                                                                                                                                                            |
| Search Item System  | Functional: Integration test | 1. Run the program 2. Login 3. Click the "view list" button 4. Input any information  regarding the item, they are looking for 5.Click the magnifying glasses icon button                                           | After entering one of the information regarding the item they are looking for in the textfeild and clicking the  icon button, the table would only show that item or all the items that match the description. The database should  be opened for the data displayed on the table. Once they click the icon button again, the table will go back to  displaying every item.                                                 |
| Occupancy system    | Functional: Unit test        | 1. Run the program 2. Login 3. Click the "occupancy" button 5. Click the "back" button                                                                                                                              | The user will be directed to a screen that shows the percentage of the fridge's capacity the items had taken up with a visual representation. The database will be opened and the number of rows in the "items" table will be counted and  calculated into a percentage of the max capacity which will be showcased both through text and visuals. The user  can then press the "back" button to return to the Home screen. |
| Code review         | Non-functional: code review  | assessing the code in project3.py to see whether the variable names, function names,  and comments are suitable                                                                                                     | The user can better grasp how the code works according to the variable names and comment. The code should be simple to understand and easy to follow.                                                                                                                                                                                                                                                                       |
  
## Task Record
  
| Task No |                         Planned Action                        |                                                         Planned Outcome                                                         | Design cycle | Time Estimate | Completion date | Criterion |
|:-------:|:-------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:------------:|:-------------:|:---------------:|-----------|
| 1       | First meeting with client                                     | To understand client problem and requirements                                                                                   | Planning     | 30 minutes    | 1 March         | A         |
| 2       | Write down success criteria                                   | To list down the first success criteria                                                                                         | Planning     | 20 minutes    | 2 March         | A         |
| 3       | Write problem definition                                      | Have problem definition which will identify who client is and the product that the client wants                                 | Planning     | 1 hour        | 2 March         | A         |
| 4       | Finalise success criteria                                     | Prepare a satisfactory criteria to present to client                                                                            | Planning     | 20 minutes    | 2 March         | A         |
| 5       | Meet with the client to discuss the success criteria.         | Receive the final approval to start creating the application                                                                    | Planning     | 20 minutes    | 2 March         | A         |
| 6       | Research and develop a rationale for the proposed solution.   | Finish rationale for proposed solution                                                                                          | Planning     | 30 minutes    | 3 March         | A         |
| 7       | Create system diagram                                         | Develop a clear idea of the hardware and software requirements for the proposed solution                                        | Planning     | 30 minutes    | 3 March         | B         |
| 8       | Create ER diagram including descriptions                      | Create an ER diagram that illustrates the tables and attributes of the solution with a brief explanation                        | Design       | 1 hour        | 3 March         | B         |
| 9       | Draw Wireframe diagram including descriptions                 | Wireframe diagram that is clear for the client to understand                                                                    | Design       | 1 hour        | 3 March         | B         |
| 10      | Draw UML diagram including descriptions                       | diagram illustrating the solution's classes, objects, and methods, as well as a brief explanation                               | Design       | 1.5 hours     | 3 March         | B         |
| 11      | Produce Flow diagrams including descriptions                  | flowcharts and a brief explanation for each section of the solution to obtain a clearer understanding of the code's proccess    | Design       | 3 hours       | 3 March         | B         |
| 12      | Code start screen                                             | have an inviting screen for client to use                                                                                       | Development  | 2 hours       | 3 March         | C         |
| 13      | Code login and registration system                            | A working login and register screen with Python and KivyMD with a GUI                                                           | Development  | 3 hours       | 4 March         | C         |
| 14      | Create show password function                                 | make the application more simple for use                                                                                        | Development  | 30 minutes    | 4 March         | C         |
| 15      | Create home/welcome screen according to the wireframe diagram | screen that contains all the available functions of the program                                                                 | Development  | 1 hours       | 4 March         | C         |
| 16      | Code transitions between screens                              | Python and KivyMD with a GUI are used to switch between screens.                                                                | Development  | 30 minutes    | 4 March         | C         |
| 17      | Create database                                               | insert and store inputs of users and items into the database                                                                    | Development  | 1 hour        | 4 March         | C         |
| 18      | Create add item screen                                        | a page that allows the user to enter food items into the 'items' table within the database                                      | Development  | 1 hour        | 4 March         | C         |
| 19      | Code add item screen                                          | functional program that allows the client to enter and save food item information                                               | Development  | 2 hours       | 4 March         | C         |
| 20      | Add date picker to add item system                            | a calendar that users can click on to input the date of expiry                                                                  | Development  | 30 minutes    | 4 March         | C         |
| 21      | Add check boxes                                               | make it more convenient for the client to classify the food into a category                                                     | Development  | 1 hour        | 4 March         | C         |
| 22      | Show add item screen to client                                | ensure that all elements the client wanted regarding the item are present                                                       | Evaluation   | 30 minutes    | 4 March         | A         |
| 23      | Create table to show items                                    | food item table that shows up on the database                                                                                   | Development  | 30 minutes    | 4 March         | C         |
| 24      | Code table screen                                             | screen that shows the table in the database                                                                                     | Development  | 1 hour        | 4 March         | C         |
| 25      | Code delete item function                                     | function that allows the client to remove the item from the database (for exmaple if they ate it)                               | Development  | 30 minutes    | 4 March         | C         |
| 26      | Code search item function                                     | allows the client to conveniently search up the object they are looking for by entering any element about the item in the table | Development  | 1 hour        | 4 March         | C         |
| 27      | Show list screen to client                                    | ensure that all elements the client wanted regarding the list are present                                                       | Evaluation   | 30 minutes    | 5 March         | A         |
| 28      | Create occupancy screens                                      | screens that each showcases the amount of space the food has filled up the fridge in a visually pleasing manor                  | Development  | 1 hour        | 5 March         | C         |
| 29      | Code occupancy function                                       | Allow the client to get a clear visual representation of how full the fridge is                                                 | Development  | 1 hour        | 5 March         | C         |
| 30      | Finalise program                                              | Test all the functions and beautify to present to the client                                                                    | Development  | 1 hour        | 5 March         | C         |
| 31      | Present application to client                                 | Get final approval for the application                                                                                          | Evaluation   | 1 hour        | 6 March         | A         |
| 32      | Finish test plans                                             | contains the procedures for testing the application as well as the expected results of each test.                               | Planning     | 2 hours       | 6 March         | B         |
| 33      | Write Criteria C                                              | Write the code descriptions as well as the specifics of the techniques implemented.                                             | Evaluation   | 2 hours       | 7 March         | C         |
| 34      | Film final video                                              | Video demonstration of all success criterias operating and functioning within the built application                             | Evaluation   | 1 hours       | 8 March         | D         |

# Criteria C: Development 

## Techniques used
  
1. OOP paradigm
2. KivyMD Library
3. Relational databases
4. SQLite, ORM
5. functions
6. if statements
7. for loop

## Computational thinking
  
1. decomposition
2. pattern recognition
3. abstraction 
4. algorithm design
  
## Python file: "project3.py"
  
  
### Setting up the file
  
```py
import sqlite3
from secure_password import encrypt_password
from kivymd.uix.pickers import MDDatePicker
from database_library import database_worker
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog  
```
The code imports several libraries that will be used to build the Refrigerator Manager application. The sqlite3 library is used to connect to and manipulate an SQLite database, which will be used to store the data about the food items stored in the fridge. The secure_password library is used to encrypt the user's password before storing it in the database, ensuring that it is secure. The kivymd library is used to build the graphical user interface (GUI) of the application, which will be user-friendly and easy to navigate.
  
### Database worker
 
The class called database_worker that initializes a connection to a SQLite database with the given name.  It abstract away the details of connecting to a database, allowing the developer to interact with the database through a simplified interface. This will allow me to focus on the more complex and important aspects of the application, such as the user interface and functionality.
  
This class will be useful in the implementation of my application as it allows for a simplified and organized way to store and retrieve data related to the food items stored in the fridge.
  
```py
class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
```  
In this code the __init__ function takes one argument, which is the name of the database file to connect to. The code uses the sqlite3 library to connect to the specified database file and creates a cursor object to interact with the database. This cursor object is used to execute SQL commands and queries on the connected database. The database_worker class abstracts away the implementation details of connecting to and interacting with a database. This allows me , for the rest of the code to simply create an instance of database_worker and call its methods without worrying about the underlying database implementation.
  
### Registering  

#### Checking for matches

```py  
db = database_worker("project3.db")
query = f"SELECT * from users WHERE username ='{uname}'"
result = db.search(query=query) 
if len(result) == 1: #user already exists
        dialog = MDDialog(title="User exists",
                          text=f"The username you entered: {self.ids.uname.text} already exists.")

        dialog.open()  
```  
 
The code is for checking whether a user with a given username already exists in the database. The first line of the code creates an object of the database_worker class and passes the name of the database file to it. The second line constructs a query to select all rows from the users table where the username matches the given username. The third line executes the query using the search() method of the database_worker class and stores the result in the result variable. The code then checks whether the length of the result is equal to 1, which means that a user with the given username already exists in the database "project3.db". If the condition is true, then a dialog box/ pop-up is created and opened using the MDDialog class of the KivyMD library. The dialog box displays a message to inform the user that the username already exists. 
  
This code can be used to prevent multiple users from registering with the same username, which could lead to confusion and disputes over food ownership, or the same person accidentally registering twice with different passwords. It ensures that each user has a unique username, which will facilitate efficient management of the refrigerator and improve the overall living environment.  
  
#### Hash

Hashing involves taking an input (such as a password) and converting it into a fixed-size string of characters using a mathematical function. The resulting string, known as a hash, is unique to the input, and it cannot be reversed to obtain the original password. The hash can be used as a secure way to store passwords in a database, as it is not possible to recover the original password from the hash, even if the database is compromised.  
  
```py
hash = encrypt_password(passwd)
db = database_worker("project3.db")
# add user to the database
query = f"INSERT into users ( password, username) values('{passwd}','{uname}')"
db.run_save(query)
db.close()  
```  

In this application, hashing is used to secure user passwords before storing them in the database. When a user creates an account or changes their password, the password is first hashed using the "encrypt_password" function before being added to the "users" table in the database. This ensures that even if the database is hacked, the hackers will not be able to retrieve the users' passwords as they are stored as hashes.

The "encrypt_password" function required algorithm design. It involves designing step-by-step instructions that can be followed to solve a specific problem or perform a specific task. In this case, the function takes a password as an input, applies a mathematical algorithm to it, and outputs a hash. The function is designed to be secure, meaning that it should produce a unique hash for each input and that it should be difficult to reverse-engineer the original password from the hash. By using secure hashing algorithms, the application ensures that user data is protected, which is essential for maintaining a harmonious living environment among housemates.
  
### loging in 

  
#### retrieving query
  
Retrieving query results in Python involves executing a SQL query on a database and retrieving the results into a Python data structure. This data can then be processed, manipulated, and displayed to the user in a variety of formats depending on the application's needs.  
  
```py  
def try_login(self):
    # Get the input username and password and print it
    uname = self.ids.uname.text
    passwd = self.ids.passwd.text
    query = f"SELECT * from users WHERE username='{uname}' and password='{passwd}'"
    db = database_worker("project3.db")
    result = db.search(query=query)
    db.close()
```  
This is a Python function called try_login that takes one argument self. It retrieves the values of the input fields with ids "uname" and "passwd" using the text attribute of their ids object. It then constructs a SQL query string using string formatting to search for a user in a SQLite database file "project3.db" using the retrieved username and password values. The function then creates a database_worker object passing the name of the database file and calls its search method with the constructed query string as an argument. The search method executes the query and returns a result set. The result set is assigned to the result variable. Finally, the function closes the database connection using the close method of the database_worker object.  

I utilised the algorithm design aspect of computational thinking, as it is outlining the steps to be taken in order to authenticate a user and query a database. I also used abstraction, as the code abstracts away the details of the database querying and instead presents a high-level interface for user authentication. This code would be used to authenticate users and provide them with access to their stored food items. It would ensure that only authorized users are able to access and modify the data, thus providing a secure and efficient tool for managing the fridge. 
  
### Toggling text's visibility
                          
```                          
def show_password(self): #make input password visible
  password_field = self.ids.passwd
  if password_field.password:
      password_field.password = False
      password_field.helper_text_mode = 'persistent'
  else:
      password_field.password = True
      password_field.helper_text_mode = 'on_focus'
```       
The code toggles the visibility of a password field in a user interface. Within the function, the password field is identified by its ID and stored in the "password_field" variable. An if statement is then used: If the password field is currently visible, the function sets the "password" attribute to "False" to hide the password and sets the "helper_text_mode" attribute to "persistent" to display a helper message and If the password field is currently hidden, the function sets the "password" attribute to "True" to show the password and sets the "helper_text_mode" attribute to "on_focus" to only display the helper message when the field is in focus.

I have used algorithm design by creating a step-by-step procedure for solving a problem. The function clearly defines the steps necessary for toggling the password field visibility and allows for easy modification or expansion of the code in the future. The proposed Refrigerator Manager application would benefit from this code by allowing users to easily toggle password visibility when necessary, enhancing their privacy and security when accessing the application.
  
### Adding an Item  
  
#### Inserting query

Overall, inserting queries in Python are a critical aspect of interacting with databases and are essential for building robust data-driven applications. This query allows data to be added to a specific table in the database. The insert query takes the form of a string that specifies the table name and the values to be inserted.   
  
```py
db = database_worker("project3.db")
# add items to the database
query = f"INSERT into items (owner, title, exp_date,type,location,notes) values('{owner}', '{title}','{exp_date}','{location}','{type}','{notes}')"
db.run_save(query)
db.close()  
```  
This is responsible for adding food items to the database for the application. The code uses a database worker object to execute an SQL query that inserts information about the food item which includes the owner, title, expiration date, type, location, and notes. I utilised algorithm design by creating a process that outlines a set of instructions to insert data into the database. Algorithm design involves identifying the steps needed to solve a problem or complete a task. 
  
This process enables the refrigerator manager application to store and retrieve data effectively, ensuring a seamless user experience. By utilizing algorithm design, the application can perform create, read, update, and delete operations effectively, providing an efficient tool for managing the fridge.
  
#### DatePicker
                          
```py                           
def date(self): # to select expiry date
    date_dialog = MDDatePicker()
    date_dialog.bind(on_save=self.on_save)
    date_dialog.open()
def on_save(self,instance, value, date_range): #to save the selected date into the database
    self.selected_date=value
    print(value)
    self.ids.exp_date.text = f"{value}"
```
  
These are two methods related to selecting an expiration date for food items in the proposed Refrigerator Manager application. 

The "date" method is responsible for creating a date picker dialog box that is displayed to the user when called. It creates an instance of the MDDatePicker class which provides a graphical date picker widget for the user. The bind() method is used to attach an event listener to the on_save event, which is triggered when the user selects a date from the widget. The second method, "on_save," saves the selected date into the database and updates the text field displaying the expiration date. It is called when the user selects a date from the MDDatePicker widget. The value parameter holds the selected date in the format "yyyy-mm-dd". This method sets the selected_date attribute to the selected value and prints it to the console for debugging purposes. It also sets the exp_date text field in to display the selected date using string interpolation. 
  
I made use of the MDDatePicker, which simplifies the process of selecting a date and enhances the user experience of the application. I used abstraction in this code in regards to simplifying complex date selection functionality, making it easy for users to select and record expiration dates for their food items. Moreover, it highlights use of algorithm design and decomposition in creating a smooth and efficient user experience. By enabling users to quickly and easily record expiration dates for their food items, this feature contributes to the overall efficiency and reliability of the application in managing fridge contents.
  
  
#### Checkboxes

```py                          
def checkbox_click_1(self, checkbox, value, location):
    if value:  # if the check is true
        self.selected_location = location
        print(location)
        self.ids.location.text = f"{location}"
```                          

The checkbox_click_1() function is called when the user clicks on a checkbox associated with a specific location. It takes three arguments: checkbox, value, and location. The checkbox argument is the checkbox object that was clicked on, value is the state of the checkbox (either True or False), and location is the name of the location associated with the checkbox. If the value of the checkbox is True, the function sets the selected_location variable to the value of the location argument, and then updates the text of the location input field to display the selected location using string formatting. The print(location) statement is used for debugging purposes and can be removed once the code is working correctly.

For this code, I have used decomposition regarding the process of selecting a location into a single function that can be reused multiple times throughout the application. This will allow users to easily categorize the item based on the location. I used checkboxes instead of textfeild because there are only a few inputs they can enter, unlike the name of a food item, having the location be in chackboxes makes it quicker for the user to just simply select rather than having to waste time by typing it up. 
  
### The table
  
```py
def on_pre_enter(self, *args):
    # before the screen in shown, the code runs
    self.data_table = MDDataTable(
        size_hint=(.8, .7),
        pos_hint={"center_x": .5, "center_y": .5},
        use_pagination=True,
        check=True,
        column_data=[("id", 35), ("owner", 25),
                     ("title", 30), ("Exp date", 40), ("location", 30),
                     ("type", 40), ("notes",50)]
    )
    # add the table
    self.data_table.bind(on_row_press=self.row_pressed)
    self.data_table.bind(on_check_press=self.check_pressed)
    self.add_widget(self.data_table)
    self.update()  
```  
The on_pre_enter method is used in KivyMD to specify the actions to be taken before a screen is shown. In this case, the method creates a MDDataTable object, which is a widget that displays data in a table format. The MDDataTable is customized with specific attributes like size_hint, pos_hint, use_pagination, check, and column_data to determine the size and location of the table, whether or not pagination will be used, if checkboxes will be displayed, and the column headers and their sizes, respectively. The MDDataTable object is then added to the current screen using the add_widget method, which adds a child widget to the current screen. Finally, the update method is called to update the screen with the newly added widget.

This code could be used to display a table of food items stored in the refrigerator, allowing users to easily add, remove, and search for items.A function on_pre_enter that is called before a screen is displayed. This function creates a MDDataTable widget with specific column data and bindings for row and check presses. The widget is added to the screen, and the update method is called to populate the table with data. I have utilised decomposition to break down the task of creating a table widget into smaller, more manageable pieces. It also highlights the importance of abstraction, where the complexity of creating a table widget is abstracted away from the user, making it easier to use. As well as calculating the size of each column in order for all the data to be presented to the client in an easy-to-understand. The user-friendly interface of the MDDataTable widget would be a key feature of the application, as it would enable all housemates to use the app effectively, regardless of their technical skill level. 
  
  
### Deleting items
  
```py
rows_checked = self.data_table.get_row_checks()
db = database_worker("project3.db")
for r in rows_checked:
    id = r[0]
    query = f"delete from items where id = {id}"
    db.run_save(query)
db.close()  
```
 
This performs a database operation on selected rows in a data table. The code first retrieves the rows that have been checked in the data table using the "get_row_checks()" method. The code then creates a connection to the database using a custom database_worker class by a for loop, passing in the name of the database file. The code then loops through each row that has been checked and retrieves the id value of the row, which is then used to construct a SQL DELETE query. The "run_save()" method of the database_worker class is then called, passing in the SQL query. Finally, the database connection is closed. This code has taught me to use decomposition to break down the problem into smaller tasks, pattern recognition to identify a common operation that needs to be performed on each selected row, and algorithm design to perform the necessary database operations efficiently.
  
### Searching for item(s)  

```py  
if self.ids.searchtext.text:
    db = database_worker("project3.db")
    searchword = self.ids.searchtext.text
    # any information regarding the item
    query = f"SELECT * FROM items WHERE owner='{searchword}' or title='{searchword}' or " \
            f"exp_date='{searchword}' or location ='{searchword}' or type='{searchword}' or notes='{searchword}'"
    data = db.search(query)
    db.close()
    self.data_table.update_row_data(None, data)
else:
    self.update()  
```
This if statement checks if the search text input is not empty. If it's not empty, it retrieves the search text, creates a query to search the database for any item whose owner, title, expiry date, location, type, or notes match the search text. I used the "or" in the query instead of "and" in order to make it more easy for the client to look up an item, rather than having to memorise all aspects regarding the item. It then retrieves the search results and updates the data table with the search results. On the other hand, if the search text input is empty, it updates the data table with all items in the database by calling the update() method. 
  
I used pattern recognition to identify the need to perform a search on the database since thhe more items are added, the harder it will be for the client to find their item and defeats the purpose of having the program be simple and convemient. Abstraction was used to hide the details of the database query and search functionality, thus making the code more modular and easy to understand. The algorithm design in this code involves retrieving and updating data from a database based on user input. 
    
#### Checking the occupancy
  
```py  
full = 50 #max capacity
db = sqlite3.connect("project3.db")
c = db.cursor()
c.execute("SELECT COUNT(*) FROM items") #how many items are there
amount = c.fetchone()[0]
db.close()
percentage = amount / full * 100
print(percentage)
if percentage == 0:
    self.parent.current = "emptyScreen"
if percentage <= 25:
    self.parent.current = "quarterScreen"  
```  
                   
This calculates the percentage of capacity that is being used in the database in my case, the fridge. I started by setting a maximum capacity of the fridge at 50 items, and then connects to the database using SQLite3. The code then retrieves the number of items in the database using a SELECT COUNT(*) query, which returns a single value representing the number of rows in the "items" table. The code then closes the database connection and calculates the percentage of capacity that is being used by dividing the number of items by the maximum capacity and multiplying by 100. At first I struggled with coming up with how to present the calculated percentage in an interesting manor, but through using pattern recognition, I decided to create screens each representing a set amount of percentage - which reflecting back, may not be the most efficient and a pop up may be more efficient since it doesn't require me to impliment another screen. An if statement is then used to match the calculated percentage to the screens that the user will be directed to depending on the calculated results. This code would help users monitor the status of the refrigerator and take necessary actions to prevent overcrowding or waste.                  
                   
## Kivy File: "project3.kv"

### Screen Manager                          
```py
ScreenManager:
    StartScreen:
        name: "StartScreen"

    LoginScreen:
        name: "LoginScreen"
```
The ScreenManager provides a simple and efficient way to organize and switch between different screens in an application. Each screen is defined using a custom class that inherits from the Screen class, which allows for custom attributes and functionality to be defined for each screen. Abstraction was used 
to make the process of managing different screens and easily switch between them easier for me.               
                                     
### MDTextField
                          
```py
MDTextField:
  id: uname
  icon_left: "account"
  hint_text: "enter username"
  username: True
  helper_text_mode: "on_error"
  size_hint: .8, .1
  pos_hint: {"center_x":.5}                          
 ```   
                   
The code creates an MDTextField widget that allows users to input text. The MDTextField is defined with an ID of "uname" and several attributes such as icon_left, hint_text, username, and helper_text_mode. The username attribute is set to True, indicating that the text field is intended for username input. The helper_text_mode attribute is set to "on_error," which displays an error message if the input provided is invalid. Additionally, the use of helper_text_mode highlights algorithm design by providing a specific feedback mechanism for users in the event of an error.
                   
                   
### Float Layout and MDRectangleFlatIconButton

```py
FloatLayout:
  MDRectangleFlatIconButton:
      id: newfood
      text: "add item"
      text_color: "white"
      icon: "cookie-plus"
      icon_color: "white"
      md_bg_color: "#FF6B6B"
      on_press: root.parent.current = "AddItemScreen"
      size_hint: .15, .05
      pos_hint: {"center_x":.433,"center_y":.78}                          
```                 

A FloatLayout provides a flexible container for placing and organizing widgets. In this case, I wanted to make the display more visually pleasing and interesting, so, I used the FloatLayout inorder to positioning my button inside each shelf of the fridge - as if they're taking out an object from it. Through pattern recognition, the icon attribute of the MDRectangleFlatIconButton helps in enhancing the distinction between each button since there are multiple. I did this by copying the code and pasting but changing the icon, position, color, and size in order to make it easier for the client to easily distinguish the difference between each option buttons.               
                   
### MDCheckbox

```py                          
MDCheckbox:
      id: meat
      group: 'group2' #this group is so that all the checkboxes are linked and only one can be selected
      size_hint: None, None
      size: dp(48), dp(48)
      active: True
      on_active: root.checkbox_click_1(self, self.active, "meat")
      pos_hint: {"center_y":.5}
  MDLabel:
      text: 'meat'
      pos_hint: {"center_y":.5}
      font_size:20                          
```   
                   
The MDCheckbox is a custom Checkbox that implements Material Design guidelines. The code assigns an ID of "meat" to the MDCheckbox and specifies its size and position. By setting the "group" attribute to "group2," this code ensures that only one checkbox in the group can be selected at a time. This implementation was through my use pattern recognition as I could copy this code structure and paste it to create more checkboxes whilst ensuring that only 1 could be selected.

### MDBoxLayout
                   
                   
                          
[^1]: Python Software Foundation. (2021). Python Usage. https://www.python.org/about/success/
[^2]: Rose, J. (2020). Why Python is so popular with developers: 3 reasons the language has exploded. TechRepublic. https://www.techrepublic.com/article/why-python-is-so-popular-with-developers-3-reasons-the-language-has-exploded/
[^3]: KivyMD. (n.d.). KivyMD: Introduction. https://kivymd.readthedocs.io/en/latest/introduction/
[^4]: Kivy. (n.d.). User Interface - Widgets. https://kivy.org/doc/stable/gettingstarted/widgets.html
[^5]: Smith, L. (2021). Flutter vs Kivy: Which One is Better for Cross-Platform App Development? Medium. https://levelup.gitconnected.com/flutter-vs-kivy-which-one-is-better-for-cross-platform-app-development-f38d73624e6b
[^6]: SQLite. (n.d.). SQLite Features. https://www.sqlite.org/features.html
[^7]: IBM. (2021). IBM Db2. https://www.ibm.com/products/db2-database
[^8]: SQL Tutorial. (n.d.). What is SQLite? https://www.sqlitetutorial.net/what-is-sqlite/
