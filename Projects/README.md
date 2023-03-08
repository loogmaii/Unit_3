# Kris' Fridge Manager

![fridge phone](https://user-images.githubusercontent.com/111941936/221760786-ab80eca0-ab94-4039-a442-f05c970ddca2.jpeg)

<sub> Fig.1 shows @coen_pohl_design's illustration on instagram

# Criteria A: Planning

## Problem definition

Kris is a grade 11 student at UWC ISAK Japan, residing in a boarding house. Despite enjoying living there, she has noticed a significant problem with the shared refrigerator. The fridge is disorganized, with no clear indication of which items belong to each housemate. Additionally, expired food is left to spoil, leading to a foul odor in the house and arguments among housemates over food ownership. As the residential assistant, Kris feels a sense of responsibility to find a solution to this problem. She has asked Mai to develop a Refrigerator Manager application to keep track of the items stored in the fridge. This application will record details such as the owner, food type, location of the item in the fridge, expiration date, and any additional notes to then be displayed in a simple format. To ensure privacy and security for all housemates, the program will have a secure registration system.

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

To effectively address my client's issue with the shared refrigerator, I propose developing a Refrigerator Manager application using Python, KivyMD, and SQLite. This solution will allow each housemate to record important details about the food they store in the fridge, including the food's owner, type, location, and expiration date. The application's user-friendly interface will make it easy for users to add and remove food items, search for specific items, and view a presented table of all stored food items. To ensure the privacy and security of the housemates' information, the app will have a secure registration system.

I chose to use the Python language to develop the application because it is a popular and commonly used programming language that is rapidly growing in the tech industry. Its widespread use makes it easier for many developers to understand compared to other languages like C or Javascript, which would benefit the application's development [^1]. Additionally, Python has a wide range of libraries available that can be easily accessed using basic syntax. Overall, the Python programming language is suitable for developing the client's desired application [^2].

To develop the application, I will use KivyMD as the framework for its graphical user interface. KivyMD is a multi-platform application development framework that is easy to learn and work with [^3]. Its pre-built user-interface elements and styles can be easily customized and integrated into Kivy-based applications, saving time and effort in developing the application's interface [^4]. While there are other alternatives such as Flutter or PyQt, I have chosen KivyMD for its ease of use, customizability, and compatibility [^5].

For the application's database management system, I have selected SQLite. SQLite is a free database that requires no additional server process and is implemented on a single file [^6]. It is designed to handle large amounts of data efficiently, making it suitable for storing all kinds of information related to the stored food items . SQLite continuously updates its content, minimizing the risk of lost data in the event of a power failure or crash. Its cross-platform compatibility will enable future developers to expand the program to other platforms [^7]. In comparison to other databases available, SQLite is reliable, efficient, cost-friendly, and easy to use [^8].
  


Overall, the proposed Refrigerator Manager application will provide an efficient and reliable tool for managing the fridge and preventing disputes among housemates over food ownership, ensuring a more harmonious living environment.

  
  | Task No |        Planned Action       |                                       Planned Outcome                                      | Time estimate | Target completion date | Criterion |   |
|:-------:|:---------------------------:|:------------------------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------:|---|
| 1       | First meeting with client   | To understand client problem and requirements                                              | Planning      | 30 minutes             | 5 March   | A |
| 2       | Write down success criteria | To list down the first success criteria                                                    | Planning      | 20 minutes             | 6 March   | A |
| 3       | Write problem definition    | Have problem definition which will identify who client is and the product that client want | Planning      | 1 hour                 | 6 March   |   |

[^1]: Python Software Foundation. (2021). Python Usage. https://www.python.org/about/success/
[^2]: Rose, J. (2020). Why Python is so popular with developers: 3 reasons the language has exploded. TechRepublic. https://www.techrepublic.com/article/why-python-is-so-popular-with-developers-3-reasons-the-language-has-exploded/
[^3]: KivyMD. (n.d.). KivyMD: Introduction. https://kivymd.readthedocs.io/en/latest/introduction/
[^4]: Kivy. (n.d.). User Interface - Widgets. https://kivy.org/doc/stable/gettingstarted/widgets.html
[^5]: Smith, L. (2021). Flutter vs Kivy: Which One is Better for Cross-Platform App Development? Medium. https://levelup.gitconnected.com/flutter-vs-kivy-which-one-is-better-for-cross-platform-app-development-f38d73624e6b
[^6]: SQLite. (n.d.). SQLite Features. https://www.sqlite.org/features.html
[^7]: IBM. (2021). IBM Db2. https://www.ibm.com/products/db2-database
[^8]: SQL Tutorial. (n.d.). What is SQLite? https://www.sqlitetutorial.net/what-is-sqlite/
