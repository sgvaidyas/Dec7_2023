import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", user="root", password="root"
)
mycursor = mydb.cursor()
mycursor.execute("show databases")
print(type(mycursor))
for x in mycursor:
    print(x)
