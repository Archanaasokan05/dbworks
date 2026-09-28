import mysql.connector

# ### from mysql import connector

# con=mysql.connector.connect(user="root",password="root",host="localhost")

# # establish connection between Python code and mysql server
# # it returns a connection object
#
# print(con)       #connection object
#
# c=con.cursor()   #cursor object used to execute sql queries/commands
#
# # c.execute(command)
# # create database file
#
# c.execute("create database school_db")
# print("Database file created")

con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")
c=con.cursor()

# c.execute('''
# create table student(roll_no int primary key,
#                     name varchar(20),
#                     age int,
#                     place varchar(20),
#                     phone varchar(12),
#                     total_mark int)''')
#
# print("Table created successfully")

# # c.execute("drop table student;")
# # c.execute("alter table student add age int")

# c.execute(''' insert into student(roll_no,name,age,place,phone,total_mark)
#                     values(101,"ASWIN",21,"ALUVA","8590543533",179),
#                           (102,"ATHUL",22,"EKM","9495-33129",160),
#                           (103,"AMAL",25,"KOCHI","0983764836",155),
#                           (104,"DIYA",22,"CHENNAI","6753764836",165),
#                           (105,"REENA",20,"PKD","9543764836",140)''')


# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"          #%s --place holder

# data=(106,"KIRAN",26,"TVM","8956743875",135)

# c.execute(query,data)
# con.commit()    #TO SAVE DATA PERMENANTLY
#
# print("SUCCEFULLY INSERTED")

# query="select * from student"
# c.execute(query)
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("No records found")

# # read all attributes of a student with roll number=roll number entered by user
# number=int(input("Enter roll number:"))
# query="select * from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print("no record found")

# # update mark of a student with roll number=roll number entered by user
# number=int(input("Enter roll number:"))
# mark=int(input("Enter new mark:"))
# query="update student set total_mark=%s where roll_no=%s"
# data=(mark,number,)
# c.execute(query,data)
# con.commit()
# print("Mark Updated")

# # delete a record with roll number=roll number entered by user
# number=int(input("Enter roll number:"))
# query="delete from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# con.commit()
# print("Deleted")

# # create a new record using values entered by user
# rollno=int(input("Enter roll number:"))
# name=input("Enter name:")
# age=int(input("Enter age:"))
# place=input("Enter place:")
# phone=input("Enter phone no:")
# mark=int(input("Enter total mark:"))
# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
# data=(rollno,name,age,place,phone,mark)
# c.execute(query,data)
# con.commit()
# print("Added")

