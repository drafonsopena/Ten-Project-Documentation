"""
    GIT: @drafonsopena
    + The objective is to create a Simple Calculator using Python.
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
    | All necessary libraries for the Simple Calculator:
    | from tkinter import *
    | import parser
    | from math import factorial
    +------------------------------------
"""
# importing libraries
from tkinter import *
import parser
from math import factorial
# creating the display window
root = Tk()
# root.geometry ('300x300')
root.title("A Simple Calculator")
# designing the buttons and entry field
# adding input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=N+E+W+S)
# adding buttons to the calculator
# 1 to 3
Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0, sticky=N+S+E+W)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1, sticky=N+S+E+W)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2, sticky=N+S+E+W)
# 4 to 6
Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0, sticky=N+S+E+W)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1, sticky=N+S+E+W)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2, sticky=N+S+E+W)
# 7 to 9
Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0, sticky=N+S+E+W)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1, sticky=N+S+E+W)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2, sticky=N+S+E+W)
# adding other buttons to the calculator
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0, sticky=N+S+E+W)
Button(root, text=" 0", command=lambda: get_variables(0)).grid(row=5, column=1, sticky=N+S+E+W)
Button(root, text=" .", command=lambda: get_variables(" .")).grid(row=5, column=2, sticky=N+S+E+W)
# adding the operation buttons (+-*/)
Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=N+S+E+W)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=N+S+E+W)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=N+S+E+W)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=N+S+E+W)
# adding special operations part 1
Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4, sticky=N+S+E+W)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4, sticky=N+S+E+W)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=N+S+E+W)
Button(root, text="expo", command=lambda: get_operation("**")).grid(row=5, column=4, sticky=N+S+E+W)
# adding special operations part 2
Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5, sticky=N+S+E+W)
Button(root, text="x!", command=lambda: fact()).grid(row=3, column=5, sticky=N+S+E+W)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=N+S+E+W)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N+S+E+W)
# Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N+S+E+W)
Button(root, text="=", command=lambda: calculate()).grid(columnspan=6, sticky=N+S+E+W)
# mapping the button to their functionalities
# mapping the digits
# variable 'i' keeps track of current position on the input text field
i = 1
# recieves the digit as parameter and display it on the input field
def get_variables(num):
    global i
    # 'i' position to insert digit
    # num the digit inserted
    display.insert(i, num)
    i += 1
# mapping operator buttons
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length
# the clear_all function
def clear_all():
    # zero is the start position
    # END is the end position
    display.delete(0, END)
# the undo function
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error!")
# the equal button's function
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")
# mapping factorial key
def fact():
    entri_string = display.get()
    try:
        result = factorial(int(entri_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!!")

# run program
root.mainloop()