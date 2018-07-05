from flask import Flask, Response, abort, request, json, jsonify, make_response
from flask_jwt import  jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import jwt
from functools import wraps
from .models import JSON_MIME_TYPE, Ride,User,Ride_request
from .models import c

from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY'])
            currentuser = User.post_user(public_id=data['username'])
        except:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(currentuser, *args, **kwargs)

    return decorated



@classmethod 
@app.route('/rides', methods=["GET"])
def get_all_rides():    
    cur = c.cursor()
    response = ''
    query = 'SELECT * FROM rides'
    if cur is not None:
        cur.execute(query)
        c.commit()
        rows = cur.fetchall()
        response = json.dumps(rows)
    return response, 200

@jwt_required()
@classmethod 
@app.route('/rides/<ride_id>', methods=["GET"])
def get_ride(ride_id):
    cur = c.cursor()
    response = ''
    query = ("SELECT * FROM rides WHERE ride_id ='{}'".format(ride_id))
    if cur is not None:
        cur.execute(query)
        c.commit()
        rows = cur.fetchone()
        response = json.dumps(rows)
    return response, 200

@jwt_required()
@classmethod #converts ftn to class method
@app.route('/users/rides',methods=['POST'])
def create_ride():
    data = request.get_json()
    ride = Ride(data['ride_id'], data['d_name'], data['origin'], data['departure_time'],  data['destination'],  
                data['cost'], data['ride_status'])
    response = Ride.post_ride(ride)
    result ="Ride Created"
    return jsonify({"Message":result}),201



@app.route('/auth/signup', methods=['POST'])
def register():
    try:
        data = request.get_json()
        user = User(data['username'], data['email'], data['password'])
        results = User.post_user(user)
        result = "User Created"
        return jsonify({"Message":result}),201
    except:
        return jsonify("Message :User with same email exists!"),500

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.get_login(data["username"],data["password"])
    
    if not user:
        return make_response("Couldn't verify now", 404, {"WWW-Authenticate": 'Basic realm-'"Login required"})

    if data["username"] and data["password"]:
        token = jwt.encode({"exp":datetime.datetime.utcnow() + datetime.timedelta(minutes =30)}, app.config["SECRET_KEY"])
        return jsonify({"token": token.decode("UTF-8")})

    return make_response("Couldn't verify", 404, {"WWW-Authenticate": 'Basic realm-'"Login required"})


'''functions for ride requests'''
@jwt_required()
@app.route('/users/rides/<rideId>/requests', methods=['GET'])
def rides_requests():
    
    """A route to handle Requests"""
    data = request.get_json()
    
    ride_request = Ride_request(data['ride_id'], data['user_id'], data['request_status'])
    response = Ride_request.fetch_all_requests(ride_request)
    result ="Avialble ride riquest"
    return jsonify({"Message":result}),201


@app.route('/Request/<request_id>', methods=['GET'])
def fetch_one_request(request_id):
    """A route to handle request updates"""
    request_id = uuid.UUID(request_id)
    request_object = request_instance.fetch_request_by_id(request_id)
    return jsonify(request_object), 200


@app.route('/Request/<request_id>', methods=['PUT'])
def modify_request(request_id):
    """A route to handle requests modification"""
    
    request_data = request.get_json()
    user_id = request_data['user_id']
    ride_id = request_data['ride_id']
    ride_status = request_data['ride_status']
    result = modify_request(
        request_id, user_id, ride_id, ride_status)
    if result == "update success":
        return jsonify(response=result), 200
    elif result == "no request with given id":
        return jsonify(response=result), 404
    else:
        return jsonify(response=result), 409
 

@app.errorhandler(404)
def not_found(e):
    return 'Ride Not Found', 404

@app.errorhandler(400)
def ride_duplicate(e):
    return 'Same Ride Exists', 400
