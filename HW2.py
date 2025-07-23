#Melody Warfel 2025
#Homework 2, CS314

#imports
import tkinter

#internal variables
x = 25 #x coord (1-50)
y = 25 #y coord (1-50)
max = 50
min = 1

#event handlers
def move_up():
    global y
    y = y + 1
    update_location()

def move_down():
    global y
    y = y - 1
    update_location()

def move_left():
    global x
    x = x - 1
    update_location()

def move_right():
    global x
    x = x + 1
    update_location()

def update_location():
    global x
    global y
    if x < 1 or x > 50:
        x = 1
    if y < 1 or y > 50:
        y = 1
    location.set("(" + str(x) + "," + str(y) + ")")

#setup
#window setup
window = tkinter.Tk() #main window object
window.title("Homework 2") #set title
window.geometry("300x100") #set WxH
#window variables
location = tkinter.StringVar() #allows label to be updated with .set()
buttonwidth=10

#frames & packing
#controls frame
controls_frame = tkinter.Frame(window)
controls_frame.pack()
#controls components
controls_left = tkinter.Frame(controls_frame)
controls_left.pack(side=tkinter.LEFT)
controls_center = tkinter.Frame(controls_frame)
controls_center.pack(side=tkinter.LEFT)
controls_right = tkinter.Frame(controls_frame)
controls_right.pack(side=tkinter.LEFT)
#buttons
up_btn = tkinter.Button(controls_center, text=" UP ", command=move_up, width=buttonwidth)
up_btn.pack(side=tkinter.TOP)
down_btn = tkinter.Button(controls_center, text="DOWN", command=move_down, width=buttonwidth)
down_btn.pack(side=tkinter.TOP)
left_btn = tkinter.Button(controls_left, text="LEFT", command=move_left, width=buttonwidth)
left_btn.pack()
right_btn = tkinter.Button(controls_right, text="RIGHT", command=move_right, width=buttonwidth)
right_btn.pack()

#location label
lbl_location = tkinter.Label(window, textvariable=location)
lbl_location.pack() #side?

#call the main loop
update_location()
window.mainloop()