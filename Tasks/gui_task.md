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

<sub> Fig. Shows the result for example 1
  
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


<sub> Fig. Shows the result for example 2
    

## Example 3

### Code

gui_examples.py

```py
    
```
gui_examples.kv

```py
    
```

### Evidence
    


<sub> Fig. Shows the result for example 3

## Task 1 

<img width="553" alt="Screen Shot 2566-01-29 at 15 54 37" src="https://user-images.githubusercontent.com/111941936/215310295-f40239de-07a7-4b9a-a6f3-fa33e6da3e91.png">

<sub> Fig. Shows the task

Create a Currency Converter GUI that takes an integer representing an amount from your home country currency and converts it into USD and JPY rounded to 2 decimals.

⚠️ Remember to validate user inputs

## Code
  
## Evidence
