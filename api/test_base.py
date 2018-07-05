""" Tests module """
import unittest
from flask import json

# from app import create_app,
from app.views import app

class rides_test(unittest.TestCase):
        
        app.app_context().push()
        client = app.test_client()
        