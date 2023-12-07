import mysql.connector
fp = open('mydata','r')
content = fp.readlines()
master = []
for x in content:
    n = x.split("=")
    print(n[1])
    master.append(n[1][:-1])
print(master)
'''
mydb=mysql.connector.connect(
    host="localhost", user=master[0], password=master[1],database="SMS"
)
mycursor = mydb.cursor()
sql = "insert into Student values(99,'SS Jack',99,999)"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("select * from Student")
for rec in mycursor:
    print(rec)
'''