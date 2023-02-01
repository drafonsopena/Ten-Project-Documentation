"""
    GIT: @drafonsopena
    + The objective is to create a base64 Encode and Decode Message using Python.
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
    | All necessary libraries for the Encode and Decode Message:
    | import tkinter as tk
    | import base64
    +------------------------------------
"""

# import modules
from tkinter import *
import base64
# create window
root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Encode and Decode App")

# creation of labels
Label(root, text="Encode & Decode", font="arial 20 bold").pack()
Label(root, text="By: DRAP", font="arial 20 bold").pack(side=BOTTOM)
# define global variables Text, private_key, mode and Result
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# create function used to encode
def encode_message(key, message):
    enc = [] # empty list
    # run a loop till the length of the message
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    # return
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# creation of function used to decode
def decode_message(key, message):
    dec = [] # empty list
    message = base64.urlsafe_b64decode(message).decode()
    # a for loop
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    # return
    return "".join(dec)
# creation the function to se the mode of encoding
def Mode():
    if mode.get() == "e" or "E":
        Result.set(encode_message(private_key.get(), Text.get()))
    elif mode.get() == "d" or "D":
        Result.set(decode_message(private_key.get(), Text.get()))
    else:
        Result.set("Invalid Mode, choose another!")
# function used to Exit window
def Exit():
    root.destroy()
# function used to reset the window, sets variables to empty strings
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
# creation of more labels and Buttons
# Label and Entry for Text variable
Label(root, text="MESSAGE", font="arial 12 bold").place(x=60, y=60)
Entry(root, font="arial 10", textvariable=Text, bg="ghost white").place(x=290, y=60)
# Label and Entry for the private_key variable
Label(root, text="Key", font="arial 12 bold").place(x=60, y=90)
Entry(root, font="arial 10", textvariable=private_key,
      bg="ghost white").place(x=290, y=90)

# Label and Entry for mode variable
Label(root, text="MODE(e-encode, d-decode)", font="arial 12 bold").place(x=60, y=120)
Entry(root, font="arial 10 bold", textvariable=mode, bg="ghost white").place(x=290, y=120)
# Entry for Result variable
Entry(root, font="arial 10 bold", textvariable=Result, bg="ghost white").place(x=290, y=150)
# creation for the MODE button
Button(root, text="Result", font="arial 10 bold", padx=2, bg="LightGray",
       command=Mode).place(x=60, y=150)

# creation of the Reset button
Button(root, text="Reset", font="arial 10 bold", width=6,
       command=Reset, bg="LimeGreen", padx=2).place(x=80, y=190)
# creation of exit button
Button(root, text="EXIT", font="arial 10 bold", width=6,
       command=Exit, bg="OrangeRed", padx=2, pady=2).place(x=180, y=190)

# run the program
root.mainloop()