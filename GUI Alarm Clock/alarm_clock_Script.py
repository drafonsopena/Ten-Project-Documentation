"""
    GIT: @drafonsopena
    + The objective is to implement an alarm clock using Python.:
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install Tkinter (pip3 install tk)
    | Basic Python skills
    | Use a virtual environment
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Use 'while' loop which takes argument of the time
    | Create a dialog box for user input
    +---------------- 3 ----------------
    | All necessary libraries to form the alarm clock:
    | From tkinter import *
    | Import datetime
    | Import time
    | Import winsound
    +------------------------------------
"""

# importing all necessary libraries
from tkinter import *
import \
    datetime
import \
    time
import \
    winsound

# creating the function 'alarm'
def alarm (set_alarm_timer):
    # while loop takes the time argument:
    # Boolean set to True to make the program work automatically:
    while True:
        time.sleep (1)
        current_time = datetime.datetime.now ()
        now = current_time.strftime ("%H:%M:%S")
        date = current_time.strftime ("%d/%m/%Y")
        print ("Current Date: ", date)
        print ("Current Time: ", now)
        if now == set_alarm_timer:
            print ("GO GET IT!")
        winsound.PlaySound ("sound.wav", winsound.SND_ASYNC)
        break
# convert the current time to string:
def actual_time ():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{sec.get()}"
    alarm (set_alarm_timer)
# initialize tkinter:
clock = Tk()
# title of dialog box:
clock.title ("ClockS Alarm")
# size of dialog box:
clock.geometry ("400x200")
# time_format label for time format "Enter time in 24h format!":
time_format = Label (clock, text="Enter time in 24h format!",
                     fg="red", bg="black",
                     font="Arial").place (x=60, y=120)
# addTime label for "Hour, Minute, Sec" above input boxes:
addTime = Label (clock, text="Hour Min Sec",
                 font=60).place (x=110)
# setYourAlarm label for "When to wake up?":
setYourAlarm = Label (clock, text="When to wake up?",
                      fg="blue", relief="solid",
                      font=("Helevetica", 7, "bold")).place (x=0, y=29)
# initialize input dialog boxes:
hour = StringVar()
minute = StringVar()
sec = StringVar()
# input boxes to take user input in 24h format:
hourTime = Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110, y=30)
minTime = Entry(clock, textvariable=minute, bg="pink", width=15).place(x=150, y=30)
secTime = Entry(clock, textvariable=sec, bg="pink", width=15).place(x=200, y=30)
# the button used to execute/start the program:
# takes command from actual_time function
submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command=actual_time).place(x=110, y=70)
# compile all previous commands with their basic settings
# color, font, width, axis... and display the program window:
clock.mainloop()
