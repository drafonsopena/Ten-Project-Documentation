"""
    GIT: @drafonsopena
    + The objective is to create a Currency Convertor using Python.
    | Group:
    +-+---------------- 1 ----------------
    | Prerequisites:
    | Install libraries (eg: pip3 install tk)
    | Basic Python skills
    | Use a virtual environment
    | API (url = 'https://api.exchangerate-api.com/v4/latest/USD')
    +---------------- 2 ----------------
    | Project File Structure:
    | Import all the needed libraries/modules
    | Form the images representing the dice parts
    | Create labels, functions and buttons
    +---------------- 3 ----------------
    | All necessary libraries to form the alarm clock:
    | import re
    | From tkinter import *
    | import tkinter as tk
    | from tkinter import ttk
    | import requests
    +------------------------------------
"""

# import the necessary libraries tkinter and requests
import \
    re
from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests

# create CurrencyConverter class
# with a constructor
class RealTimeCurrencyConvertor:
    def __init__(self, url):
        # requests.get(url) loads page in the program
        # .json() converts the page into json file
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first we convert to our base currency USD
        if from_currency != 'USD':
            amount = amount/self.currencies[from_currency]
        # result limited to only 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
"""
Example used to test our Converter, if this does not work chaeck above code.
# Test progress code
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = RealTimeCurrencyConvertor(url)
# from_currency, to_currency and amount
print(converter.convert('INR','USD',100))
"""
# User Interface creation
# class for UI
class App (tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self) # Frame creation
        self.title = 'Currency Converter v 0.1.05'
        self.currency_converter = converter
        # creation of the converter
        self.geometry("500x200")
        # Labels
        self.intro_label = Label(self, text='This is a real time Currency Converter',
                                 fg='dark blue', relief=tk.RAISED, borderwidth=3)
        self.intro_label.config(font=('Helvetica', 15, 'bold'))
        self.date_label = Label (self,
                                 text=f"1 Kwanza is = to {self.currency_converter.convert ('AOA', 'USD', 1)} USD \n Date : {self.currency_converter.data ['date']}",
                                 relief=tk.GROOVE,
                                 borderwidth=6)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=180, y=60)
        # Entry Box
        valid = (self.register(self.restrictNumberOnly), '%d, %P')
        # Restrict user from entering invalid numbers will be defined later
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key',
                                  validatecommand=valid, width=17, borderwidth=3)
        self.converted_amount_field_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE,
                                                  justify=tk.CENTER, width=17, borderwidth=3)

        # Drop down menu for currency selection
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("AOA") # default value Kwanza
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") # default value American Dollar
        # font selection
        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable, values=list(self.currency_converter.currencies.keys()),
                                                   font=font, state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable, values=list(self.currency_converter.currencies.keys()),
                                                 font=font, state='readonly', width=12, justify=tk.CENTER)
        # Placing the dropdown menu
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        # self.converter_amount_field.place(x=346, y=150)
        self.converted_amount_field_label.place(x=346, y=150)
        # Converter button
        self.converter_button = Button(self, text="Exchange Currency", fg="black",
                                       command=self.perform)
        self.converter_button.config(font=("Courier", 10, "bold"))
        self.converter_button.place(x=180, y=125)
# APP class
    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()
        # convert amount
        convert_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(convert_amount, 2)
        self.converted_amount_field_label.config(text=str(converted_amount))
    # Restrict Number
    def restrictNumberOnly (self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return string == "" or (string.count(".") <= 1 and result is not None)

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConvertor (url)

    App(converter)
    mainloop()