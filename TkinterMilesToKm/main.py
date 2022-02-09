from tkinter import *

def calculate():
    if km_input.get():
        km = float(km_input.get())
        miles_input.delete(0, END)
        miles_input.insert(0, km / 1.609344)
    elif miles_input.get():
        miles = float(miles_input.get())
        km_input.delete(0, END)
        km_input.insert(0, miles * 1.609344)

window = Tk()
window.title("Miles to KM converter")
window.minsize(300, 300)
window.config(padx=20, pady=20)

miles_input = Entry(window,width=10)
miles_input.grid(row=0, column=0)

from_label = Label(text="Miles", font=("Arial", 16, "normal"))
from_label.grid(row=1, column=0)

equals_label = Label(text="=", font=("Arial", 16, "normal"))
equals_label.grid(row=0, column=1)

km_input = Entry(window, width=10)
km_input.grid(row=0, column=3)

km_label = Label(text="Km", font=("Arial", 16, "normal"))
km_label.grid(row=1, column=3)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
