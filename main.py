from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    passwd_entry.delete(0, END)
    passwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():

    if len(website_entry.get()) * len(email_entry.get()) * len(passwd_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        line_to_write = website_entry.get() + " | " + email_entry.get() + " | " + passwd_entry.get() + "\n"
        msg = f"Do you want to save? \nEmail/Username: {email_entry.get()} \nPassword: {passwd_entry.get()}"
        is_ok = messagebox.askokcancel(title=f"Website: {website_entry.get()}", message=msg)

        if is_ok:
            with open("passwords.txt", 'a') as file:
                file.write(line_to_write)
            website_entry.delete(0, END)
            passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=53)
email_entry.insert(0, "mibu989@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

passwd_entry = Entry(width=34)
passwd_entry.grid(column=1, row=3)

gen_passwd_btn = Button(text="Generate Password", command=generate_passwd)
gen_passwd_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=45, command=save_to_file)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
