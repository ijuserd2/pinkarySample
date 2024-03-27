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
    sign_up_sql = "INSERT INTO Users(FullName, UserName, Email, Pass, DataCreated, DataModified) VALUES ('"+name+"', '"+username+"', '"+email+"', '"+pwd+"', GETDATE(), GETDATE())"
    cursor.execute(sign_up_sql)
    cursor.commit()
def email_pass_check(email, pwd):
    email_pass_check_sql = "SELECT * FROM USERS WHERE Email = '"+email+"' AND Pass ='"+pwd+"' "
    cursor.execute(email_pass_check_sql)

def fetch_user_pass(email):
    fetch_user_pass_sql = "SELECT Pass FROM Users WHERE Email = '"+email+"'"
    cursor.execute(fetch_user_pass_sql)
    dbpass = cursor.fetchall()[0][0]
    return dbpass
#sign_up('john','doe','johndoe2@email.com','2468john')
print_users()
#print(fetch_user_pass('johndoe2@email.com'))

