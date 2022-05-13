import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Buffy", "Old Time Rock and Roll", 100)
        self.guest1 = Guest("Willow", "Tumbling Dice", 2)
        self.room1 = Room(6, 10, 5)

    # Remove entry fee from guest wallet

    def test_decrease_guest_wallet__can_afford(self):
        self.guest.decrease_wallet(self.room1)
        self.assertEqual(95, self.guest.wallet)

    def test_decrease_guest_wallet__cant_afford(self):
        self.guest1.decrease_wallet(self.room1)
        self.assertEqual(2, self.guest1.wallet)
