# coding: utf8

from flask import Flask, render_template, request, redirect, url_for, session
import dbsql
import page_settings

app = Flask(__name__)
app.secret_key = "super secret key"
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/home/', methods=['GET','POST'])
def home():
    if 'email' in session:
        return render_template('home.html', email=session['email'])
    return redirect(url_for('login'))
@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pwd")
        check = dbsql.email_pass_check(email, password)
        if(check!=None):
            session['email'] = email
            userid = dbsql.fetch_user_id(email)
            session['userid'] = userid
            return redirect(url_for('home'))
        return redirect(url_for('login'))

@app.route('/u/<username>', methods=['GET','POST'])
def u(username):

    userid = dbsql.fetch_user_id_by_username(username)
    userid = str(userid)
    check_username = dbsql.fetch_user_by_username(username)
    if(check_username!=None):
        try:
            linkdata = dbsql.fetch_test_links(userid)
            settingsvalues = dbsql.fetch_test_user_pagesettings(userid)
            return render_template('user.html', bgcolor=settingsvalues[0], borderradius=settingsvalues[1],
                                   linkdata=linkdata)
        except Exception:
            pass
    return redirect(url_for('home'))

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
        return redirect(url_for('login'))

@app.route('/user/', methods=['GET','POST'])
def user():
    if request.method == "GET":
        linkdata = dbsql.fetch_test_links()
        settingsvalues = dbsql.fetch_test_user_pagesettings()
        return render_template('user.html', bgcolor = settingsvalues[0], borderradius = settingsvalues[1], linkdata = linkdata)
    if request.method == "POST":
        if (request.form["page-setting"] == "bgcolor-borderradius"):
            border_radius = request.form.get("border-radius-rate")
            bg_color = request.form.get("bg-color-set")
            values = page_settings.check(bg_color, border_radius)
            dbsql.set_test_user_pagesettings(values[0], values[1])

            linkdata = dbsql.fetch_test_links()
            settingsvalues = dbsql.fetch_test_user_pagesettings()
            return render_template('user.html', bgcolor=settingsvalues[0], borderradius=settingsvalues[1], linkdata = linkdata)

        if (request.form["page-setting"] == "link"):
            description = request.form.get("description")
            link = request.form.get("link")
            dbsql.set_test_links(description, link)

            linkdata = dbsql.fetch_test_links()
            settingsvalues = dbsql.fetch_test_user_pagesettings()
            return render_template('user.html', bgcolor=settingsvalues[0], borderradius=settingsvalues[1], linkdata = linkdata)

        linkdata = dbsql.fetch_test_links()
        settingsvalues = dbsql.fetch_test_user_pagesettings()
        return render_template('user.html', bgcolor=settingsvalues[0], borderradius=settingsvalues[1], linkdata = linkdata)

@app.route('/logout/', methods=['GET','POST'])
def logout():
    session.pop('email', None)
    session.pop('userid', None)
    return redirect(url_for('login'))
@app.route('/profile/', methods=['GET','POST'])
def profile():
    if 'email' in session:
        if request.method == "GET":
            return render_template('profile.html')
        if request.method == "POST":
            if (request.form["update_acc"] == "acc"):
                name = request.form.get("fullname")
                username = request.form.get("username")
                email = request.form.get("email")
                bio = request.form.get("bio")
                dbsql.update_test_user_acc(name, username, email, bio)

                return render_template('profile.html')
            if (request.form["update_acc"] == "pwd"):
                old_pwd = request.form.get("old_pwd")
                new_pwd = request.form.get("new_pwd")
                c_new_pwd = request.form.get("c_new_pwd")
                dbsql.update_test_user_pass(old_pwd, new_pwd, c_new_pwd)
                return render_template('profile.html')

            return render_template('profile.html')

    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)