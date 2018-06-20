from flask import Flask, jsonify, request

app = Flask(__name__)

rideDB=[
        {
        'id':'101',
        'name':'Saravanan S',
        'title':'Technical Leader'
        },
        {
        'id':'201',
        'name':'Rajkumar P',
        'title':'Sr Software Engineer'
        }
 ]

 #==Fetch all ride offers==
@app.route('/app/v1/rides', methods=['GET'])
def get_All_ride():
    return jsonify({'rides':rideDB})

@app.route('/app/v1/rides/<ride_id>',methods=['GET'])
def get_ride(ride_id):
    usr = [ ride for ride in rideDB if (ride['id'] == ride_id) ] 
    return jsonify({'ride':usr})

@app.route('/app/v1/rides/<ride_id>/requests',methods=['GET'])
def request_ride(tittle):
    rqts = [ ride for ride in rideDB if (ride['id'] == tittle) ] 
    return jsonify({'ride':rqts})
    
@app.route('/app/v1/rides/<ride_Id>',methods=['PUT'])
def updateride(ride_Id):
    rid = [ ride for ride in rideDB if (ride['id'] == ride_Id) ]
    if 'name' in request.json : 
        rid[0]['name'] = request.json['name']
    if 'title' in request.json:
        rid[0]['title'] = request.json['title']
    return jsonify({'ride':rid[0]})
    
@app.route('/app/v1/rides',methods=['POST'])
def createride():
    dat = {
    'id':request.json['id'],
    'name':request.json['name'],
    'title':request.json['title']
    }
    rideDB.append(dat)
    return jsonify(dat)
@app.route('/app/v1/rides/<ride_Id>',methods=['DELETE'])
def deleteride(ride_Id):
    em = [ ride for ride in rideDB if (ride['id'] == ride_Id) ]
    if len(em) == 0:
        return em, 200 #Success or OK
    rideDB.remove(em[0])
    return jsonify({'response':'Success'})
if __name__ == '__main__':
 app.run()
