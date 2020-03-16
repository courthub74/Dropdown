from tkinter import *

app = Tk()
app.title("DropDown")

# Title
title = Label(app, text="Theee DropDown", font="none 20 bold", fg="Blue2")
title.pack()

# List for Drop Down Menu
numlist = ["Pick a Number", "1", "2", "3", "4", "5", "6"]

# Drop Down Menu
numbers = StringVar()  # String variable for the dropdown
numbers.set(numlist[0]) # Sets the String displayed on the dropdown
droplist = OptionMenu(app, numbers, *numlist) # appends the string var and ALL of the chosen list
droplist.config(width=20, height=1, font="arial 12")
droplist.pack()

def getnum(*args):
	if numbers.get() == "1":
		tfield.delete(0.0, END)
		tfield.insert(INSERT, "One")
	if numbers.get() == "2":
		tfield.delete(0.0, END)
		tfield.insert(INSERT, "Two")
	if numbers.get() == "3":
		tfield.delete(0.0, END)
		tfield.insert(INSERT, "Three")
	if numbers.get() == "4":
		tfield.delete(0.0, END)
		tfield.insert(INSERT, "Four")
	if numbers.get() == "5":
		tfield.delete(0.0, END)
		tfield.insert(INSERT, "Five")
	if numbers.get() == "6":
		tfield.delete(0.0, END)
		tfield.insert(INSERT, "Six")

numbers.trace("w", getnum) # Call the StringVar.trace (write, function desired)

# Output Field
tfield = Text(app, width=20, height=5, font="Arial 20 bold")
tfield.pack()

app.mainloop()
