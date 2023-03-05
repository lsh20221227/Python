from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("index.html",posts=data)


@app.route('/post/<int:num>')
def blog_post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()
    return render_template("post.html", posts=data,num=num)


if __name__ == "__main__":
    app.run(debug=True)
