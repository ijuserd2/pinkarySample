import pyodbc

def db_connect():
    cnxn = pyodbc.connect(
        Trusted_Connection='yes',
        Driver='{ODBC Driver 17 for SQL Server}',
        Server='DESKTOP-5C8RGPJ\SQLEXPRESS',
        Database='ProjectDB'
    )
    return cnxn
