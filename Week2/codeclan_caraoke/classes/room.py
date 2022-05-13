class Room:
    def __init__(self, number, capacity, entry_fee):
        self.number = number
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.room_guests = []
        self.songs = []
        self.guest_count = len(self.room_guests)

        def has_capacity(self):
            return self.capacity > self.guest_count

    def check_in_guest(self, guest):
        if self.has_capacity():
            self.room_guests.append(guest)
            self.guest_count += 1

    def check_out_guest(self, guest):
        self.room_guests.remove(guest)
        self.guest_count += 1

    def add_song_to_room(self, song):
        self.songs.append(song)

    def guest_can_afford_fee(self, guest):
        return self.entry_fee <= guest.wallet
