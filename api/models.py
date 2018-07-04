from flask import make_response, abort, request,jsonify
from .utilities import Database
import psycopg2
from psycopg2.extras import RealDictCursor
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
        cur = c.cursor(cursor_factory=RealDictCursor)
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
        cur = c.cursor(cursor_factory=RealDictCursor)
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

            print("Avilaible ride")
        c.close()


    @staticmethod
    def post_ride(ride):
        
        cur = c.cursor(cursor_factory=RealDictCursor)

        
        SQL = ''' INSERT INTO rides (ride_id, d_name,origin,departure_time,destination,cost, ride_status) 
                    VALUES(%s, %s, %s, %s, %s, %s, %s)'''
        cur.execute(SQL,  (ride.ride_id, ride.d_name, ride.origin, ride.departure_time,ride.destination, ride.cost, ride.ride_status))

        

            
            
       
    @classmethod
    def update_ride(cls, ride_id):
        data=request.get_json()
        cur = c.cursor(cursor_factory=RealDictCursor)
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
        # Initializes the ride object
        self.username = username
        self.email = email
        self.password =password
       

    @staticmethod
    def post_user(user):
        cur = c.cursor(cursor_factory=RealDictCursor)
        SQL = ''' INSERT INTO users (username, email, password) 
                    VALUES(%s, %s, %s)'''
        cur.execute(SQL, (user.username, user.email, user.password))


'''class UserModel(c.Model):
    __tablename__ = 'users'

    id = c.Column(c.Integer, primary_key = True)
    username = c.Column(c.String(120), unique = True, nullable = False)
    password = c.Column(c.String(120), nullable = False)
    
    def save_to_c(self):
        c.session.add(self)
        c.session.commit()
    
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
    
    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }
        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)'''


    


'''define json response header'''
    
def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
