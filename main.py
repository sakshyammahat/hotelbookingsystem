from models.room import StandardRoom, DeluxeRoom, highRoom
from models.customer import Customer
from services.hotel import Hotel
from utils.filehandler import save_booking
from models.booking import Booking


hotel=Hotel()

hotel.add_room(StandardRoom(101))
hotel.add_room(DeluxeRoom(102))
hotel.add_room(highRoom(103))

while True:
    print("\n1 = Show Room")
    print("2. Book Room")
    print("3.Checkout")
    print("4. Exit")

    choice = input("Enter choice: ")

    match choice:
        case "1":
            hotel.show_available_room()
        case "2":
            try:
                name = input("Enter name")
                phone = input("Enter phone")
                room_number = int(input("Enter room number:"))
                days = int(input("Enter days: "))
                customer = Customer(name, phone)
                booking = hotel.book_room(room_number, customer, days)
                if booking:
                    print("Booking successfully")
                    print("Total price:", booking.total_price())
                    print(f"{booking.customer.name}, {booking.customer.phone},")
                    save_booking(booking)
                else:
                    print("Room not available")
            except ValueError:
                print("Invalid input")
        case "3":
            room_number = int(input("Enter room number:"))
            result = hotel.checkout(room_number)
            if result:
                print("Checkout Successfully")
            else:
                print("Room number invalid")
        case "4":
            break
        case _:
            print("invalid choice")