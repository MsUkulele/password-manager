from tkinter import *
from tkinter import messagebox

BG = "#EEEFE0"
FG = "#641B2E"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pw():
    print("password generated")
# Define the password length
# Pw should be letters, numbers and signs (maybe insert a file that contains that
# make a for loop and select random indexes from those lists
# save it in a string
# put the string into the label

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
        is_correct= messagebox.askokcancel(title="Correct input?", message=f"Are you sure your details are correct?\n \nEmail: {email} \n Website: {website} \nPassword: {password}")
        if is_correct:
            with open("data.txt", "a") as pw_file:
                pw_file.write(f"{website}, {email}, {password}\n")

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