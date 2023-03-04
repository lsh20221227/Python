from flask import Flask, render_template
import datetime
import requests
import random

app = Flask(__name__)


@app.route('/')
def home():
    years = datetime.datetime.now().year
    num = random.randint(1,10)
    return render_template("index.html",year=years, num=num)

@app.route(f'/guess/<name>')
def api_test(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    genders = gender_data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    ages = age_data["age"]
    return render_template("test.html",person_name=name, gender = genders,age=ages)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url="https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts=all_posts)
if __name__ == "__main__":
    app.run(debug=True)



