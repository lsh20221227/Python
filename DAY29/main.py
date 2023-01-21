from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols


    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)



# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)

# password_list = []
# [password_list.append(random.choice(letters)) for letter in range(nr_letters)]
# [password_list.append(random.choice(symbols)) for symbol in range(nr_symbols)]
# [password_list.append(random.choice(numbers)) for number in range(nr_numbers)]

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()

    if len(user_website)==0 or len(user_password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message = f"These are the details enter: \nEmail:{user_email}"
                                                                     f"\nPassword: {user_password} \nIs it ok to save?")
        if is_ok:
            with open ("data.txt",mode ="a") as file:
                file.write(f"{user_website} {user_email} {user_password}\n")
                website_input.delete(0, END)
                password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas = Canvas(width=200,height=200)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0, column=1)

website=Label(text="Website:")
website.grid(row=1,column=0)
email = Label(text="Email/Username:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)


# Entry
website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0, "python@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3,column=1)


#Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)







window.mainloop()

