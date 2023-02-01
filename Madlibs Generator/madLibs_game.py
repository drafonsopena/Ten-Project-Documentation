"""
    GIT: @drafonsopena
    + The objective of this project is to create a Madlibs Generator App using Python.
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install Tkinter (pip3 install tk)
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Create display window
    | Create functions and input variables
    +---------------- 3 ----------------
    | All necessary libraries to form the alarm clock:
    | From tkinter import *
    +------------------------------------
"""

# import module
from tkinter import *
# create a display window
# set the size of the window
root = Tk ()
root.geometry ('300x300')
root.title ('Mad Libs Generator')

Label (root, text='Mad Libs Generator \n For Fun Time',
       font='arial 20 bold').pack ()

Label (root, text='Click Any One: ',
       font='arial 15 bold').place (x=40, y=80)

# madlibs_One function was created for the first story "The Photograph."
# and some user input variables
def madlib_One ():
    animals = input ("Enter an animal name: ")
    profession = input ("Enter a profession name: ")
    cloth = input ("Enter a cloth name: ")
    objects = input ("Enter an object name: ")
    name = input ("Enter a name: ")
    place = input ("Enter a place name: ")
    verb = input ("Enter a verb in 'ing' form: ")
    food = input ("Enter a food name: ")

    print ('Say ' + food + ', the photographer said as the camera flashed! '
           + name + ' and I had gone to ' + place + ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as '
           + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like '
           + objects + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

# madlibs_Two function was created for the second story "The Butterfly."
# and some user input variables
def madlib_Two ():
    adjective = input ("Enter an adjective: ")
    color = input ("Enter a color name: ")
    objects = input ("Enter an object name: ")
    place = input ("Enter a place name: ")
    person = input ("Enter a person's'name: ")
    adjective1 = input ("Enter an adjective: ")
    insect = input ("Enter an insect name: ")
    food = input ("Enter a food name: ")
    verb = input ("Enter a verb: ")

    print ('Last night I dreamed I was a ' + adjective + ' butterfly with ' + color + ' splotches that looked like '
           + objects + ' .I flew to ' + place + ' with my best-friend and ' + person + ' who was a '
           + adjective1 + ' ' + insect + ' . We ate some ' + food + ' when we got there and then decided to '
           + verb + ' and the dream ended when I said-- lets ' + verb + '.')

# madlibs_Three function was created for the first story "Apples and Apples"
# and some user input variables
def madlib_Three ():
    person = input ("Enter a person's' name: ")
    color = input ("Enter color: ")
    foods = input ("Enter a food name: ")
    adjective = input ("Enter an adjective name: ")
    objects = input ("Enter an object name: ")
    place = input ("Enter a place name: ")
    verb = input ("Enter a verb: ")
    adverb = input ("Enter an adverb: ")
    food = input ("Enter a food name: ")
    objects1 = input ("Enter another object name: ")

    print ('Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many different varieties of apples. I ate "
           + color + ' apples straight off the tree that tested like ' + foods + '. Then there was a ' + adjective + ' apple that looked like a '
           + objects + '.When our bag were full, we went on a free hay ride to ' + place + ' and back. It ended at a hay pile where we got to '
           + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make apple ' + food + ' and '
           + objects1 + ' pies!.')
# creation of the buttons used to select the stories
Button (root, text='The Photographer',
        font='arial 15', command=madlib_One,
        bg='ghost white').place (x=60, y=120)

Button (root, text='The Butterfly',
        font='arial 15', command=madlib_Two,
        bg='ghost white').place (x=70, y=180)

Button (root, text='Apple and Apples',
        font='arial 15', command=madlib_Three,
        bg='ghost white').place (x=70, y=240)
# run the program
root.mainloop ()
