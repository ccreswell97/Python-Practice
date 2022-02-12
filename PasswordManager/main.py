from tkinter import Button, Canvas, Entry, Label, Tk, PhotoImage, END, messagebox
import random

# TODO: PASSWORD GENERATOR 
def generate_pw():
    password = ""

    password_input.delete(0, END)
    password_input.insert(0, password)

# Absolutely NOT a secure way to store passwords, this is just practice for now!! I would never store a user's password in plain text and this is only meant to be run on a local machine
def write_data():
    website = website_input.get()
    username = email_username_input.get()
    password = password_input.get()

    is_correct = messagebox.askokcancel(title=website, message=f"Are these details correct?\nWebsite: {website}\nUsername: {username}\nPassword: {password}" )

    if is_correct: 
        with open("data.txt", "a") as file:
            file.write(f"{website} | {username} | {password}\n")

        website_input.delete(0,END)
        email_username_input.delete(0, END)
        password_input.delete(0, END) 

win = Tk()
win.title("Password Manager")
win.config(padx=20, pady=40)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website input
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=38)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email/Username input
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_input = Entry(width=38)
email_username_input.grid(column=1, row=2, columnspan=2)

# Password input
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Generate Password button
generate_pw_button = Button(text="Generate Password", command=generate_pw)
generate_pw_button.grid(column=2, row=3)

# Add button
add_button = Button(width=35, text="Add", command=write_data)
add_button.grid(column=1, row=4, columnspan=2)

win.mainloop()