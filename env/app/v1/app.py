from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

rides = [
    {
        "name": "Gabriel",
        "departure_time": "12:30am",
        "origin": "Kisaasi",
        "destination":"Kampala City",
        "cost":"2000"
    },
    {
        "name": "Innocent",
        "departure_time": "10:42pm",
        "origin": "Bukoto",
        "destination":"Kampala City",
        "cost":"2000"
    },
    {
        "name": "Okello",
        "departure_time": "11:30am",
        "origin": "Kisaasi",
        "destination":"Kampala City",
        "cost":"2000"
    },
]

class Ride(Resource):
    
    def get(self, name):
        for ride in rides:
            if(name == ride["name"]):
                return ride, 200                #Success or OK
        return "ride not found", 404            #page not fund

    def post(self, name):
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

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("origin")
        parser.add_argument("destination")
        parser.add_argument("cost")
        parser.add_argument("departure_time")
        args = parser.parse_args()

        for ride in rides:
            if(name == ride["name"]):
                ride["origin"] = args["origin"]
                ride["destination"] = args["destination"]
                return ride, 200
        
        ride = {
            "name": name,
            "origin": args["origin"],
            "destination": args["destination"],
            "cost":args["cost"],
            "departure_time":args["departure_time"],
        }
        rides.append(ride)
        return ride, 201

    def delete(self, name):
        global rides
        rides = [ride for ride in rides if ride["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(Ride, "/app/v1/ride/<string:name>")


app.run(debug=True)