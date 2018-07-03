import psycopg2
from flask import Flask


class Database:

    def connect(self):
        
        return psycopg2.connect("dbname=postgress user=postgres password=moschinogab19")
    
    def read(self, id):
        conn = Database.connect(self)
        cursor = conn.cursor()

        try:
            if id == id:
                cursor.execute("SELECT * FROM rides order by d_name asc")
            else:
                cursor.execute("SELECT * FROM rides where id = %s order by d_name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            conn.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO rides(ride_id,d_name,origin,destination,departure_time,cost,status)"
                           " VALUES(%s, %s, %s, %s, %s, %s, $s)",
                           (data['ride_id'], data['d_name'], data['origin'], data['destination'], data['departure_time']
                            , data['cost'], data['status'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE rides set d_name = %s, origin = %s, destination = %s,"
                           " departure_time = %s, cost = $s where ride_id = %s",
                           (data['ride_id'], data['d_name'], data['origin'], data['destination'], data['departure_time']
                            , data['cost'], data['status'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM rides where ride_id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

            