from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import random
import pyperclip
import json

BG = "#EEEFE0"
FG = "#641B2E"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # new_list = [new_item for item in list if test]

    # for char in range(nr_letters):
    #  password_list.append(random.choice(letters))

    letters_list = [choice(letters) for char in range(0, nr_letters)]
    symbol_list = [choice(symbols) for symbol in range(0, nr_symbols)]
    numbers_list = [choice(numbers) for number in range(0, nr_numbers)]

    # for char in range(nr_symbols):
    #  password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #  password_list += random.choice(numbers)

    password_list = letters_list + symbol_list + numbers_list

    # password = [new item for char in password_list ]

    #global password_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.config(password_entry.delete(0, END))
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Create a file data.txt DONE
# Use variables for the entries DONE
# Decide a format for the file, I think csv would be great or key-value
# go into write mode and write that file. Write a new line for each entry

# Create a method and link it to the button add

# ---------------------------- UI SETUP ------------------------------- #


## Window Setup##
window = Tk()
window.title("Password Manager")
window.config(width = 220, height = 220, padx=20, pady = 20, bg = BG)

## Canvas & Picture##
canvas = Canvas(width = 200, height = 200, highlightthickness=0)
canvas.config(bg = BG)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo)
canvas.grid(row = 0, column = 1)

## Labels ##
website_label = Label()
website_label.config(text = "Website:", bg = BG, fg = FG )
website_label.grid(row = 1, column = 0)

email_label = Label()
email_label.config(text = "Email/Username:", bg = BG, fg = FG )
email_label.grid(row = 2, column = 0)

password_label = Label()
password_label.config(text = "Password:", bg = BG, fg = FG )
password_label.grid(row = 3, column = 0)

## Entries ##
website_entry = Entry()
website_entry.config(bg = BG, bd= 1, width = 35, fg = FG)
website_entry.grid(row = 1, column = 1, columnspan = 2)

email_entry = Entry()
email_entry.config(bg = BG, bd= 1, width = 35, fg = FG)
email_entry.insert(0, "example@gmail.com")
email_entry.grid(row = 2, column = 1, columnspan = 2)


password_entry = Entry()
password_entry.config(bg = BG, bd= 1, width = 21, fg = FG)
password_entry.grid(row = 3, column = 1, columnspan = 1)


def add_pw():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()

    l_pw = len(password)
    l_ws = len(website)
    l_email = len(email)



    if l_pw == 0:
        messagebox.showinfo(title="Missing info", message = "You left the password field open.")
    elif l_ws == 0:
        messagebox.showinfo(title="Missing info", message="You left the website field open.")
    else:
        # Try opening the file and loading the data
        try:
            with open("data.json", "r") as pw_file:
                # If that file has some content
                data = json.load(pw_file)
            with open("data.json", "r") as pw_file:
                # If that file has some content
                data = json.load(pw_file)
                new_data = {
                    website: {
                        "email:": email,
                        "password:": password
                    }
                }
                data.update(new_data)
            with open("data.json", "w") as pw_file:
                json.dump(data, pw_file, indent=4)
        # If the file is empty
        except JSONDecodeError:
            with open("data.json", "w") as pw_file:
                new_data = {
                    website: {
                        "email:": email,
                        "password:": password
                    }
                }
                json.dump(new_data, pw_file, indent = 4)
        # If file does not exist yet
        except FileNotFoundError:
            with open("data.json", "w") as pw_file:
                new_data = {
                    website: {
                        "email:": email,
                        "password:": password
                    }
                }
                json.dump(new_data, pw_file, indent = 4)
        password_entry.delete(0, END)
        website_entry.delete(0, END)


# Buttons
add_pw_button = Button()
add_pw_button.config(text = "Add", highlightthickness= 0, bg = BG, width = 32, command = add_pw)
add_pw_button.grid(row = 4, column = 1, columnspan = 2)

gen_pw_button = Button()
gen_pw_button.config(text = "Generate Password", highlightthickness= 0, bg = BG, width = 10, command = generate_pw)
gen_pw_button.grid(row = 3, column = 2, columnspan=1)







window.mainloop()