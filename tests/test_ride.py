from flask import jsonify
from flask import Flask, request, Response, json
import unittest

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

def setUp(self):
        pass
app = Flask(__name__)
@app.route('/tests/rides',methods=['GET']) #endpoit fo all rides
def test_get_all_ride(self): 
        response = response = self.app.get(jsonify({"rides":rideDB}))
        
        self.assertEqual(response.status_code, 201)
        

        response = self.app.post('/tests/rides/',
                                    content_type='application/json',
                                    data=json.dumps(rideDB))
        self.assertEqual(response.json(),{
                                        'id':'101',
                                        'name':'Saravanan S',
                                        'title':'Technical Leader'
                                        } )

        response = self.app.get('/tests/rides/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", str(response.data))

if __name__ == '__main__':
    unittest.main()