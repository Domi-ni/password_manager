from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_input.grid(row=1, column=1, columnspan=2)

user_input = Entry(width=40)
user_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

# buttons
generate_password_button = Button(text="Generate Password")  # command=generate_password
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
