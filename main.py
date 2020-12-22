from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    passwd_letters = [random.choice(letters) for _ in range(nr_letters)]
    passwd_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    passwd_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = passwd_letters + passwd_symbols + passwd_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    passwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = passwd_entry.get()
    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please dont leave any of the field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f" These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it OK to Save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                #email_entry.delete(0, END)
                passwd_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
passwd_label = Label(text="Password:")
passwd_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
passwd_entry = Entry(width=21)
passwd_entry.grid(row=3, column=1)

#Button
gen_pwd_btn = Button(text="Generate Password", command=generate_passwd)
gen_pwd_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()