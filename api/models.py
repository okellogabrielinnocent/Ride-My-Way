from flask import make_response

rides = [{
        'ride_id':'1',
        'd_name':'Gabriel',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"False"
        },
        {
        'ride_id':'2',
        'd_name':'Okello',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':3,
        'd_name':'Innocent',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':'4',
        'd_name':'Susan',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':'5',
        'd_name':'Abram',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        },
        {
        'ride_id':'6',
        'd_name':'Eunice',
        'departure_time':'12:15 am',
        'origin':'Kisaasi',
        'destination':'Andela',
        "cost":"200Shs", 
        'status':"True"
        }]


JSON_MIME_TYPE = 'application/json'

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

#get ride by id
    @classmethod
    def get_ride(cls, ride_id):
        for ride in rides:
            if ride['ride_id'] == ride_id:
                return ride
                
    # check existing ride object
    @classmethod
    def existing_ride(cls, origin, destination, date):
        for ride in rides:
            if ride['origin'] == origin and ride['destination'] == destination and ride['date'] == date:
                return True
        else:
            return False
    #post ride method
    @classmethod
    def post_ride(cls, origin,d_name, destination, date):
        
        cls.data = {}
        if cls.existing_ride(origin, destination, date):
            return "ride already exists"
        else:          
            cls.data['id'] = id
            cls.data['origin'] = origin
            cls.data['d_name'] = d_name
            cls.data['destination'] = destination
            cls.data["date"] = date
            cls.data["status"] = "False"

            rides.append(cls.data)
            return "Ride offered"

    @classmethod
    def join_ride(cls, ride_id):
        for ride in rides:
            if ride['id'] == ride_id:
                ride['status'] == "True"
                rides.append(ride)
                return "A request to join this ride has been sent"

    # define json response header
    @classmethod
    def json_response(data='', status=200, headers=None):
        headers = headers or {}
        if 'Content-Type' not in headers:
            headers['Content-Type'] = JSON_MIME_TYPE

        return make_response(data, status, headers)
