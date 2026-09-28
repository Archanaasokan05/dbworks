import mysql.connector

# # Create a database named shop
#
# con=mysql.connector.connect(user="root",password="root",host="localhost")
# print(con)
# c=con.cursor()
# c.execute("create database shop")
# print("Database created")

# # Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
con=mysql.connector.connect(user="root",password="root",host="localhost",database="shop")
c=con.cursor()

# c.execute('''
# # create table product(product_id int primary key,
# #                     name varchar(20),
# #                     brand varchar(20),
# #                     category varchar(20),
# #                     price int,
# #                     stock int)''')
#
# print("Table created successfully")

# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit

def insert():
    product_id = int(input("Enter product id:"))
    name = input("Enter product name:")
    brand = input("Enter the brand:")
    cat = input("Enter the category:")
    price = int(input("Enter price:"))
    stock = int(input("Enter stock:"))
    query = "insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)"
    data = (product_id, name, brand, cat, price, stock,)
    c.execute(query, data)
    con.commit()

def read():
    query="select * from product"
    c.execute(query)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("No records found")

def search():
    p_id=int(input("Enter product id:"))
    query="select * from product where product_id=%s"
    data=(p_id,)
    c.execute(query,data)
    records=c.fetchone()
    if records:
        print(records)
    else:
        print("no records found")

def update():
    p_id=int(input("Enter product id:"))
    stock=int(input("Enter new stock:"))
    query="update product set stock=%s where product_id=%s"
    data=(stock,p_id,)
    c.execute(query,data)
    con.commit()
    print("STOCK UPDATED")

def delete():
    p_id=int(input("Enter product id:"))
    query="delete from product where product_id=%s"
    data=(p_id,)
    c.execute(query,data)
    con.commit()
    print("DELETED SUCCESSFULLY")

while(1):
    print("-----MENU DRIVEN-----")
    print("1. Insert Product details\n2. Read all Product details\n3. Search a Product by product_id\n"
          "4. Update the stock of a Product\n5. Delete a Product record\n6. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        insert()
    elif ch==2:
        read()
    elif ch==3:
        search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
        exit()
    else:
        print("Invalid input")


