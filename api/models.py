from flask import make_response, abort, request,jsonify, json
from werkzeug.security import safe_str_cmp
from .utilities import Database
import psycopg2
import jwt
from flask.views import MethodView
import datetime
from psycopg2.extras import DictCursor


JSON_MIME_TYPE = 'application/json'


c = Database.conn
class Ride(object):
    # A Rides class

    def __init__(self, ride_id, d_name,  origin, destination, cost, departure_time, date, ride_status="False"):
        # Initializes the ride object
        self.ride_id = ride_id
        self.origin = origin
        self.d_name =d_name
        self.destination = destination
        self.departure_time = departure_time
        self.cost = cost
        self.date = date
        self.ride_status = ride_status

    @classmethod
    def get_rides(cls):
        cur = c.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT *  from rides")
        rows = cur.fetchall()
        for row in rows:
            print("ride_id = "), row[0]
            print("d_name = "), row[1]
            print("origin = "), row[2]
            print("destination = "), row[3]
            print("ride_status = "), row[4]
            print("cost = "), row[4]
            print("departure_time = "), row[5], "\n"
            response = json.dumps(rows)
            return jsonify(response)
            
        c.close()

    '''get ride by id'''
    @classmethod
    def get_ride(cls):
        cur = c.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT *  from rides  where ride_id = %s,(ride_id)")
        rows = cur.fetchone()
        for row in rows:
            print("ride_id = "), row[0]
            print("d_name = "), row[1]
            print("origin = "), row[2]
            print("destination = "), row[3]
            print("ride_status = "), row[4]
            print("cost = "), row[5]
            print("departure_time = "), row[6].strftime("%b %d %Y %H:%M:%S", time.gmtime(t)), "\n"
            response = json.dumps(rows)
            return jsonify(response)
        c.close()


    @staticmethod
    def post_ride(ride):
        
        try:
        
            cur = c.cursor(cursor_factory=DictCursor)

            
            SQL = ''' INSERT INTO rides (ride_id, d_name,origin,departure_time,destination,cost, ride_status) 
                        VALUES(%s, %s, %s, %s, %s, %s, %s)'''
            cur.execute(SQL,  (ride.ride_id, ride.d_name, ride.origin, ride.departure_time,ride.destination, ride.cost, ride.ride_status))
            return True
        except:
            c.rollback()

            return False
            
            
class User(object):
    
    def __init__(self, username, email,  password):
        # Initializes the user object
        
        self.email = email
        self.username = username
        self.password = password
    
    @staticmethod
    def post_user(user):
        cur = c.cursor(cursor_factory=DictCursor)
        SQL = ''' INSERT INTO users (username, email, password) 
                    VALUES(%s, %s, %s)'''
        cur.execute(SQL, (user.username, user.email, user.password))
        


    @staticmethod
    def get_login(username, password):
        cur = c.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT * FROM users WHERE username=%s AND password =%s",(username, password)) 
        dbuser = cur.fetchone()
        return  dbuser

   
def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
