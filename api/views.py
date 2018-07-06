from flask import Flask, Response, abort, request, json, jsonify, make_response
from werkzeug.security import safe_str_cmp
import jwt
from functools import wraps
from .models import JSON_MIME_TYPE, Ride,User
from .models import c
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'topsecretenocrack'
jwt = JWTManager(app)


'''Method to view all rides'''
@classmethod 
@app.route('/rides', methods=["GET"])
@jwt_required
def get_all_rides():
    user_identity = get_jwt_identity()   
    cur = c.cursor()
    response = ''
    query = 'SELECT * FROM rides'
    if cur is not None:
        cur.execute(query)
        c.commit()
        rows = cur.fetchall()
        response = json.dumps(rows)
    return jsonify(response), 200


'''Method to view ride by id'''
@classmethod 
@app.route('/rides/<ride_id>', methods=["GET"])
@jwt_required
def get_ride(ride_id):
    user_identity = get_jwt_identity()
    cur = c.cursor()
    response = ''
    query = ("SELECT * FROM rides WHERE ride_id ='{}'".format(ride_id))
    if cur is not None:
        cur.execute(query)
        c.commit()
        rows = cur.fetchone()
        response = json.dumps(rows)
        return response, 200
    else:
        result ="Ride Not Found"
        return jsonify({"Message":result}),404


'''Method for user to post ride or create ride'''
@classmethod #converts ftn to class method
@app.route('/users/rides',methods=['POST'])
@jwt_required
def create_ride():
    user_identity = get_jwt_identity()
    data = request.get_json()
    ride = Ride(data['ride_id'], data['d_name'], data['origin'], data['departure_time'],  data['destination'],  
                data['cost'], data['ride_status'])
    response = Ride.post_ride(ride)
    result ="Ride Created"
    return jsonify({"Message":result}),201


'''Method to to sign up User'''
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


'''Methode to login user'''
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.get_login(data["username"],data["password"])
    
    if not user:
        return make_response("Couldn't verify now", 404, {"WWW-Authenticate": 'Basic realm-'"Login required"})

# Create  JWTs
    access_token = create_access_token(identity="username")
    resp = {
        'access_token': access_token
    }
    return jsonify(resp), 201


'''Methods to handle errors'''   
@app.errorhandler(404)
def not_found(e):
    return 'Not Found', 404

@app.errorhandler(400)
def ride_duplicate(e):
    return 'Same Ride Exists', 400


@app.errorhandler(401)
def Unauthorized(e):
    return 'Unauthorized', 401
