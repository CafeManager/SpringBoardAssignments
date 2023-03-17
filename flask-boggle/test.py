from app import app, check_if_in_words
from boggle import Boggle
from flask import session
from unittest import TestCase
import json

app.config["DEBUG_TB_HOSTS"] = ['dont-show-debug-toolbar']

testBoard = [['S', 'G', 'K', 'B', 'I'], 
                ['R', 'C', 'G', 'Q', 'W'], 
                ['Y', 'G', 'V', 'H', 'A'], 
                ['Y', 'K', 'J', 'M', 'Z'], 
                ['J', 'G', 'O', 'G', 'D']]

boggle = Boggle()


  # This is not testable because the code in app needs to be refactored to be made more modular.
    # This requires either a personal instance of the app to be created which can be a hacky solution
    # Or the code can be refactored to enact a separation of concerns. The assignment tells us
    
class FlaskTests(TestCase):
   
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    # makes sure "/" navigates to the boggle page
    def test_home_page(self):
        with self.client as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1> Welcome to Boggle! </h1>', html)

    # initialize_board is called whenever the client navigates to "/"
    def test_initialize_board(self):
        with self.client as client:
            res = client.get('/')
            self.assertEqual(len(session["board"]), 5)
            self.assertEqual(len(session["board"][0]), 5)
            
    # initialize_board is called whenever the client navigates to "/"
    def test_check_if_in_words(self):
        with self.client as client:        
            res = client.get('/')
            session["board"] = testBoard
            self.assertEqual(check_if_in_words("jog").strip(), "ok")


  