from models.booking import Booking

class Hotel:
    def __init__(self):
        self.rooms = []
        self.bookings = []

    #add room
    def add_room(self,room):
        self.rooms.append(room)

    #show available room
    def show_available_room(self):
        for room in self.rooms:
            if not room.is_booked:
                print(f"Room {room.room_number} - {room.price()}")

    # book rooms 
    def book_room(self, room_number, customer, days):
        for room in self.rooms:
            if room.room_number == room_number and not room.is_booked:
                room.is_booked = True
                booking = Booking(customer, room, days)
                self.bookings.append(booking)
                return booking
            return None
    
    #checkout
    def checkout(self,room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.is_booked=False
                return True
        return False
