from unittest import TestCase
from app import app

app.config["DEBUG_TB_HOSTS"] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def SetUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
    def test_create(self):
        with self.client as client:
            res = client.post('/create')