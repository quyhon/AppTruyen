import pyodbc 

def checkUser(user,password):
    """Find user in DB"""
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-QOPGE90;'
                        'Database=PTPM;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()
    query = "SELECT * FROM USERS where username = '{}'".format(user)
    try:
        cursor.execute(query)
        row= [list(_) for _ in cursor ][0]
        if row[1]==password:
            return 1
        else:
            return 0
    except:
        return 0
def register(data):
    """Insert Data to DB"""
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-QOPGE90;'
                        'Database=PTPM;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()
    query = "INSERT INTO USERS(username,pass,name,sex) VALUES (N'{}',N'{}',N'{}',N'{}')".format(data[0],data[1],data[2],data[3])
    try:
        cursor.execute(query)
        conn.commit()
        return 1
    except:
        return 0