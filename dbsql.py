import pyodbc
import dbconnect

conn = dbconnect.db_connect()

cursor = conn.cursor()
#cursor.execute("INSERT INTO Users(FullName, UserName, Email, Pass, DataCreated, DataModified) VALUES ('Joe', 'userjoe', 'joesmith@gmail.com', '2468pass', GETDATE(), GETDATE())")
def print_users():
    cursor.execute("SELECT * FROM ProjectDB.dbo.Users")
    row = cursor.fetchall()
    print (row)

def sign_up(name, username, email, pwd):
    sign_up_sql = "INSERT INTO Users(FullName, UserName, Email, Pass, Bio, DataCreated, DataModified) VALUES ('"+name+"', '"+username+"', '"+email+"', '"+pwd+"', '', GETDATE(), GETDATE())"
    cursor.execute(sign_up_sql)
    cursor.commit()
def email_pass_check(email, pwd):
    email_pass_check_sql = "SELECT * FROM Users WHERE Email = '"+email+"' AND Pass ='"+pwd+"' COLLATE Latin1_General_CS_AS"
    cursor.execute(email_pass_check_sql)
    data = cursor.fetchone()
    return data

def fetch_user_pass(email):
    fetch_user_pass_sql = "SELECT Pass FROM Users WHERE Email = '"+email+"'"
    cursor.execute(fetch_user_pass_sql)
    dbpass = cursor.fetchall()[0][0]
    return dbpass

def fetch_user_by_username(username):
    fetch_user_sql = "SELECT * FROM Users WHERE UserName = '"+username+"'"
    cursor.execute(fetch_user_sql)
    dbuser = cursor.fetchone()
    return dbuser

def fetch_username_by_email(email):
    fetch_username_sql = "SELECT UserName FROM Users WHERE Email = '"+email+"'"
    cursor.execute(fetch_username_sql)
    dbuname = cursor.fetchone()[0]
    print(dbuname)
    return dbuname
def fetch_user_id(email):
    fetch_user_id_sql = "SELECT UserId FROM Users WHERE Email = '"+email+"'"
    cursor.execute(fetch_user_id_sql)
    dbid = cursor.fetchall()[0][0]
    return dbid

def fetch_user_id_by_username(username):
    fetch_user_id_sql = "SELECT UserId FROM Users WHERE UserName = '"+username+"'"
    cursor.execute(fetch_user_id_sql)
    try:
        dbid = cursor.fetchall()[0][0]
    except Exception:
        dbid = None
        pass
    return dbid
def fetch_user_pass_by_id():
    fetch_user_pass_sql = "SELECT Pass FROM Users WHERE UserId = 11 "
    cursor.execute(fetch_user_pass_sql)
    dbpass = cursor.fetchall()[0][0]
    return dbpass
def fetch_user_fullname(userid):
    fetch_user_pass_sql = "SELECT FullName FROM Users WHERE UserId ='"+userid+"' COLLATE Latin1_General_CS_AS"
    cursor.execute(fetch_user_pass_sql)
    db_full_name = cursor.fetchone()[0]
    print(db_full_name)
    return db_full_name
def fetch_test_user_pagesettings(userid):
    fetch_sql = "SELECT BgColor FROM UserPageSettings WHERE UserId ='"+userid+"'"
    cursor.execute(fetch_sql)
    db_bgcolor = cursor.fetchone()[0]
    fetch_sql = "SELECT BorderRadius FROM UserPageSettings WHERE UserId = '"+userid+"'"
    cursor.execute(fetch_sql)
    db_border_radius = cursor.fetchone()[0]
    return [db_bgcolor, db_border_radius]

def set_test_user_pagesettings(bgcolor, borderradius, userid):
    set_sql = "INSERT INTO UserPageSettings(UserId, BgColor, BorderRadius, DataCreated, DataModified) VALUES ('"+userid+"', '"+bgcolor+"', '"+borderradius+"', GETDATE(), GETDATE())"
    cursor.execute(set_sql)
    cursor.commit()
def fetch_test_links(userid):
    fetch_sql = "SELECT * FROM ProjectDB.dbo.Links WHERE UserId = '"+userid+"'"
    cursor.execute(fetch_sql)
    db_link_data = cursor.fetchall()
    return db_link_data

def fetch_pagesettings_by_username(username):
    fetch_sql = "SELECT BgColor FROM UserPageSettings WHERE UserId ='"+username+"'"
    cursor.execute(fetch_sql)
    db_bgcolor = cursor.fetchone()[0]
    fetch_sql = "SELECT BorderRadius FROM UserPageSettings WHERE UserId = '"+username+"'"
    cursor.execute(fetch_sql)
    db_border_radius = cursor.fetchone()[0]
    return [db_bgcolor, db_border_radius]

def fetch_links_by_username(username):
    fetch_sql = "SELECT * FROM ProjectDB.dbo.Links WHERE UserName = '"+username+"'"
    cursor.execute(fetch_sql)
    db_link_data = cursor.fetchall()
    return db_link_data

def set_test_links(desc, link, userid):
    set_sql = "INSERT INTO Links(UserId, Description, Link, DataCreated, DataModified) VALUES ('"+userid+"', '"+desc+"', '"+link+"', GETDATE(), GETDATE())"
    cursor.execute(set_sql)
    cursor.commit()

def update_test_user_acc(name, username, email, bio, userid):
    update_sql = "UPDATE Users SET FullName = '" + name + "', UserName = '" + username + "', Email = '" + email + "', Bio = '" + bio + "', DataModified = GETDATE() WHERE UserId = '"+userid+"'"
    cursor.execute(update_sql)
    cursor.commit()

def update_test_user_pass(old_pwd, new_pwd, c_new_pwd, userid):
    old_pwd_fetched = fetch_user_pass_by_id()
    if(old_pwd != old_pwd_fetched):
        print("old pwd wrong")
        return False
    if(new_pwd != c_new_pwd):
        print("new_pwd not same with confirm_new_pw")
        return False
    if (old_pwd == new_pwd):
        print("old pwd same with new pwd")
        return False
    update_sql = "UPDATE Users SET Pass = '" + new_pwd + "', DataModified = GETDATE() WHERE UserId = '"+userid+"'"
    cursor.execute(update_sql)
    cursor.commit()

#fetch_username_by_email("new@email.com")
#update_test_user_pass("123456newe", "123456newx", "123456newx")
#set_test_links("descr3","www.tumblr.com")
#fetch_test_user_pagesettings()
#set_test_user_pagesettings("to right,red,blue","0")
#fetch_test_user_pagesettings()
#sign_up('john','doe','johndoe2@email.com','2468john')
#print_users()
#email_pass_check('name@email.com', '1234567891')
#print(fetch_user_pass('johndoe2@email.com'))

