def save_booking(booking):
    with open("data/bookings.txt","a") as file:
        file.write(
            f"{booking.customer.name}, {booking.customer.phone},{booking.room.room_number},{booking.days},{booking.total_price()}\n"
                   )
