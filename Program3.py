import mysql.connector
mydb=mysql.connector.connect(
    host="localhost", user="root", password="root",database="SMS"
)

sql = "insert into Course values(%s,%s,%s)"
data = [
    (11,'python','with mysql'),
    (12, 'C', 'data structures'),
    (13, 'C++', 'with oops')
]
mycursor = mydb.cursor()
mycursor.executemany(sql,data)
mydb.commit()



