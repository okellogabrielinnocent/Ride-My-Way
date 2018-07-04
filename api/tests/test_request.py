from api.utilities import Database
from test_base import rides_test
import unittest
from flask import json, Response


""" Defines tests for the methods of for rides """     
class TestRide(rides_test):
    def setUp(self):
            pass
            

def test_request_to_join_ride(self):
    
    results = json.loads(response.data.decode())


    for ride in results:
        
        response = self.client.post('/rides/<ride_id>/requests'.format(ride['ride_id']),
                                    content_type='application/json',
                                    data=json.dumps({'status':True}))
        self.assertEqual(response.status_code, 201)
        self.assertIn("A request has been sent", str(response.data))

if __name__ == '__main__':
    unittest.main()