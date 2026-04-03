class Room:

    def __init__(self,room_number):
        self.room_number=room_number
        self.is_booked = False


class StandardRoom(Room):
    def price(self):
        return 1000
    
class DeluxeRoom(Room):
    def price(self):
        return 1000

class highRoom(Room):
    def price(self):
        return 3000
    