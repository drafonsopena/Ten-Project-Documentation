"""
    GIT: @drafonsopena
    + The objective is to create a Password Generator project using Python.
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install Tkinter (pip3 install tk)
    | Install pyperclip module (pip3 install pyperclip)
    | Install the random module (pip3 install random)
    | Basic Python skills
    | Use a virtual environment
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Create a dialog box for user input
    | Use 'For' loop to combine different characters for the password
    +---------------- 3 ----------------
    | All necessary libraries to form the alarm clock:
    | From tkinter import *
    | Import string, random
    | Import pyperclip
    +------------------------------------
"""


# import the necessary libraries
from tkinter import *
import string, random
import pyperclip

# initialize window
root = Tk()
# set width and height of the window
root.geometry("400x400")
# set fixed size of the window
root.resizable (False, False)
# title of the window
root.title("Forever Green - PASSWORD GENERATOR")
# display lines of text in the GUI Window
Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack()
Label(root, text='4EverGreen', font='arial 25 bold').pack(side=BOTTOM)
pass_label = Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack()
# used to store the length of a password
pass_len = IntVar()
# select password length from fixed number values (from 8 to 32)
length = Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()
pass_str = StringVar()
# create a function used to generate password
def pass_generator():
    # empty string variable for the random password
    password = ''
    # combine uppercase, lowercase, digits and special symbols
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    # generate a random string of length entered by the user
    # 4 is subtracted because we already generate a string of length 4
    for y in range(pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    # set password to the string variable
    pass_str.set(password)
# display a button on the GUI Window
Button(root, text='Generate Your Password', command=pass_generator).pack(pady=5)
# create a text input field
# and retrieve current text to the entry widget
Entry(root, textvariable=pass_str).pack()
# function used to copy password to clipboard
def copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=5)

# run program
root.mainloop()
