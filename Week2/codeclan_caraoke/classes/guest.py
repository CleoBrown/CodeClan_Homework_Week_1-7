from classes.room import Room


class Guest:
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    # Remove entry fee from guest wallet

    def decrease_wallet(self, room):
        if room.guest_can_afford_fee(self):
            self.wallet -= room.entry_fee
