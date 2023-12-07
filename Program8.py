import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", user="root", password="root",database="SMS"
)
sql = " update Course set Cname = 'DDDDDD' where cid = 12"
mycursor = mydb.cursor()
mycursor.execute(sql)
mydb.commit()
print("data entered to Course")