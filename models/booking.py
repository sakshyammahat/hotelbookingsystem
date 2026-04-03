class Booking:
    def __init__(self,customer,room,days):
        self.customer=customer
        self.room=room
        self.days=days

    def total_price(self):
        return self.room.price() * self.days