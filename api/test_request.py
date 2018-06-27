
from test_base import rides_test
import unittest
from flask import json
from rides import rideDB
from rides import app

""" Defines tests for the view methods of for rides """     
class TestRide(rides_test):
    
    

    def setUp(self):
            pass
            

def test_request_to_join_ride(self):
    response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(rides))

    self.assertEqual(response.status_code, 201)
    response = self.client.get('api/v1/rides/')
    self.assertEqual(response.status_code, 200)
    
    results = json.loads(response.data.decode())


    for ride in results:
        
        response = self.client.post('/api/v1/rides/<ride_id>/requests'.format(ride['Id']),
                                    content_type='application/json',
                                    data=json.dumps({'status':True}))
        self.assertEqual(response.status_code, 201)
        self.assertIn("A request to join this ride has been sent", str(response.data))

if __name__ == '__main__':
        unittest.main()