# simple interest calculator - A = P * r * t

from tkinter import *
from tkinter import ttk

# Amount is the result of the formula above
amount = 0

# Finds the product of the principal, rate and time
def calculate_simple_interest(p, r, t):
    global amount
    amount = p * (r/100) * t
    return amount

# Pushes the calculation onto the button
def calculate_button_wn():
    global principal_entry, rate_entry, time_entry
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    total = calculate_simple_interest(p, r, t)
    result_label.config(text="Your money will yield $" + str(calculate_simple_interest(p, r, t)))


# Instantiates the Tkinter object as "wn"
wn = Tk()
wn.title("Calculate interest")
wn.geometry("250x250")

# Puts title of the caluclator as a readable title for the viewer
intro_label = Label(wn, text="Simple interest calculator").grid(row=0, column=1)

principal_label = Label(wn, text="Principal: $").grid(row=1, column=0)
principal_entry = Entry(wn, width=15)
principal_entry.grid(row=1, column=1)

rate_label = Label(wn, text="Rate: (%)").grid(row=2, column=0)
rate_entry = Entry(wn, width=15)
rate_entry.grid(row=2, column=1)

time_label = Label(wn, text="Time in years: ").grid(row=3, column=0)
time_entry = Entry(wn, width=15)
time_entry.grid(row=3, column=1)

calculate_button = Button(wn, text="Calculate", command=calculate_button_wn).grid(row=4, column=1)

result_label = Label(wn, text="")
result_label.grid(row = 5, column=1)

wn.mainloop()
