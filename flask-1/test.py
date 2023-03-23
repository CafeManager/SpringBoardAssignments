from app import app
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
    
    