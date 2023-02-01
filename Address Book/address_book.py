"""
    GIT: @drafonsopena
    + The objective is to create an Address Book using Python.
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install libraries (eg: pip3 install tk)
    | Basic Python skills
    | Use a virtual environment
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Create display window
    | Create labels, functions and buttons
    +---------------- 3 ----------------
    | All necessary libraries for the Address Book:
    | from tkinter import *
    +------------------------------------
"""


# import modules
from tkinter import *
# initialize display window
root = Tk()
root.geometry("400x400")
root.config(bg="SlateGray3")
root.resizable (0, 0)
root.title("My Address Book")
# creation of variables that store the contact list
contactList = [
    ["Bruce Wayne", "0176738493"],
    ["Clark Kent", "2684430000"],
    ["Berry Alan", "4338354432"],
    ["Harley Queen", "6834552341"],
    ["Elizabeth Swan", "1234852689"],
    ["Edward Cullen", "2119876543"],
]
# creation of variables that store the name and number
name = StringVar()
number = StringVar()
# creation of container to organise the widgets
frame = Frame(root)
frame.pack(side=RIGHT)
# scrollbar and listbox widget
scroll = Scrollbar(frame, orient=VERTICAL)
Select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config(command=Select.yview)
scroll.pack(side=RIGHT, fill=Y)
Select.pack(side=LEFT, fill=BOTH, expand=1)
# defining the functions
# select() function
def selected_contact():
    return int(Select.curselection()[0])
# add() contact function
def addContact():
    contactList.append([name.get(), number.get()])
    Select_set()
# edit() contact function
def EDIT():
    contactList[selected_contact()] = [name.get(), number.get()]
    Select_set()
# delete() contact function
def DELETE():
    del contactList[selected_contact()]
    Select_set()
# view() contact function
def VIEW():
    Name, phone = contactList[selected_contact()]
    name.set(Name)
    number.set(phone)
# exit() contact function
def EXIT():
    root.destroy()
# reset() contact function
def RESET():
    name.set("")
    number.set("")
# select_set() function
def Select_set():
    contactList.sort()
    Select.delete(0, END)
    for Name, phone in contactList:
        Select.insert(END, Name)
Select_set()
# Define Labels and Entry boxes
# Label and Entry for Name
Label(root, text="NAME", font="arial 12 bold",
      bg="SlateGray3").place(x=30, y=20)
Entry(root, textvariable=name).place(x=100, y=20)
# Label and Entry for phone number
Label(root, text="Phone Number", font="arial 12 bold",
      bg="SlateGray3").place(x=30, y=70)
Entry(root, textvariable=number).place(x=150, y=70)
# Define buttons
# Add contact button
Button(root, text="Add", font="arial 12 bold", bg="SlateGray4",
       command=addContact).place(x=50, y=110)
# Edit contact button
Button(root, text="Edit", font="arial 12 bold", bg="SlateGray4",
       command=EDIT).place(x=50, y=260)
# Delete contact button
Button(root, text="Delete", font="arial 12 bold", bg="SlateGray4",
       command=DELETE).place(x=50, y=210)
# View contact button
Button(root, text="View", font="arial 12 bold", bg="SlateGray4",
       command=VIEW).place(x=50, y=160)
# Exit contact button
Button(root, text="Exit", font="arial 12 bold", bg="SlateGray4",
       command=EXIT).place(x=300, y=320)
# Add contact button
Button(root, text="Clear", font="arial 12 bold", bg="SlateGray4",
       command=RESET).place(x=50, y=310)
# run program
root.mainloop()