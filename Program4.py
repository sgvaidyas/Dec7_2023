import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", user="root", password="root",database="SMS"
)
mycursor = mydb.cursor()
mycursor.execute("select name from Student")

for x in mycursor:
    print(x)

