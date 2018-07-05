import unittest
import psycopg2
import os
import unittest
from flask import Flask,Response, json
from api.utilities import Database
from .test_base import rides_test
from api.models import JSON_MIME_TYPE, Ride,User



'''Defines tests for the view methods of for rides'''


class TestRide(rides_test):

    def setUp(self):
            pass
     
    def test_get_all_rides(self):
            
            response = self.client.get("/rides", content_type='application/json', data=json.dumps(rides))

            self.assertEqual(response.status_code, 200)

    def test_get_ride(self):
            response = self.client.get("/rides/<ride_id>")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')


    def test_create_ride(self):
            response = self.client.create_ride('/user/rides', data = request.get_json(ride), content_type='application/json',
                                        follow_redirects=True)
            self.assertEqual(response.status_code, 201)
            response = self.create_ride('gabriel@gmail.com', 'okello', 'innocent')
            self.assertIn(b'Ride Created', response.data)

    def test_index(self):
            client = app.test_client(self)
            response = client.get('/index', content_type='application/json')
            self.assertEqual(response.status_code, 404)

    def test_login(self):
            client = app.test_client(self)
            response = client.get('/login', content_type='application/json')
            self.assertEqual(response.status_code, 404)


    def test_registor(self):
        """ Test for user registration """
        response = self.client.post(
            '/auth/signup',
            data=json.dumps(dict(
                email='joe@gmail.com',
                password='123456'
            )),
            content_type='application/json'
        )
        data = json.loads(response.data.decode())
        self.assertFalse(data['result'] == 'success')
        self.assertTrue(data['result'] == 'User Created')
        self.assertTrue(data['auth_token'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            '/auth/signup',
            data=json.dumps(dict(
                email='joe@gmail.com',
                password='123456'
            )),
        content_type='application/json'
        )
        data = json.loads(response.data.decode())
        self.assertFalse(data['result'] == 'success')
        self.assertTrue(data['result'] == 'Message :User with same email exists!')
        self.assertTrue(data['auth_token'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 500)


    
def test_request_to_join_ride(self):
    
    results = json.loads(response.data.decode())


    for ride in results:
        
        response = self.client.post('/rides/<ride_id>/requests'.format(ride['ride_id']),
                                    content_type='application/json',
                                    data=json.dumps({'status':True}))
        self.assertEqual(response.status_code, 201)
        self.assertIn("A request has been sent", str(response.data))


    def test_empty_query(self):
        cur = conn.cursor()
        self.assertRaises(psycopg2.ProgrammingError, cur.execute, "")
        self.assertRaises(psycopg2.ProgrammingError, cur.execute, " ")
        self.assertRaises(psycopg2.ProgrammingError, cur.execute, ";")


if __name__ == '__main__':
        unittest.main()
