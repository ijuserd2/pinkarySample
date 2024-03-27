# coding: utf8

from flask import Flask, render_template, request, redirect, url_for
import dbsql

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/home/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/register/', methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":

        full_name = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("pwd")
        #dbsql.sign_up(full_name,username,email,password)

        return redirect(url_for('home'))

@app.route('/user/', methods=['GET','POST'])
def user():
    return render_template('user.html')

@app.route('/profile/', methods=['GET','POST'])
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=True)