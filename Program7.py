import mysql.connector
master = []
fp = open('mydata','r')
master = fp.read()
m = master.split('\n')
master=[]
for x in m:
    d = x.split(',')
    print(d)
    if(len(d)==3):
        master.append((int(d[0]),d[1],d[2]))
print(master)

'''
mydb=mysql.connector.connect(
    host="localhost", user="root", password="root",database="SMS"
)

sql = " insert into Course values(%s,%s,%s)"
mycursor = mydb.cursor()
mycursor.executemany(sql,master)
mydb.commit()

print("data entered to Course")'''