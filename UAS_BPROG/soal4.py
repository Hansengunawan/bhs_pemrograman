import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='hansengans2016',
    database =''
)
 
cursor = db.cursor()
cursor.execute("Create Database BPROG")

print("database berhasil")

# if db.is_connected():
#     print("berhasil")
