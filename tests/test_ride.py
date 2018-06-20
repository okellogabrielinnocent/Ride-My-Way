
import unittest, jsonify
import get_ride_by_id
from get_ride_by_id import rideDB
import pytest
#class TestClass(object):

class TestRide(unittest.TestCase):
    
    #== setup and tiedown method to avoid repeatition
    # setUp runs every singl test
    #run after every single test
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
        
    
    def test_get_All_ride(self):
        assert '/app/v1/rides',methods=['GET'] == jsonify({'rides':rideDB})
        self.assertEqual(get_ride_by_id.get_All_ride(-8,8),8)
        self.assertEqual(get_ride_by_id.get_All_ride(-8,8),0)

    def test_divide(self):
        self.assertEqual(get_ride_by_id.divide(10,2),5)
        self.assertRaises(ValueError,get_ride_by_id.divide(10,0))

# test by context manager  
        with self.assertRaises(ValueError):
            get_ride_by_id.divide(10,2)
           
# To run test directly
       
if __name__=='__main__':
    unittest.main()