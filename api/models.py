from flask import make_response, abort, request,jsonify, json
from werkzeug.security import safe_str_cmp
from .utilities import Database
import psycopg2
import jwt
from flask.views import MethodView
import datetime
from psycopg2.extras import DictCursor

#from passlib.hash import pbkdf2_sha256 as sha256


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

            print("Avilaible ride")
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
        
        cur = c.cursor(cursor_factory=DictCursor)

        
        SQL = ''' INSERT INTO rides (ride_id, d_name,origin,departure_time,destination,cost, ride_status) 
                    VALUES(%s, %s, %s, %s, %s, %s, %s)'''
        cur.execute(SQL,  (ride.ride_id, ride.d_name, ride.origin, ride.departure_time,ride.destination, ride.cost, ride.ride_status))
           
            
       
    @classmethod
    def update_ride(cls, ride_id):
        data=request.get_json()
        cur = c.cursor(cursor_factory=DictCursor)
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

class Request(object):
    """ A class to handle actions related to requests"""

    def __init__(self, request_id, user_id, request_status, ride_id):
        # Initializes the ride object
        self.request_id = request_id
        self.user_id = user_id
        self.ride_id =ride_id
        self.requests_list = []

        


    def existing_request(self, origin, ride_id):
        """A method to check if the same request exists """
        for request_object in self.requests_list:
            if request_object['origin'] == origin and request_object['ride_id'] == ride_id:
                return True
        else:
            return False


    def create_request(self,ride_request):
        cur = c.cursor(cursor_factory=DictCursor)
        SQL = ''' INSERT INTO requests (user_id, ride_id, request_status) 
                    VALUES(%s, %s, %s)'''
        cur.execute(SQL, (ride_request.user_id, ride_request.ride_id, ride_request.request_status))
        

    def fetch_all_requests(self):
        "a method to fetch all requests"
        cur = c.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT *  from rides WHERE ride_status='False'")
        rows = cur.fetchall()
        for row in rows:
            print("ride_id = "), row[0]
            print("d_name = "), row[1]
            print("origin = "), row[2]
            print("destination = "), row[3]
            print("ride_status = "), row[4]
            print("cost = "), row[4]
            print("ride_status = "), row[5], "\n"

            print("Avilaible ride Requests")
        c.close()

    def fetch_request_by_id(self, request_id):
        """A method to f given an title of a request"""
        for request_object in self.requests_list:
            if request_object['request_id'] == request_id:
                return request_object
        return False

    def modify_request(self, request_id, item, ride_status,
                       origin, status):
        """ Find a request with the given id and modify its details"""

        for request_object in self.requests_list:
            if request_object['request_id'] == request_id:
                self.requests_list.remove(request_object)
                
                request_object['ride_status'] = ride_status
                request_object['origin'] = origin
                request_object['status'] = status
                request_object['request_id'] = request_id
                self.requests_list.append(self.data)
                return "request modifyied"
        else:
            return "no request with given id"
            
            

    
def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
