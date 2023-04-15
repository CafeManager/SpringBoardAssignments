from app import app, validateValues
from flask import session
from unittest import TestCase
import json

app.config["DEBUG_TB_HOSTS"] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home_page(self):
        with self.client as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertIn("<h1> Welcome to the currency converter! </h1>", html)
    
    def test_form_submit(self):
        with self.client as client:
            res = client.post('form-submit', follow_redirects=True, data={'startingCurrency':'usd', 'endCurrency':'eur', 'amount':10})
            html = res.get_data(as_text=True)
            self.assertIn('<p id="result"> The result is €', html)

    def test_validate_values(self):
        errorList = validateValues("hi", "me", "12a")
        self.assertEqual(len(errorList), 3)
        self.assertEqual('Invalid currency: hi', errorList[0]) 
        self.assertEqual('Invalid currency: me', errorList[1]) 
        self.assertEqual('Invalid value for: Amount input', errorList[2]) 