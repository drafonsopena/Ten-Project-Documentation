"""
    GIT: @drafonsopena
    + The objective is to create a Die Rolling Simulator using Python.
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install libraries (pip3 install tk)
    | Basic Python skills
    | Use a virtual environment
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Form the images representing the dice parts
    | Create labels, functions and buttons
    +---------------- 3 ----------------
    | All necessary libraries to form the alarm clock:
    | From tkinter import *
    | from PIL import Image, ImageTk
    | import random
    +------------------------------------
"""
# Importing libaries
import tkinter
from PIL import Image, ImageTk
import random

# build the main window for the application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Dice Rolling Simulator')
# adding a label to the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()
# adding a label with different font and format
headingLabel = tkinter.Label(root, text="Ready To Roll",
                             fg="dark green",
                             bg="light green",
                             font="Helvetica 16 bold italic")
headingLabel.pack()
# images
# forming a list of images to be randomly displayed
dice = ['die1.png', 'die2.png', 'die3.png',
        'die4.png', 'die5.png', 'die6.png']
# simulate dice roll with random numbers
# between 0 and 6 generating images
diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label image for Label
imageLabel = tkinter.Label(root, image=diceImage)
imageLabel.image = diceImage

# packing a widget in parent widget
imageLabel.pack(expand=True)
# create a button to activate the function
def rolling_dice():
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    imageLabel.configure(image=diceImage)
    # keep a reference of image
    imageLabel.image = diceImage

# adding a button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll Dice', fg='blue',
                        command=rolling_dice)
# pack the button in parent widget
button.pack(expand=True)
# Run program
root.mainloop()