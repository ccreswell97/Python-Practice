from tkinter import Tk, Button, PhotoImage


win = Tk()
win.title("Flashy")
win.config(padx=20, pady=40)

checkmark_image = PhotoImage(file="./images/right.png") 
yes_button = Button(image=checkmark_image, highlightthickness=0)

x_image = PhotoImage(file="./images/wrong.png") 
no_button = Button(image=x_image, highlightthickness=0)

win.mainloop()
