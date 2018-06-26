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
        'status':'accepted'
        },
        {
        'id':'2',
        'd_name':'Okello',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':'accepted'
        },
        {
        'id':'3',
        'd_name':'Innocent',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':'accepted'
        },
        {
        'id':'4',
        'd_name':'Susan',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':'accepted'
        },
        {
        'id':'5',
        'd_name':'Abram',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':'accepted'
        },
        {
        'id':'6',
        'd_name':'Eunice',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':'accepted'
        },
 ]

 #==Fetch all ride offers==
@app.route('/app/v1/rides',methods=['GET'])
def getAllride():
    return jsonify({'rides':rideDB}), 200

@app.route('/app/v1/rides/<ride_id>',methods=['GET'])
def getride(ride_id):
    usr = [ ride for ride in rideDB if (ride['id'] == ride_id) ]
    
    return jsonify({'ride':usr}),200


@app.route('/app/v1/rides',methods=['POST'])
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
        'status':True
        }
    rideDB.append(ride)
    return jsonify({'ride': ride}), 201
        
@app.route('/app/v1/rides/<ride_Id>',methods=['PUT'])
def updateride(ride_Id):
    
    rid = [ ri for ri in rideDB if (ri['id'] == ride_Id) ]
    if 'id' in request.json : 
        rid[0]['id'] = request.json['id']
    if 'd_name' in request.json : 
        rid[0]['d_name'] = request.json['d_name']
    if 'departure_time' in request.json:
        rid[0]['departure_time'] = request.json['departure_time']
    if 'origin' in request.json : 
        rid[0]['origin'] = request.json['origin']
    if 'destination' in request.json : 
        rid[0]['destination'] = request.json['destination']
    if 'status' in request.json : 
        rid[0]['status'] = request.json['status']
    if 'cost' in request.json : 
        rid[0]['cost'] = request.json['cost']
    
        
        rides.append(ride)
        return jsonify({'ride':rid[0]}), 201

@app.route('/app/v1/rides/<ride_Id>',methods=['DELETE'])
def deleteride(ride_Id):
    ri = [ ride for ride in rideDB if (ride['id'] == ride_Id) ]
    if len(ri) == 0:
        return ri, 200
    rideDB.remove(ri[0])
    return jsonify({'response':'Success'})
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
if __name__ == '__main__':
    app.run()