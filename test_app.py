from unittest import TestCase

from app import app, games

import json

from random import choice

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

TEST_BOARD =[
 [ "F", "O", "O", "R", "T"],
 [ "D", "E", "A", "N", "T" ], 
 [ "E", "F", "E", "T", "V" ], 
 [ "B", "I", "O", "I", "N" ], 
 [ "A", "B", "R", "B", "R" ] 
]

class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code,200)
            self.assertIn('<title>Boggle</title>',html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.get('/api/new-game')
            data = response.get_json()

            self.assertIsInstance(data['board'],list)
            self.assertIsInstance(data['gameId'],str)
            self.assertEqual(len(games),1)
            self.assertEqual(response.status_code,200)

    def test_api_score_word(self):
        """ Test if score_word function returns correct JSON response """

        with self.client as client:
            game = client.get('/api/new-game')
            game_data = game.get_json()
            games[game_data['gameId']].board = TEST_BOARD
            
            words = ["ANT","ABRB","PONY"]
            word = choice(words)
            
            response = client.post('/api/score-word',
                                    json={'gameId': game_data['gameId'], 
                                          'word': word})
            json_data = response.get_json()
            
            if word == "ANT":
                self.assertIn("ok", json_data["result"])
            elif word == "ABRB":
                self.assertIn("not-word", json_data["result"])
            else:
                self.assertIn("not-on-board", json_data["result"])
 
             

