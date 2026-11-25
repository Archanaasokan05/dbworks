import mysql.connector

class PersonDB:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="person_db")
            print(self.con)
        except:
            print("Failed to Connect")

    def create(self,id,name,age):
        try:
            cursor=self.con.cursor()
            query="insert into Person(id,name,age)values(%s,%s,%s)"
            data=(id,name,age)
            cursor.execute(query,data)
            self.con.commit()
            print("Insert record successfully")

        except:
            print("Failed yo insert")

    def read(self):
        try:
            cursor=self.con.cursor()
            query="select*from Person"
            cursor.execute(query,)
            records=cursor.fetchall()
            if records:
                for row in records:
                    print(row)
            else:
                print('No records Found')
        except:
            print("Failed To Read")

    def retrieve(self,id):
        try:
            cursor=self.con.cursor()
            query="select * from Person where id=%s"
            data=(id,)
            cursor.execute(query,data)
            record=cursor.fetchone()
            if record:
                print(record)
            else:
                print("No records found")
        except:
            print("Failed to Retrieve")

    def update(self, id, name, age):
        try:
            cursor = self.con.cursor()
            query = "update person set name=%s,age=%s where id=%s"
            data = (name, age, id)
            cursor.execute(query, data)
            self.con.commit()
            if cursor.rowcount > 0:
                print('RECORD UPDATED SUCCESSFULLY')
            else:
                print('ID NOT FOUND')
        except:
            print("FAILED TO UPDATE")


    def delete(self, id):
        try:
            cursor = self.con.cursor()
            query = 'delete from person where id=%s'
            data = (id,)
            cursor.execute(query, data)
            self.con.commit()
            if cursor.rowcount > 0:
                print('RECORD DELETED SUCCESSFULLY')
            else:
                print('ID NOT FOUND')
        except:
            print("FAILED TO DELETE")


p=PersonDB()

while(1):
    print('1.Create')
    print('2.Read')
    print('3.Retrieve')
    print('4.Update')
    print('5.Delete')
    print('6.Exit')

    ch=int(input("Enter choice:"))
    if ch==1:
        id=int(input("Enter id:"))
        n=input("Enter name:")
        a=int(input("Enter age:"))
        p.create(id,n,a)

    elif ch==2:
        p.read()

    elif ch==3:
        id=int(input("Enter id:"))
        p.retrieve(id)

    elif ch==4:
        id=int(input("Enter id:"))
        n=input("Enter name:")
        a=int(input("Enter age:"))
        p.update(id,n,a)

    elif ch==5:
        id=int(input("Enter id:"))
        p.delete(id)

    else:
        exit()
