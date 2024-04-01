# coding: utf8

from flask import Flask, render_template, request, redirect, url_for
import dbsql
import page_settings

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/home/', methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pwd")
        check = dbsql.email_pass_check(email, password)
        if(check!=None):
            hello_user = "Hello" + dbsql.fetch_user_fullname(email, password)+"!"
            return redirect(url_for('home',hello_user="hello_user"))
        return redirect(url_for('login'))

@app.route('/register/', methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":

        full_name = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("pwd")
        dbsql.sign_up(full_name,username,email,password)

        return redirect(url_for('home'))

@app.route('/user/', methods=['GET','POST'])
def user():
    if request.method == "GET":
        settingsvalues = dbsql.fetch_test_user_pagesettings()
        return render_template('user.html', bgcolor = settingsvalues[0], borderradius = settingsvalues[1])
    if request.method == "POST":
        if (request.form["page-settings"] == "bgcolor-borderradius"):
            border_radius = request.form.get("border-radius-rate")
            bg_color = request.form.get("bg-color-set")
            values = page_settings.check(bg_color, border_radius)
            dbsql.set_test_user_pagesettings(values[0], values[1])
            print(values[0],values[1])
            settingsvalues = dbsql.fetch_test_user_pagesettings()
            return render_template('user.html', bgcolor=settingsvalues[0], borderradius=settingsvalues[1])

        settingsvalues = dbsql.fetch_test_user_pagesettings()
        return render_template('user.html', bgcolor=settingsvalues[0], borderradius=settingsvalues[1])

@app.route('/profile/', methods=['GET','POST'])
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.run(debug=True)