# GUI Task

## Example 1

### Code

gui_example1.py

```py
from kivymd.app import MDApp

class gui_example1(MDApp):
    def build(self):
        return

test = gui_example1()
test.run()
```
gui_example1.kv

```py
Screen:
    size: 500, 500

    MDLabel:
        text: "Hello World"
        halign: "center"
        font_size: "34pt"
```

### Evidence

<img width="831" alt="Screen Shot 2566-01-29 at 21 22 52" src="https://user-images.githubusercontent.com/111941936/215325795-0b662080-2a54-409b-98e0-f699df32aa94.png">

<sub> Fig.1 Shows the result for example 1
  
## Example 2

### Code

gui_examples.py

```py
from kivymd.app import MDApp

class gui_examples(MDApp):
    def build(self):
        return

    def close(self):
        exit()

test = gui_examples()
test.run()
```
gui_examples.kv

```py
Screen:
    size: 500, 500
    MDBoxLayout:
        pos_hint: {"center_x":0.5}
        size_hint: .7, .7
        md_bg_color: "#fdfcdc"
        orientation: "vertical"

        MDLabel:
            text: "Hello World"
            halign: "center"
            font_size: "34pt"

        MDRaisedButton:
            text: "Close"
            size_hint: .5, 1
            font_size: "34pt"
            md_bg_color: "#f07167"
            pos_hint: {"center_x":0.5}
            on_press:
                app.close()
```

### Evidence
    
<img width="831" alt="Screen Shot 2566-01-29 at 21 53 53" src="https://user-images.githubusercontent.com/111941936/215327471-00c00948-bfa5-4e3b-8b1d-a65f76b2a0e4.png">


<sub> Fig.2 Shows the result for example 2
    

## Example 3

### Code

gui_examples.py

```py
from kivymd.app import MDApp

class gui_examples(MDApp):
    def build(self):
        return

    def change_author(self, name):
        self.root.ids.title.text = f"Author {name}"

test = gui_examples()
test.run()    
```
gui_examples.kv

```py
Screen:
    size:500, 500
    MDLabel:
        id: title
        text: ""
        font_style: "H1"
        pos_hint: {"center_y": .8}
        halign: "center"

    MDBoxLayout:
        pos_hint: {"center_x":0.5,"center_y": .5}
        size_hint: .7, .2
        orientation: "horizontal"

        MDChip:
            text: "Author A"
            pos_hint: {"center_y": .5}
            icon_right: "close-circle-outline"
            md_bg_color: "#003049"
            text_color: "#FFFFFF"
            on_press: app.change_author("A")

        MDChip:
            text: "Author B"
            pos_hint: {"center_y": .5}
            icon_right: "close-circle-outline"
            md_bg_color: "#D62828"
            on_press: app.change_author("B")

        MDChip:
            text: "Author C"
            pos_hint: {"center_y": .5}
            icon_right: "close-circle-outline"
            md_bg_color: "#F77F00"
            on_press: app.change_author("C")

        MDChip:
            text: "Author D"
            pos_hint: {"center_y": .5}
            icon_right: "close-circle-outline"
            md_bg_color: "#FCBF49"
            on_press: app.change_author("D")

        MDChip:
            text: "Author E"
            pos_hint: {"center_y": .5}
            icon_right: "close-circle-outline"
            md_bg_color: "#EAE287"
            icon_left: "map-marker"
            on_press: app.change_author("E")
    
```

### Evidence
    
<img width="831" alt="Screen Shot 2566-01-29 at 22 29 19" src="https://user-images.githubusercontent.com/111941936/215329438-732df18d-bbf7-478e-8747-faeef7fc1580.png">

<sub> Fig.3 Shows the result for example 3

## Task 1 

<img width="553" alt="Screen Shot 2566-01-29 at 15 54 37" src="https://user-images.githubusercontent.com/111941936/215310295-f40239de-07a7-4b9a-a6f3-fa33e6da3e91.png">

<sub> Fig.4 Shows the task

Create a Currency Converter GUI that takes an integer representing an amount from your home country currency and converts it into USD and JPY rounded to 2 decimals.

⚠️ Remember to validate user inputs

## Code

gui_task.py    
    
```py
from kivymd.app import MDApp

class gui_task(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input = 0

    def build(self):
        return

    def val_input(self):
        if not self.root.ids.input.text.isdigit():
            self.root.ids.final_amount.text = "Please enter a valid number"
        number = int(self.root.ids.input.text)
        self.input = number

    def convert_usd(self):
        self.converted = round(self.input * 0.031, 2)
        self.root.ids.final_amount.text = f" {self.converted} USD"

    def convert_jpy(self):
        self.converted = round(self.input * 3.97, 2)
        self.root.ids.final_amount.text= f" {self.converted} JPY"


app = gui_task()
app.run()
```
gui_task.kv

```py    
Screen:
    size: 500,500

    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.6
        pos_hint: {'center_x':.5, 'center_y':.6}

        MDLabel:
            id: title
            text: "Currency Converter"
            font_style: "H4"
            pos_hint: {"center_x": .5}
            halign: "center"

        MDTextField:
            id: input
            hint_text: "Enter Amount in THB"
            pos_hint: {'center_x':.5}
            size_hint: .7, .35
            on_text:
                app.val_input()

        MDBoxLayout:
            id: currency_box
            orientation: 'horizontal'
            size_hint:1,.6
            pos_hint: {'center_x':.5, 'center_y':.5}


            MDLabel:
                id : click_con
                text: "CLICK TO CONVERT"
                halign: 'center'
                size_hint: .275, .35
                pos_hint: {'center_x':.5,'center_y': .5}

            MDBoxLayout:
                id: button_result
                orientation:"vertical"
                size_hint: .3, 1


                MDBoxLayout:
                    id: buttons
                    orientation: "horizontal"
                    size_hint: .55, 1
                    pos_hint: {'center_x':.7, 'center_y':.1}

                    MDRaisedButton:
                        id: usd
                        text: "USD"
                        pos_hint: {"center_x": .4, "center_y": .45}
                        on_release: app.convert_usd()
                        md_bg_color:"#000066"

                    MDRaisedButton:
                        id: jpy
                        text: "JPY"
                        pos_hint: {"center_x": .75, "center_y": .45}
                        on_release: app.convert_jpy()
                        md_bg_color:"#FF0000"

                MDLabel:
                    id: final_amount
                    text: "0"
                    halign: 'center'
                    text_color: "#000000"
                    size_hint: .6, 1
                    pos_hint: {'center_x':.55}
                    font_size:70

```
    
## Evidence

<img width="806" alt="Screen Shot 2566-01-31 at 12 50 30" src="https://user-images.githubusercontent.com/111941936/215658525-794e1a7f-bb18-4d08-98ba-571f8a661a8a.png">

<sub> Fig.5 Shows the program
    
<img width="806" alt="Screen Shot 2566-01-31 at 12 50 51" src="https://user-images.githubusercontent.com/111941936/215658588-3bf9e4d0-cc70-4aed-b00a-f2b8d25dfc9f.png">
<sub> Fig.6 Shows the input converted to USD
    
<img width="806" alt="Screen Shot 2566-01-31 at 12 51 30" src="https://user-images.githubusercontent.com/111941936/215658663-dba01607-47bf-4905-ba44-3c52414e3da7.png">
<sub> Fig.7 Shows the input converted to JPY
