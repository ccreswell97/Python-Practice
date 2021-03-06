from tkinter import Button, Canvas, Entry, Label, Tk, PhotoImage, END, messagebox
from random import choice, randint, shuffle
from string import ascii_letters, punctuation

import json

def generate_pw():
    letters = [choice(ascii_letters) for _ in range(8)]
    punct = [choice(punctuation) for _ in range(2)]
    numbers = [str(randint(0,9)) for _ in range(2)]

    password_list = letters + punct + numbers
    shuffle(password_list)
    password = ''.join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    win.clipboard_clear()
    win.clipboard_append(password)

# Absolutely NOT a secure way to store passwords, this is just practice for now!! I would never store a user's password in plain text and this is only meant to be run on a local machine
def write_data():
    website = website_input.get().strip()
    username = email_username_input.get().strip()
    password = password_input.get().strip()
    new_data = { 
        website: {
            "username": username, 
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave any fields empty!")
        return

    is_correct = messagebox.askokcancel(title=website, message=f"Are these details correct?\nWebsite: {website}\nUsername: {username}\nPassword: {password}" )

    if is_correct: 
        try:
            with open("data.json", "r") as file:
                data = json.load(file)       
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            
        website_input.delete(0,END)
        email_username_input.delete(0, END)
        password_input.delete(0, END) 

def search_credentials(website):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(message="No credentials stored yet")
    else: 
        try:
            credentials = data[website]
            messagebox.showinfo(message=f"{website.title()}\nUsername: {credentials['username']}\nPassword: {credentials['password']}")
        except KeyError:
            messagebox.showerror(message=f"Credentials for website {website} not found")

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

website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

# Website Search button
search_button = Button(text="Search", width=13, command= lambda: search_credentials(website_input.get()))
search_button.grid(column=2, row=1)

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