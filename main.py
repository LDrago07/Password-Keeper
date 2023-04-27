from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
def save():
    
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Opps", message="Please don't have any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the details entered: \nEmail: {email_input.get()} \nPassword: {password_input.get()} \nIs it ok to save?")

        if is_ok:
            with open(f"Day 29 My Pass/data.txt", mode="a") as data:
                data.write(f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
            
window = Tk()
window.title("My Pass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="Day 29 My Pass/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2,sticky="EW")
email_input.insert(0, "example-email@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()