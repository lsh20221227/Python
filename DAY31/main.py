BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial",40,"italic")
FONT_WORD = ("Arial",60,"bold")

from tkinter import *
import pandas
import random

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    df = data.to_dict(orient='records')
else:
    df = data.to_dict(orient='records')

answer=[]


def english_card(random_card):
    canvas.itemconfig(image_front,image=back_img)
    canvas.itemconfig(french, text="English",font=FONT_TITLE,fill="white")
    canvas.itemconfig(word,text=random_card['English'],font=FONT_WORD,fill="white")


def card_select():
    global  random_card
    random_card = random.choice(df)
    canvas.itemconfig(image_front, image=front_img)
    canvas.itemconfig(french, text="French", fill="black")
    canvas.itemconfig(word, text=random_card['French'], fill="black")
    canvas.after(3000, english_card, random_card)


def is_known():
    df.remove(random_card)
    print(len(df))
    data = pandas.DataFrame(df)
    data.to_csv("word_to_learn.csv")



window = Tk()
window.title("단어 암기")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)




canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

front_img = PhotoImage(file="images/card_front.png")
image_front = canvas.create_image(400,263,image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

back_img = PhotoImage(file="images/card_back.png")


#TEXT
french = canvas.create_text(400,150,text="French",font=FONT_TITLE)
word = canvas.create_text(400,263,text="trouve",font=FONT_WORD)


#BUTTON

wrong_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_img,highlightthickness=0,command = card_select)
unknown_button.grid(row=1,column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,highlightthickness=0, command = is_known)


right_button.grid(row=1,column=1)


card_select()




#[{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}
# df = pandas.DataFrame.to_dict(data,orient='dict')
# {'French': {0: 'partie', 1: 'histoire', 2: 'chercher', 3: 'seulement', 4: 'police',
#df = pandas.DataFrame.to_dict(data,orient='list')
# {'French': ['partie', 'histoire', 'chercher', 'seulement', 'police',
# df = pandas.DataFrame.to_dict(data,orient='split')
# 'columns': ['French', 'English'], 'data': [['partie', 'part'], ['histoire', 'history'], ['chercher', 'search'], ['seulement', 'only'],
# df = pandas.DataFrame.to_dict(data,orient='index')
# 0: {'French': 'partie', 'English': 'part'}, 1: {'French': 'histoire', 'English': 'history'}, 2: {'French': 'c
# print(df)

# dic_data = {row.French: row.English for (index, row) in data.iterrows()}
# print(dic_data)
# {'partie': 'part', 'histoire': 'history', 'chercher': 'search', 'seulement': 'only', 'police': 'police', 'pensais': 'thought', 'aide






window.mainloop()