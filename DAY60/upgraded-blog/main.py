from flask import Flask,render_template, request
import requests



app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/9836678c273a1c7f9edb")
    data = response.json()
    return render_template("index.html",post=data)

@app.route('/about')
def about_page():
    return render_template("about.html")

# @app.route('/contact')
# def contact_page():
#     return render_template("contact.html")

@app.route('/post-<int:num>')
def post_page(num):
    response = requests.get(url="https://api.npoint.io/9836678c273a1c7f9edb")
    datas = response.json()
    data=None
    for blog_data in datas:
        if blog_data["id"] == num:
            data=blog_data
    return render_template("post.html",post=data)


@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method =="POST":
        data= request.form
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['phone'])
        print(request.form['message'])
        return render_template('contact.html', msg_sent=True)
    return render_template("contact.html", msg_sent=False)

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     data= request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return "<h1>Successfully sent your message</h1>"




if __name__ == "__main__":
    app.run(debug=True)

