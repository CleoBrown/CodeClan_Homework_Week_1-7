import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Old Time Rock and Roll", "Bob Seger")
