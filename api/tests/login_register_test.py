import os
import unittest
from flask import Flask,Response

from .models import c


def test_registration(self):
    response = self.register('gabriel@gmail.com', 'okello', 'okello')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Thanks for registering!', response.data)

def test_diplucate_mail(self):
    
    response = self.register('gabriel@gmail.com', 'okello', 'innocent')
    self.assertEqual(response.status_code, 500)
    self.assertIn(b'Message :User with same email exists!', response.data)
