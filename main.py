import json
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X", "Y", "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random_password = password_letters + password_numbers + password_symbols
    random.shuffle(random_password)

    new_password = "".join(random_password)
    password_input.insert(0, new_password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    website = website_input.get()
    try:
        with open("data/data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            user = data[website]["user"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {user}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There's No Data File Found For {website}")
    finally:
        website_input.delete(0, "end")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }

    if website == "" or password == "" or user == "":
        messagebox.showinfo(title="Miss Information", message="Please don't leave any of the fields empty")

    else:
        try:
            with open("data/data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data/data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data/data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_text_label = Label(text="Website: ")
website_text_label.grid(row=1, column=0)

user_text_label = Label(text="Email/Username: ")
user_text_label.grid(row=2, column=0)

password_text_label = Label(text="Password: ")
password_text_label.grid(row=3, column=0)

# entry
website_input = Entry(width=28)
website_input.focus()
website_input.grid(row=1, column=1)

user_input = Entry(width=47)

try:
    with open("data/user_mail.txt", mode="r") as user_mail_data:
        user_input.insert(index=0, string=user_mail_data.read())

except FileNotFoundError:
    user_mail = askstring("Email", "\nWhat's your most used email?\n")

    with open("data/user_mail.txt", mode="w") as user_mail_data:
        user_mail_data.write(user_mail)


user_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=28)
password_input.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2, columnspan=2)

window.mainloop()
