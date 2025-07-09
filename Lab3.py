#imports
import tkinter

#event handlers
def click_morning():
    message.set("Good Morning " + name)

def click_afternoon():
    message.set("Good Afternoon " + name)

#setup
window = tkinter.Tk() #main window object
window.title("Lab3") #set title
window.geometry("300x100") #set WxH
name = "Melody"
message = tkinter.StringVar() #allows label to be updated with .set()

#create buttons
morning_button = tkinter.Button(window, text="Morning", command=click_morning)
afternoon_button = tkinter.Button(window, text="Afternoon", command=click_afternoon)
#pack buttons
morning_button.pack(side=tkinter.LEFT)
afternoon_button.pack(side=tkinter.LEFT)
#label
lbl_greeting = tkinter.Label(window, textvariable=message)
lbl_greeting.pack(side=tkinter.LEFT)

#call the main loop
window.mainloop()