from test_base import rides_test
import unittest
from flask import json
from rides import rideDB
from rides import app

#Defines tests for the view methods of for rides"""     
class TestRide(rides_test):   
    
    def setUp(self):
            pass
     
    def test_getAllride(self):
            
            response = self.client.get('api/v1/rides',
                                      content_type='application/json',
                                      data=json.dumps(rideDB))

            self.assertEqual(response.status_code, 200)
            

    def test_getride(self):
            response = self.client.get('/api/v1/rides/<ride_id>'.format(self.id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

            response = json.loads(response.get_data(as_text=True))
            self.assertEqual(len(response), 1)
            self.assertEqual(response, {
            "ride":[],
            })
            

    def test_create_ride(self):
            
            ride = {
                    
                    "id":10,
                    "d_name":"Susan",
                    "departure_time":"12:15 am",
                    "origin":"Kisaasi",
                    "destination":"Andela",
                    "cost":"200Shs",
                    "status":"True"
                    
                    }
            response = self.client.post('/api/v1/rides',
                            data=json.dumps(ride),
                            content_type='application/json',
                            follow_redirects=True)
            self.assertEqual(response.status_code, 201)
            json_response = json.loads(response.get_data(as_text=True))

    def test_index(self):
            client = app.test_client(self)
            response = client.get('/index',
                                 content_type='application/json'
                                 )
            self.assertEqual(response.status_code, 404)

    def test_login(self):
            client = app.test_client(self)
            response = client.get('/login', 
                                content_type='application/json'
                                )
            self.assertEqual(response.status_code, 404)

    def test_request_to_join_ride(self):
        rideDB = json.loads(response.data.decode())
        for ride in rideDB:
            response = self.client.post('/api/v1/rides/<ride_id>/requests'.format(self.ride['id']),
                                    content_type='application/json',
                                    data=json.dumps({'status':True}))
            self.assertEqual(response.status_code, 201)
            self.assertIn("A request has been sent", str(response.data))

        


if __name__ == '__main__':
        unittest.main()