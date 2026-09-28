
                # ====== VEHICLE DB ======

## define a class to perform database operations on vehicle table

# #create a class named VehicleListCreateRetriveUpdateDelete
# and define methods

# list()--> read all records
# # create()-->for creating a new record
# # retrieve(id) --> for reading a specific record
# # update(id,data)--> for updating specific record
# # delete(id)--> for deleting a specific record

import mysql.connector

class VehicleListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection = mysql.connector.connect(user="root", password="root", host="localhost", database="vehicle_db")
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("SUCCESSFULLY CONNECTED")

    def list(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("NO RECORDS FOUND")

    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year)values(%s,%s,%s,%s,%s)"
        data=(brand,model,type,price,year)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("DATA INSERTED SUCCESSFULLY")

    def retrieve(self,id):
        query="select * from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("NO RECORDS FOUND")

    def update(self,brand,model,type,price,year,id):
        query="update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data=(brand,model,type,price,year,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("UPDATED SUCCESSFULLY")
        else:
            print("NO RECORDS FOUND")

    def delete(self,id):
        query="delete from vehicle where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("DELETED SUCCESSFULLY")
        else:
            print("NO RECORDS FOUND")


vehicle_instance = VehicleListCreateRetrieveUpdateDelete()

# vehicle_instance.list()
# vehicle_instance.create('Honda', 'City', 'Sedan', 1600000, 2022)
# vehicle_instance.retrieve(3)
# vehicle_instance.update('Volkswagen', 'Virtus', 'Sedan', 1500000, 2022,1)
vehicle_instance.delete(7)