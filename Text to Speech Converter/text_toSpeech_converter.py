"""
    GIT: @drafonsopena
    + The objective is to create a Text-to-Speech Converter using Python.
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
    | All necessary libraries for the Text-to-Speech Converter:
    | import tkinter as tk
    | from gtts import gTTS
    | from playsound import playsound
    +------------------------------------
"""

# importing the necessary modules
import \
    tkinter
from gtts import gTTS
from playsound import playsound

# creation of display window
root = tkinter.Tk()
root.geometry("350x300")
root.configure(bg="ghost white")
root.title("Convert TEXT to SPEECH")
# Insert labels and pack them in display window
tkinter.Label(root, text="TEXT_TO_SPEECH", font="arial 20 bold",
              bg="white smoke").pack()
tkinter.Label(root, text="By: DRAP", font="arial 15 bold",
              bg="white smoke", width=20).pack(side="bottom")
# Message variable
Msg = tkinter.StringVar()
tkinter.Label(root, text="Enter Text", font="arial 15 bold",
              bg="white smoke").place(x=20, y=60)
# box used to take user input
entry_field = tkinter.Entry(root, textvariable=Msg, width=50)
entry_field.place(x=20, y=100)
# function used to convert text to speech
def text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save("spoken.mp3")
    playsound("spoken.mp3")
# quit program by stopping the mainloop()
def Exit():
    root.destroy()
# set the Msg variable to empty strings
def Reset():
    Msg.set("")

# define button to play the sound from entry box
tkinter.Button(root, text="PLAY", font="arial 15 bold",
               command=text_to_speech, width=4).place(x=25, y=140)

# define button to exit/stop program
tkinter.Button(root, text="EXIT", font="arial 15 bold",
               command=Exit, width=4, bg="OrangeRed").place(x=100, y=140)
# define button to reset/empty entry box
tkinter.Button(root, text="RESET", font="arial 15 bold",
               command=Reset, width=6).place(x=175, y=140)
# run program
root.mainloop()
