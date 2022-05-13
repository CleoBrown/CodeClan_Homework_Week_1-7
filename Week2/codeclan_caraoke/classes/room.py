class Room:
    def __init__(self, number, capacity, entry_fee):
        self.number = number
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.room_guests = []
        self.songs = []
        self.guest_count = len(self.room_guests)

    def check_in_guest(self, guest):
        self.room_guests.append(guest)
        self.guest_count += 1

    def check_out_guest(self, guest):
        self.room_guests.remove(guest)
        self.guest_count += 1

    def add_song_to_room(self, song):
        self.songs.append(song)

    def check_room_capacity(
        self,
    ):
        pass

    def guest_can_afford_fee(self, fee, wallet):
        if fee.entry_fee <= wallet.wallet:
            return True
