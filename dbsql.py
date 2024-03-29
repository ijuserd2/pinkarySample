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
def fetch_user_fullname(email, pwd):
    fetch_user_pass_sql = "SELECT FullName FROM Users WHERE Email = '"+email+"' AND Pass ='"+pwd+"' COLLATE Latin1_General_CS_AS"
    cursor.execute(fetch_user_pass_sql)
    db_full_name = cursor.fetchone()[0]
    return db_full_name
def fetch_test_user_pagesettings():
    fetch_sql = "SELECT BgColor FROM UserPageSettings WHERE UserId = 11"
    cursor.execute(fetch_sql)
    db_bgcolor = cursor.fetchone()[0]
    fetch_sql = "SELECT BorderRadius FROM UserPageSettings WHERE UserId = 11"
    cursor.execute(fetch_sql)
    db_border_radius = cursor.fetchone()[0]
    return [db_bgcolor, db_border_radius]

def set_test_user_pagesettings(bgcolor, borderradius):
    set_sql = "UPDATE UserPageSettings SET BgColor = '" + bgcolor + "', BorderRadius = '" + borderradius + "' WHERE UserId = 11"
    cursor.execute(set_sql)
    cursor.commit()

#fetch_test_user_pagesettings()
#set_test_user_pagesettings("red","50px")
#fetch_test_user_pagesettings()
#sign_up('john','doe','johndoe2@email.com','2468john')
#print_users()
#email_pass_check('name@email.com', '1234567891')
#print(fetch_user_pass('johndoe2@email.com'))

