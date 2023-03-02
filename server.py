from flask import Flask
import random


random_int = random.randint(0,9)
print(random_int)
app = Flask(__name__)

@app.route('/')
def number_home():
    return "<h1> 0과 9사이의 숫자를 맞추세요 ! </h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>"

@app.route('/<int:number>')
def number_game(number):
    if number == random_int:
        return '<h1> You found me !</h1>' \
               '<img src="https://media1.giphy.com/media/trrtoypluzLdx4h9Cr/200w.webp?cid=ecf05e47gtlt7v4xl5s9kziph2c1vj37jc1syfw0wtf3iy4i&rid=200w.webp&ct=g" width=200>'
    elif random_int < number:
        return '<h1> Too high, try again !</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    else:
        return '<h1> Too low, try again !</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'

if __name__=="__main__":
    app.run(debug=True)

