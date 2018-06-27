from test_base import rides_test
import unittest
from flask import json
from rides import rideDB
from rides import app

""" Defines tests for the view methods of for rides """     
class TestRide(rides_test):
    
    

    def setUp(self):
            pass
            
    def test_getAllride(self):
            response = self.client.get('/api/v1/rides')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

            content = json.loads(response.get_data(as_text=True))
            self.assertEqual(len(content), 1)
            
            self.assertEqual(content, {
            'id':'1',
            'd_name':'Gabriel',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':True
            })

    def test_getride(self):
            response = self.client.get('/api/v1/rides/<ride_id>'.format(self.id))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

            content = json.loads(response.get_data(as_text=True))
            self.assertEqual(len(content), 1)
            self.assertEqual(content, {
            'id':'1',
            'd_name':'Gabriel',
            'departure_time':'12:15 am',
            'origin':'Kisaasi',
            'destination':'Andela',
            "cost":"200Shs", 
            'status':True
            })
            

    def test_create_ride(self):
            
            ride = {
                    
                    "id":10,
                    "d_name":"Susan",
                    "departure_time":"12:15 am",
                    "origin":"Kisaasi",
                    "destination":"Andela",
                    "cost":"200Shs", 
                    
                    }
            
            

            response = self.client.post('/api/v1/rides',
                            data=json.dumps(ride),
                            content_type='application/json',
                            follow_redirects=True)
            self.assertEqual(response.status_code, 201)
            json_response = json.loads(response.get_data(as_text=True))

    def test_index(self):
            client = app.test_client(self)
            response = client.get('/index', content_type='application/json')
            self.assertEqual(response.status_code, 404)

    def test_login(self):
            client = app.test_client(self)
            response = client.get('/login', content_type='application/json')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
        unittest.main()