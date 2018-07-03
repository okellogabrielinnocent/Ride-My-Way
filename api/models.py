from flask import make_response, abort, request,jsonify, reqparse
from .tb import Database
import psycopg2

JSON_MIME_TYPE = 'application/json'



c = Database.conn
class Ride(object):
    # A Rides class

    def __init__(self, ride_id, origin, d_name, destination, date, status = "False"):
        # Initializes the ride object
        self.ride_id = ride_id
        self.origin = origin
        self.d_name =d_name
        self.destination = destination
        self.date = date
        self.status = status


    @classmethod
    def get_rides(self):
        cur = c.cursor()
        cur.execute("SELECT *  from rides")
        rows = cur.fetchall()
        for row in rows:
            print ("ride_id = "), row[0]
            print ("d_name = "), row[1]
            print ("origin = "), row[2]
            print ("destination = "), row[3]
            print ("status = "), row[4]
            print ("cost = "), row[4]
            print ("departure_time = "), row[5], "\n"

            print ("Avilaible ride")
        c.close()




#get ride by id
    @classmethod
    def get_ride(self, ride_id):
        cur = c.cursor()
        cur.execute("SELECT *  from rides  where ride_id = %s,(ride_id)")
        rows = cur.fetchone()
        for row in rows:
            print ("ride_id = "), row[0]
            print ("d_name = "), row[1]
            print ("origin = "), row[2]
            print ("destination = "), row[3]
            print ("status = "), row[4]
            print ("cost = "), row[4]
            print ("departure_time = "), row[5], "\n"

            print ("Avilaible ride")
        c.close()

        
                
       

    @classmethod
    def post_ride(self, data):
        parser = reqparse.RequestParser()
        parser.add_argument("origin")
        parser.add_argument("destination")
        parser.add_argument("cost")
        parser.add_argument("departure_time")
        args = parser.parse_args()

        for ride in rides:
            if(name == ride["name"]):
                return "Ride with name {} already exists".format(name), 400

        ride = {
            "name": name,
            "origin": args["origin"],
            "destination": args["destination"],
            "cost": args["cost"],
            "departure_time":args["departure_time"]
        }
        rides.append(ride)
        return ride, 201
        cur = c.cursor()
        try:
            cur.execute("INSERT INTO rides(ride_id,d_name,origin,destination,departure_time,cost,status)"
                           " VALUES(%s, %s, %s, %s, %s, %s, $s)",
                           (data['ride_id'], data['d_name'], data['origin'], data['destination'], data['departure_time']
                            , data['cost'], data['status'],))
            
            
            c.commit()

            return True
        except:
            c.rollback()

            return False
        finally:
            c.close()


       
    @classmethod
    def update_ride(cls,ride_id,data):
        cur = c.cursor()
        ride = [ride for ride in data if ride['ride_id'] == ride_id]
        if len(ride) == 0:
            abort(404)
        if not request.json:
            abort(400)
        if 'origin' in request.json and type(request.json['origin']):
            abort(400)
        if 'd_name' in request.json and type(request.json['d_name']):
            abort(400)
        if 'destination' in request.json and type(request.json['destination']) is not bool:
            abort(400)
        if 'date' in request.json and type(request.json['date']):
            abort(400)
        if 'date' in request.json and type(request.json['date']):
            abort(400)
        if 'status' in request.json and type(request.json['status']) is  bool:
            abort(400)

        try:
            cur.execute("UPDATE rides set d_name = %s, origin = %s, destination = %s,"
                           " departure_time = %s, cost = $s where ride_id = %s",
                           (data['ride_id'], data['d_name'], data['origin'], data['destination'], data['departure_time']
                            , data['cost'], data['status'],))
            c.commit()

            return True
        except:
            c.rollback()

            return False


    # define json response header
    @classmethod
    def json_response(data='', status=200, headers=None):
        headers = headers or {}
        if 'Content-Type' not in headers:
            headers['Content-Type'] = JSON_MIME_TYPE

        return make_response(data, status, headers)
