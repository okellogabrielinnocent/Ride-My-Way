from flask import Flask, jsonify, request, make_response, json
import unittest
from rides import rideDB
from rides import app
        
class rides_test(unittest.TestCase):
        
        app.app_context().push()
        client = app.test_client()
        
        def setUp(self):
                pass
        
              
        def test_getAllride(self):
                response = jsonify({'rides':rideDB})
                self.assertEqual(response.status_code, 200)

        def test_getride(self):
                for ride in rideDB:
                        response = self.client.get('/app/v1/rides/<ride_id>'.format(ride['id']))
                        self.assertEqual(response.status_code, 201)

                

        def test_create_ride(self):
                
                ride = {
                        
                        "id":10,
                        "d_name":"Susan",
                        "departure_time":"12:15 am",
                        "origin":"Kisaasi",
                        "destination":"Andela",
                        "cost":"200Shs", 
                        "status":"accepted"
                        }
                
                

                response = self.client.post('/app/v1/rides',
                              data=json.dumps(ride),
                              content_type='application/json',
                              follow_redirects=True)
                self.assertEqual(response.status_code, 201)
                json_response = json.loads(response.get_data(as_text=True))

        def test_index(self):
                client = app.test_client(self)
                response = client.get('/index', content_type = 'html/text')
                self.assertEqual(response.status_code, 404)

        def test_login(self):
                client = app.test_client(self)
                response = client.get('/login', content_type = 'html/text')
                self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
        unittest.main()