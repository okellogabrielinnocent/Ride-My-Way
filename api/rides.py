from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

    rideDB=[
            {
            'id':'1',
            'd_name':'Gabriel',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':"False"
            },
            {
            'id':'2',
            'd_name':'Okello',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':"True"
            },
            {
            'id':3,
            'd_name':'Innocent',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':"True"
            },
            {
            'id':'4',
            'd_name':'Susan',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':"True"
            },
            {
            'id':'5',
            'd_name':'Abram',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':"True"
            },
            {
            'id':'6',
            'd_name':'Eunice',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':"True"
            },
    ]
    class Ride(object):
    #==Fetch all ride offers==
        
    #==Fetch all ride offers==
    @app.route('/api/v1/rides',methods=['GET'])
    def getAllride():
        return jsonify({'rides':rideDB}), 200
    #==Fetch ride by id ==
    @app.route('/api/v1/rides/<ride_id>',methods=['GET'])
    def getride(ride_id):
        request = [ ride for ride in rideDB if (ride['id'] == ride_id) ] 
        return jsonify({'ride':request}),200

    #==Create ride offers==
    @app.route('/api/v1/rides',methods=['POST'])
    def create_ride():
        if not request.json or not 'd_name' in request.json:
            400
        ride = {
            'id':request.json['id'],
            'd_name':request.json['d_name'],
            'departure_time':request.json['departure_time'],
            'origin':request.json['origin'],
            'destination':request.json['destination'],
            'cost':request.json['cost'],
            'status':"True"
            }
        rideDB.append(ride)
        return jsonify({'ride': ride}), 201

#==request to join ride offers==
    @app.route('/api/v1/rides/<ride_id>/requests', methods=['POST',])
    def request_to_join_ride(ride_id):
        for ride in rides:
            if ride['id']:
                ride['status'] == True
                rideDB.append(ride)
                return "A request has been sent" 

#==customesid error report==
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
 app.run()