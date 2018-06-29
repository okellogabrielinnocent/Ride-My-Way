from test_base import rides_test
import unittest
from flask import json,Response
from api.rides import rides
from api.rides import app

#Defines tests for the view methods of for rides"""     
class TestRide(rides_test):
        def setUp(self):
                pass
        #getting all rides 
        def test_getAllride(self):
                response = self.client.get('api/v1/rides/',
                                        content_type='application/json',
                                        data=json.dumps(rides))

                self.assertEqual(response.status_code, 201)
                self.assertEqual(response.status_code, 200)
                self.assertIn("d_name", str(response.data))
            

        def test_get_ride(self):
                response = self.client.get('api/v1/rides/<ride_id>',
                                        content_type='application/json',
                                        data=json.dumps(rides)
                                        )
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.content_type, 'application/json')

                response = json.loads(response.get_data(as_text=True))
                self.assertEqual(len(response), 1)
                self.assertEqual(response, {
                "ride":[],
                })
                

        def test_post_ride(self):        
        
        
                response = self.client.post('api/v1/rides/',
                                        content_type='application/json',
                                        data=json.dumps(rides))

                self.assertEqual(response.status_code, 201)
                self.assertIn('Ride offered', str(response.data))

        
        def test_all_rides(self):
                response = self.client.get('api/v1/rides/',
                                        content_type='application/json',
                                        data=json.dumps(rides))

                self.assertEqual(response.status_code, 201)
                self.assertEqual(response.status_code, 200)
                self.assertIn("destination", str(response.data))
    

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
                self.assertIn

if __name__ == '__main__':
        unittest.main()