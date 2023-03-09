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
  
<img width="1184" alt="Screen Shot 2566-03-10 at 03 43 30" src="https://user-images.githubusercontent.com/111941936/224124245-414a2103-76bd-4790-821b-d31e419dbbe5.png">

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
  
## Coding in Python
  
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
  
```py
def show_occupancy(self):
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
    elif percentage <= 50:
        self.parent.current = "halfScreen"
    elif percentage <= 100:
        self.parent.current = "sevfiveScreen"
    elif percentage == 100:
        self.parent.current = "fullScreen"  

    def try_login(self):
        # Get the input username and password and print it
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        query = f"SELECT * from users WHERE username='{uname}' and password='{passwd}'"
        db = database_worker("project3.db")
        result = db.search(query=query)
        db.close()
        if len(result) == 1:
            print("Login successful")
            self.parent.current = "HomeScreen"
        else:
            print("Login incorrect")
            self.ids.passwd.helper_text = "Check your password"
            self.ids.passwd.error = True
            self.ids.uname.helper_text = "Check your username"
            self.ids.uname.error = AttributeError
            self.ids.uname.text = ""
            self.ids.passwd.text = ""
            #pop up
            dialog = MDDialog(title="User not found",
                              text=f"Username '{self.ids.uname.text}' does not have an account.")
            dialog.open()

    def show_password(self): #make input password visible
        password_field = self.ids.passwd
        if password_field.password:
            password_field.password = False
            password_field.helper_text_mode = 'persistent'
        else:
            password_field.password = True
            password_field.helper_text_mode = 'on_focus'
                          
    def add_item(self):
        owner = self.ids.owner.text
        title = self.ids.title.text
        exp_date = self.selected_date
        location = self.selected_location
        type = self.selected_type
        notes = self.ids.notes.text
        db = database_worker("project3.db")
        # add items to the database
        query = f"INSERT into items (owner, title, exp_date,type,location,notes) values('{owner}', '{title}','{exp_date}','{location}','{type}','{notes}')"
        db.run_save(query)
        db.close()
        print("item added")
        self.parent.current = "HomeScreen"
        # pop up
        dialog = MDDialog(title="Item added",
                          text=f"{self.ids.owner.text}'s {self.ids.title.text} has been added!")
        dialog.open()
    def date(self): # to select expiry date
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()
    def on_save(self,instance, value, date_range): #to save the selected date into the database
        self.selected_date=value
        print(value)
        self.ids.exp_date.text = f"{value}"

    #check boxes for categorising the food
    def checkbox_click_type(self, checkbox, value, location):
        if value:  # if the check is true
            self.selected_location = location
            print(location)
            self.ids.location.text = f"{location}"
                          
```
  
## Coding in Kivy
  
```py
ScreenManager:
    StartScreen:
        name: "StartScreen"

    LoginScreen:
        name: "LoginScreen"

    RegistrationScreen:
        name: "RegistrationScreen"

    HomeScreen:
        name: "HomeScreen"

    AddItemScreen:
        name: "AddItemScreen"

    ListScreen:
        name: "ListScreen"

    emptyScreen:
        name: "emptyScreen"

    quarterScreen:
        name: "quarterScreen"

    halfScreen:
        name: "halfScreen"

    sevfiveScreen:
        name: "sevfiveScreen"

    FullScreen:
        name: "FullScreen"  
```
  
[^1]: Python Software Foundation. (2021). Python Usage. https://www.python.org/about/success/
[^2]: Rose, J. (2020). Why Python is so popular with developers: 3 reasons the language has exploded. TechRepublic. https://www.techrepublic.com/article/why-python-is-so-popular-with-developers-3-reasons-the-language-has-exploded/
[^3]: KivyMD. (n.d.). KivyMD: Introduction. https://kivymd.readthedocs.io/en/latest/introduction/
[^4]: Kivy. (n.d.). User Interface - Widgets. https://kivy.org/doc/stable/gettingstarted/widgets.html
[^5]: Smith, L. (2021). Flutter vs Kivy: Which One is Better for Cross-Platform App Development? Medium. https://levelup.gitconnected.com/flutter-vs-kivy-which-one-is-better-for-cross-platform-app-development-f38d73624e6b
[^6]: SQLite. (n.d.). SQLite Features. https://www.sqlite.org/features.html
[^7]: IBM. (2021). IBM Db2. https://www.ibm.com/products/db2-database
[^8]: SQL Tutorial. (n.d.). What is SQLite? https://www.sqlitetutorial.net/what-is-sqlite/
