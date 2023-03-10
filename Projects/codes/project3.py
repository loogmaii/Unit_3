mport sqlite3
from secure_password import encrypt_password
from kivymd.uix.pickers import MDDatePicker
from database_library import database_worker
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

class StartScreen(MDScreen):
    pass

class HomeScreen(MDScreen):
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

class LoginScreen(MDScreen):
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

class RegistrationScreen(MDScreen):
    def try_register(self):
        uname = self.ids.uname.text
        passwd = self.ids.passwd.text
        passwd_check = self.ids.passwd_check.text
        # Check if username exists
        db = database_worker("project3.db")
        query = f"SELECT * from users WHERE username ='{uname}'"
        result = db.search(query=query)
        if len(result) == 1: #user already exists
            dialog = MDDialog(title="User exists",
                              text=f"The username you entered: {self.ids.uname.text} already exists.")
            dialog.open()
            self.ids.uname.text = ""
            self.ids.passwd.text = ""
            self.ids.passwd_check.text = ""

        if passwd != passwd_check:
            self.ids.passwd_check.error = True
            self.ids.passwd.error = True
        else:
            hash = encrypt_password(passwd)
            db = database_worker("project3.db")
            # add user to the database
            query = f"INSERT into users ( password, username) values('{passwd}','{uname}')"
            db.run_save(query)
            db.close()
            print("Registration completed")
            dialog = MDDialog(title="registered",
                              text=f"{self.ids.uname.text} registered!")
            dialog.open()
            self.parent.current = "LoginScreen"

class AddItemScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected_date=None
        self.selected_location = None
        self.selected_type = None

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
    def checkbox_click_1(self, checkbox, value, location):
        if value:  # if the check is true
            self.selected_location = location
            print(location)
            self.ids.location.text = f"{location}"

    #check boxes for selecting the location
    def checkbox_click_2(self, checkbox, value, type):
        if value:  # if the check is true
            self.selected_type = type
            print(type)
            self.ids.type.text = f"{type}"

class ListScreen(MDScreen):
    #displaying
    data_table = None  # = empty/no value
    def update(self):
        db = database_worker("project3.db")
        query = "SELECT * FROM items"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)

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

    def delete(self):
        # ticked check boxes
        rows_checked = self.data_table.get_row_checks()
        db = database_worker("project3.db")
        for r in rows_checked:
            id = r[0]
            query = f"delete from items where id = {id}"
            db.run_save(query)
        db.close()
        self.update()
        dialog = MDDialog(title="deleted",
                          text=f"item(s) deleted!")
        dialog.open()

    def row_pressed(self, table, row):
        print("a row was pressed", row)

    def check_pressed(self, table, current_row):
        print("a row was checked", current_row)

    def try_search(self):
        #search for items
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

class emptyScreen(MDScreen):
    pass

class quarterScreen(MDScreen):
    pass

class halfScreen(MDScreen):
    pass

class sevfiveScreen(MDScreen):
    pass

class FullScreen(MDScreen):
    pass

class project3(MDApp):
    def build(self):
        return

#table for the food items
create = """CREATE TABLE if not exists items(
    id INTEGER PRIMARY KEY,
    owner text,
    title text,
    exp_date text,
    location text,
    type text,
    notes text
    
)"""

create = """CREATE TABLE if not exists users(
    id INTEGER PRIMARY KEY,
    password text,
    username text
)"""
db = database_worker("project3.db")
db.run_save(create)
db.close()

test = project3()
test.run()
