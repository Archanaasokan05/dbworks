
# Question 1 — Employee Salary Management
#
import mysql.connector
# con=mysql.connector.connect(user="root",password="root",host="localhost")
# c=con.cursor()
# # ----Create a database named practice.
# c.execute("create database practice")
# print("DATABASE CREATED")

# # Create a table staff with:
# #
# # staff_id – Primary Key
# # name
# # department
# # salary
# # city
# # joining_year
# #
#
con=mysql.connector.connect(user="root",password="root",host="localhost",database="practice")
c=con.cursor()
#
# # c.execute('''
# # create table staff(staff_id int auto_increment primary key,
# #                     name varchar(20),
# #                     department varchar(30),
# #                     salary int,
# #                     city varchar(20),
# #                     joining_year int)''')
# print("TABLE ' STAFF ' CREATED SUCCESSFULLY")
#
# # Menu:
# #
# # 1. Insert Staff
# # 2. Display all Staff
# # 3. Search Staff by staff_id
# # 4. Update Staff salary
# # 5. Delete Staff
# # 6. Display staff with salary greater than a given amount
# # 7. Display staff from a particular department
# # 8. Display staff with the highest salary
# # 9. Exit
#
def insert():
    name=input("Enter Name:")
    department=input("Enter Department:")
    salary=int(input("Enter Salary:"))
    city=input("Enter City:")
    j_year=int(input("Enter Joining Year:"))
    query="insert into staff(name,department,salary,city,joining_year)values(%s,%s,%s,%s,%s)"
    data=(name,department,salary,city,j_year,)
    c.execute(query,data)
    con.commit()
    print("DATA INSERTED SUCCESSFULLY")

def display():
    query="select * from staff"
    c.execute(query)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("NO RECORDS FOUND")

def search():
    staff_id=int(input("Enter Staff ID:"))
    query="select * from staff where staff_id=%s"
    data=(staff_id,)
    c.execute(query,data)
    records=c.fetchone()
    if records:
        print(records)
    else:
        print("NO RECORDS FOUND")

def update():
    staff_id=int(input("Enter Staff ID:"))
    salary=int(input("Enter New Salary:"))
    query="update staff set salary=%s where staff_id=%s"
    data=(salary,staff_id,)
    c.execute(query,data)
    con.commit()
    print("SALARY UPDATED SUCCESSFULLY")

def delete():
    staff_id=int(input("Enter Staff ID:"))
    query="delete from staff where staff_id=%s"
    data=(staff_id,)
    c.execute(query,data)
    con.commit()
    print("DELETED SUCCESSFULLY")

def salary_greater():
    amount=int(input("Enter a given amount of Salary:"))
    query="select * from staff where salary>%s"
    data=(amount,)
    c.execute(query,data)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("NO RECORDS FOUND")

def particular_department():
    department=input("Enter Department:")
    query="select * from staff where department=%s"
    data=(department,)
    c.execute(query,data)
    records=c.fetchall()
    if records:
        for row in records:
            print(records)
    else:
        print("NO RECORDS FOUND")

def highest_salary():
    query="select * from staff where salary=(select max(salary)from staff)"
    c.execute(query)
    records=c.fetchone()
    if records:
        print(records)
    else:
        print("CAN'T FIND")

while(1):
    print("\n==== MENU ====\n")
    print('''1. Insert Staff
2. Display all Staff
3. Search Staff by staff_id
4. Update Staff salary
5. Delete Staff
6. Display staff with salary greater than a given amount
7. Display staff from a particular department
8. Display staff with the highest salary
9. Exit''')
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        insert()
    elif ch==2:
        display()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        salary_greater()
    elif ch==7:
        particular_department()
    elif ch==8:
        highest_salary()
    else:
        exit()