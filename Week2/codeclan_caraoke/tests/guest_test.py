import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Buffy", "Old Time Rock and Roll", 100)
        self.room1 = Room(6, 10, 5)

    # Remove entry fee from guest wallet

    def test_decrease_guest_wallet(self):
        self.guest.decrease_guest_wallet(self.room1)
        self.assertEqual(95, self.guest.wallet)
