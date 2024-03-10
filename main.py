from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT = ("Arial", 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    user_password.delete(0, END)
    user_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = user_website.get()
    email = user_email.get()
    password = user_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details that you entered: \nEmail: {email} "
                                               f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Cream un .txt file:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}  ||| {email} ||| {password} \n")
                user_website.delete(0, END)
            user_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Pasword Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
title_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=title_image)
canvas.grid(column=1, row=0)

# Labels:

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry:

user_website = Entry(width=51)
user_website.grid(column=1, row=1, columnspan=2)
user_website.focus()

user_email = Entry(width=51)
user_email.grid(column=1, row=2, columnspan=2)
user_email.insert(0, "user_email@gmail.com")

user_password = Entry(width=33)
user_password.grid(column=1, row=3)

# Button:

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

### columnspan=2


window.mainloop()
