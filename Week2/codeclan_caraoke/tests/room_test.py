import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room(6, 10, 5)
        self.guest = Guest("Flurry", "Baby One More Time", 200)
        self.song = Song("Oops I did it again", "Britney Spears")

    # Check in guest to room
    def test_check_in_guest_to_room(self):
        self.room1.check_in_guest(self.guest)
        self.assertEqual([self.guest], self.room1.room_guests)

    # Check out guests from room
    def test_check_out_guest_from_room(self):
        self.room1.check_in_guest(self.guest)
        self.room1.check_out_guest(self.guest)
        self.assertEqual([], self.room1.room_guests)

    # Add songs to rooms
    def test_add_song_to_room(self):
        self.room1.add_song_to_room(self.song)
        self.assertEqual([self.song], self.room1.songs)

    # Extention

    # Check room capacity

    # Check guests can afford entry fee
    def guest_can_afford_fee(self):
        amount = self.room1.guest_can_afford_fee(self.entry_fee, self.wallet)
        self.assertEqual(True, amount)
