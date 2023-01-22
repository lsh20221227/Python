fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + " pie")


# make_pie(4)


#----------------------------------------------------------------------------

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        #total_likes += 0
        pass


# print(total_likes)

#-----------------------------------------------------------------------------------

import pandas

data = pandas.read_csv("../DAY26_2/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#SOLUTION

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

# generate_phonetic()


########################################################################



# is_on=True
# while is_on:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#     else:
#         print(output_list)
#         is_on=False
#


#--------------------------------------------------------------------------------
# DAY29 PASSWORD UPGRADE
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    user_website = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    if len(user_website)==0 or len(user_password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                 json.dump(data, data_file, indent=4)
        finally:
             website_input.delete(0, END)
             password_input.delete(0,END)

#--------------------------FIND PASSWORD ------------------------------------------

def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title= website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message = f"No details for {website} exists. ")

#------------------------  SEARCH -----------------------------------------------
# SOLUTION 보기 전에 혼자 해보기
def search():
    user_website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            new_dict = {key: value for (key, value) in data.items()}
    except KeyError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        user_email = new_dict[user_website]['email']
        user_password = new_dict[user_website]["password"]
        messagebox.showinfo(title=user_website, message=f"Email: {user_email}\n"
                                                     f"Password: {user_password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=10,pady=10)


canvas = Canvas(width=200,height=200)
lock_image=PhotoImage(file="../DAY29/logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0, column=1)

website_label=Label(text="Website:")
website_label.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2,column=0)
password = Label(text="Password:")
password.grid(row=3,column=0)


# Entry
website_input = Entry(width=28)
website_input.grid(row=1,column=1)
website_input.focus()
email_input = Entry(width=45)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0, "python@gmail.com")
password_input = Entry(width=28)
password_input.grid(row=3,column=1)


#Button
search_button = Button(text = "Search",bg="blue",width=14, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=45,command=save)
add_button.grid(row=4,column=1,columnspan=2)



window.mainloop()




