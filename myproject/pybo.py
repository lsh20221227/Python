from flask import Flask
app = Flask(__name__)

print(__name__)

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'

@app.route("/bye")
def say_bye():
    return "Bye"


if __name__=="__main__":
    app.run()

# https://wikidocs.net/81043 (설치 참고)