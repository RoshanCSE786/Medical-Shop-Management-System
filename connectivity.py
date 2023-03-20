import mysql.connector as c
con = c.connect(host="localhost",user="root",passwd="Roshan@01",database="my_db")
if con.is_connected():
    print("successfully connected...")
else:
    print("some connectivity issue..")
    
