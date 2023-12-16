from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    if website == "" or password == "" or user == "":
        messagebox.showinfo(title="Miss Information", message="Please don't leave any of the fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Do yo wanna to save \n Site: {website} \n "
                                                          f"User:{user} \n Password: {password} \n is that correct?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {user} | {password} \n")
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
website_input = Entry(width=40)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

user_input = Entry(width=40)
user_input.insert(index=0, string="user@gmail.com")
user_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password")  # command=generate_password
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
