import mysql.connector
master = []
def addCourse():
    id = int(input("Enter Course ID = "))
    name = input("Enter Course Name = ")
    des =  input("Enter Course Desc = ")
    return id,name,des

while True:
    rec = addCourse()
    master.append(rec)
    ch = input("Press q to stop")
    if ch == "q":
        break
print(master)


mydb=mysql.connector.connect(
    host="localhost", user="root", password="root",database="SMS"
)

sql = " insert into Course values(%s,%s,%s)"
mycursor = mydb.cursor()
mycursor.executemany(sql,master)
mydb.commit()

print("data entered to Course")
