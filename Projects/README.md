# Kris' Fridge Manager

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

## Proposed Solution

My proposed application will be a Refrigerator Manager that will enable each housemate to record details of the food they store in the fridge. The application will have a user-friendly interface that will allow users to add and remove food items easily, as well as search for specific items they are looking for from a presented table. This solution will provide a reliable and efficient tool for managing the fridge and preventing disputes among housemates over food ownership, ensuring a more harmonious living environment. The application will be constructed using Pycharm, the Python language, and the KivyMD Language. This project will take 6 weeks and will be evaluated according to the criteria set above.

## Rationale for proposed solution

I propose developing a Refrigerator Manager application using Python, KivyMD, and SQLite. This solution will allow each housemate to record important details about the food they store in the fridge, including the food's owner, type, location, and expiration date. The application's user-friendly interface will make it easy for users to add and remove food items, search for specific items, and view a presented table of all stored food items. To ensure the privacy and security of the housemates' information, the app will have a secure registration system.

I chose to use the Python language to develop the application because it is a popular and commonly used programming language that is growing in the tech industry. Its widespread use makes it easier for many developers to understand compared to other languages like C or Javascript, which would benefit the application's development [^1]. Additionally, Python has a wide range of libraries available that can be easily accessed using basic syntax. Overall, the Python programming language is suitable for developing the client's desired application [^2].

Furthermore, I will use KivyMD as the framework for its graphical user interface. KivyMD is a multi-platform application development framework that is easy to learn and work with [^3]. Its pre-built user-interface elements and styles can be easily customized and integrated into Kivy-based applications, saving time and effort in developing the application's interface [^4]. While there are other alternatives such as Flutter or PyQt, I have chosen KivyMD for its ease of use, customizability, and compatibility [^5].

For the application's database management system, I have selected SQLite. SQLite is a free database that requires no additional server process and is implemented on a single file [^6]. It is designed to handle large amounts of data efficiently, making it suitable for storing all kinds of information related to the stored food items . SQLite continuously updates its content, minimizing the risk of lost data in the event of a power failure or crash. Its cross-platform compatibility will enable future developers to expand the program to other platforms [^7]. In comparison to other databases available, SQLite is reliable, efficient, cost-friendly, and easy to use [^8].
  
Overall, the proposed Refrigerator Manager application will provide an efficient and reliable tool for managing the fridge and preventing disputes among housemates over food ownership, ensuring a more harmonious living environment.


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

[^1]: Python Software Foundation. (2021). Python Usage. https://www.python.org/about/success/
[^2]: Rose, J. (2020). Why Python is so popular with developers: 3 reasons the language has exploded. TechRepublic. https://www.techrepublic.com/article/why-python-is-so-popular-with-developers-3-reasons-the-language-has-exploded/
[^3]: KivyMD. (n.d.). KivyMD: Introduction. https://kivymd.readthedocs.io/en/latest/introduction/
[^4]: Kivy. (n.d.). User Interface - Widgets. https://kivy.org/doc/stable/gettingstarted/widgets.html
[^5]: Smith, L. (2021). Flutter vs Kivy: Which One is Better for Cross-Platform App Development? Medium. https://levelup.gitconnected.com/flutter-vs-kivy-which-one-is-better-for-cross-platform-app-development-f38d73624e6b
[^6]: SQLite. (n.d.). SQLite Features. https://www.sqlite.org/features.html
[^7]: IBM. (2021). IBM Db2. https://www.ibm.com/products/db2-database
[^8]: SQL Tutorial. (n.d.). What is SQLite? https://www.sqlitetutorial.net/what-is-sqlite/
