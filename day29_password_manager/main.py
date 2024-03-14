import tkinter
from tkinter import messagebox
import random
import pyperclip
import os
import json


# ---------------------------- Search Button ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data:
            data_to_search = json.load(data)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data file found\n"
                                          "fill in the info and press Save button to create a new file")

    if website in data_to_search:
        website_to_search = data_to_search[website]
        messagebox.showwarning("Warning", "No details for the website found")
        messagebox.showinfo(website, f"Email: {website_to_search['email']}\n"
                                     f"Password: {website_to_search['password']}")
    else:
        messagebox.showinfo(title="Warning", message="You have not saved such website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_generate_entry.delete(0, "end")
    password_generate_entry.insert(index=0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def writing_to_file():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_generate_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showwarning("Предупреждение!", "Заполни все поля!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except(FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                data.update(new_data)
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, "end")
            password_generate_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Менеджер Паролей")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)

password_logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

# website relate label and entry
website_label = tkinter.Label(text="Сайт:")
website_entry = tkinter.Entry(width=33)

website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, sticky="w")

# email and username related label and entry
email_username_label = tkinter.Label(text="Почта/Имя пользователя:")
email_username_entry = tkinter.Entry(width=52)

email_username_label.grid(column=0, row=2)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")
email_username_entry.insert(0, "Alihan-mb@mail.ru")

# password related label button and entry
password_label = tkinter.Label(text="Пароль:")
password_generate_entry = tkinter.Entry(width=33)
password_generate_button = tkinter.Button(text="Создать пароль", width=14, command=generate_password)

password_label.grid(column=0, row=3)
password_generate_entry.grid(column=1, row=3)
password_generate_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Сохранить", width=44, command=writing_to_file)
add_button.grid(column=1, row=4, columnspan=2)

search_button = tkinter.Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1, sticky="w")

window.mainloop()
