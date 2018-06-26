from flask import Flask, jsonify, request, make_response
import unittest
from get_ride_by_id import app
from get_ride_by_id import rideDB

        
class ride_my_way_test(unittest.TestCase):
        
        app.app_context().push()
        client = app.test_client()
        
        def setUp(self):
                pass
        
        def test_get_all_ride(self):
                
                #response = response = self.client.get(jsonify({"rides":rideDB}))                
                #self.assertEqual(response.status_code, 201)
                response = self.client.get('/app/v1/rides',
                                        content_type='application/json',
                                        data= jsonify({'rides':rideDB})
                                        )
                self.assertEqual(response.status_code, 201)
                response = self.client.get('/app/v1/rides')
                self.assertEqual(response.status_code, 200)
                self.assertIn("cost", str(response.data))
                
if __name__ == '__main__':
        unittest.main()