class Guest:
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    # Remove entry fee from guest wallet

    def decrease_guest_wallet(self, fee):
        self.wallet -= fee.entry_fee
