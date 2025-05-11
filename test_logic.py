from datetime import datetime

class Address:
    def __init__(self, address_id: int, street: str, city: str, zip_code: str):
        if not address_id:
            raise ValueError("address_id cannot be empty")
        if not isinstance(address_id, int):
            raise TypeError("address_id must be an integer")
        if not street:
            raise ValueError("street cannot be empty")
        if not isinstance(street, str):
            raise TypeError("street must be a string")
        if not city:
            raise ValueError("city cannot be empty")
        if not isinstance(city, str):
            raise TypeError("city must be a string")

        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    @property
    def city(self):
        return self.__city

    @property
    def zip_code(self):
        return self.__zip_code

    @property
    def street(self):
        return self.__street


class Room_Type:
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        if not room_type_id:
            raise ValueError("type_id cannot be empty")
        if not isinstance(room_type_id, int):
            raise TypeError("type_id must be an integer")
        if not description:
            raise ValueError("description cannot be empty")
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        if not max_guests:
            raise ValueError("max_guests cannot be empty")
        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be an integer")
        if max_guests < 0:
            raise ValueError("max_guests cannot be negative")  # in pycharm nicht drin

        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def max_guests(self):
        return self.__max_guests

    @property
    def description(self):
        return self.__description


class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address:Address):  # address in pycharm so nicht drin
        if not hotel_id:
            raise ValueError("hotel_id cannot be empty")
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id must be an integer")
        if not name:
            raise ValueError("name cannot be empty")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(address, Address):
            raise TypeError ("address must be an address")

        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = []
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def stars(self):
        return self.__stars

    @property
    def address(self):
        return self.__address  # in pycharm so nicht drin

    @property
    def rooms(self):
        return self.__rooms  # in pycharm so nicht drin

    def add_room(self, room_id: int, room_number: int, price_per_night: float, room_available: bool,
                 room_type: Room_Type):
        room = Room(room_id, room_number, price_per_night, room_available, room_type)
        self.__rooms.append(room)


class Room:
    def __init__(self, room_id: int, room_number: int, price_per_night: float, room_available: bool,
                 room_type: Room_Type):
        # bool fehlt in pycharm // room_type fehlt in pycharm
        if not room_id:
            raise ValueError("room_id cannot be empty")
        if not isinstance(room_id, int):
            raise TypeError("room_id must be an integer")
        if not room_number:
            raise ValueError("room_number cannot be empty")
        if not isinstance(room_number, int):
            raise TypeError("room_number must be an integer")
        if not price_per_night:
            raise ValueError("price cannot be empty")
        if not isinstance(price_per_night, float):
            raise TypeError("price must be a float")
        if price_per_night < 0:
            raise ValueError("price cannot be negative")

        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__room_available = room_available  # wie ändert sich dieser wert je nach buchungsdatum?
        self.__room_type = room_type  # association with Room_Type, fehlt in pycharm

    @property
    def room_type(self):
        return self.__room_type

    @property
    def price_per_night(self):
        return self.__price_per_night

    @property
    def room_number(self):
        return self.__room_number

    @property
    def room_id(self):
        return self.__room_id

    @property
    def room_available(self):
        return self.__room_available

    def is_available(self):
        for room in self.__hotel.rooms:
            if room.room_id == self.room_id and room.room_available == True:
                return True
        return False
    
class Booking:

    def __init__(
        self,
        booking_id: int,
        check_in_date: str,
        check_out_date: str,
        is_cancelled: bool,
        total_amount: float,
        guest_id: int,
        room_id: int
    ):
        if booking_id <= 0:
            raise ValueError("booking_id must be a positive integer")
        if not check_in_date:
            raise ValueError("check_in_date must not be empty")
        if not check_out_date:
            raise ValueError("check_out_date must not be empty")
        if total_amount < 0:
            raise ValueError("total_amount must be non-negative")
        if guest_id <= 0:
            raise ValueError("guest_id must be a positive integer")
        if room_id <= 0:
            raise ValueError("room_id must be a positive integer")
        if not isinstance(is_cancelled, bool):
            raise TypeError("is_cancelled must be a boolean")

        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
        self.__guest_id = guest_id
        self.__room_id = room_id
        self.__invoice = None
        self.__guest = None
        self.__room = None

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def check_in_date(self) -> str:
        return self.__check_in_date

    @property
    def check_out_date(self) -> str:
        return self.__check_out_date

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_cancelled must be a boolean")
        self.__is_cancelled = value

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        if value < 0:
            raise ValueError("total_amount must be non-negative")
        self.__total_amount = value

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def invoice(self):
        return self.__invoice

    def add_invoice(self, invoice: 'Invoice'):
        if not isinstance(invoice, Invoice):
            raise TypeError("invoice must be an instance of Invoice")
        self.__invoice = invoice
        invoice.add_booking(self)

    def add_guest(self, guest: 'Guest'):
        if not isinstance(guest, Guest):
            raise TypeError("guest must be an instance of Guest")
        self.__guest = guest

    def add_room(self, room: 'Room'):
        if not isinstance(room, Room):
            raise TypeError("room must be an instance of Room")
        self.__room = room

class Facilities:
    def __init__(
            self,
            facility_id: int,
            facility_name: str,
            ):
        if not facility_id:
            raise ValueError("Facility ID is required")
        if not isinstance(facility_id, int):
            raise TypeError("Facility ID must be an integer")
        if not facility_name:
            raise ValueError("Facility name is required")
        if not isinstance(facility_name, str):
            raise TypeError("Facility name must be a string")
            
        self.__facility_id: int = facility_id
        self.__facility_name: str = facility_name
    
    @property
    def facility_id(self) -> int:
        return self.__facility_id
        
    @property
    def facility_name(self) -> str:
        return self.__facility_name
    
    @facility_name.setter
    def facility_name(self, new_facility_name: str):
        if not new_facility_name:
            raise ValueError("Facility name required")
        if not isinstance(new_facility_name, str):
            raise TypeError("Facility name must be a string")
        self.__facility_name = new_facility_name

class Guest:
    def __init__(self, guest_id: int, first_name: str, last_name: str, email: str, address_id: int = None,):
        if not guest_id:
            raise ValueError("Guest ID is required")
        if not isinstance(guest_id, int):
            raise TypeError("Guest ID must be an integer")
        if not first_name:
            raise ValueError("First name is required")
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if not last_name:
            raise ValueError("Last name is required")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if not email:
            raise ValueError("Email is required")
        if not isinstance(email, str):
            raise TypeError("Email must be a string")
        if address_id is not None and not isinstance(address_id, int):
            raise TypeError("Address ID must be an integer")
            
        self.__guest_id: int = guest_id
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__email: str = email
        self.__address_id: int = address_id
    
    @property
    def guest_id(self) -> int:
        return self.__guest_id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @first_name.setter
    def first_name(self, new_first_name: str):
        if not new_first_name:
            raise ValueError("First name required")
        if not isinstance(new_first_name, str):
            raise TypeError("First name must be a string")
        self.__first_name = new_first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @last_name.setter
    def last_name(self, new_last_name: str):
        if not new_last_name:
            raise ValueError("Last name required")
        if not isinstance(new_last_name, str):
            raise TypeError("Last name must be a string")
        self.__last_name = new_last_name
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, new_email: str):
        if not new_email:
            raise ValueError("Email required")
        if not isinstance(new_email, str):
            raise TypeError("Email must be a string")
        self.__email = new_email
        
    @property
    def address_id(self) -> int:
        return self.__address_id
        
    @address_id.setter
    def address_id(self, new_address_id: int):
        if new_address_id is not None and not isinstance(new_address_id, int):
            raise TypeError("Address ID must be an integer")
        self.__address_id = new_address_id

class Invoice:

    def __init__(self, invoice_id: int, issue_date: str):
        if invoice_id <= 0:
            raise ValueError("invoice_id must be positive")
        if not issue_date:
            raise ValueError("issue_date must not be empty")

        self.__invoice_id = invoice_id
        self.__issue_date = issue_date
        self.__bookings = []

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @property
    def issue_date(self) -> str:
        return self.__issue_date

    @property
    def bookings(self) -> list:
        return self.__bookings

    def add_booking(self, booking):
        self.__bookings.append(booking)

    def get_total_amount(self) -> float:
        return sum(b.total_amount for b in self.__bookings)

# -----------------------------------

# Beispiel-Instanzen erstellen
invoice = Invoice(1001, "2025-04-08")

b1 = Booking(1, "2025-04-10", "2025-04-12", False, 300.0, 1, 101)
b2 = Booking(2, "2025-04-10", "2025-04-11", False, 100.0, 1, 102)

# Verknüpfen mit Rechnung
b1.assign_invoice(invoice)
b2.assign_invoice(invoice)

# Ausgabe prüfen
print(f"Rechnung Nr. {invoice.invoice_id} vom {invoice.issue_date}")
for booking in invoice.bookings:
    print(f"- Buchung ID {booking.booking_id}: CHF {booking.total_amount:.2f}")
print(f"Gesamtbetrag: CHF {invoice.get_total_amount():.2f}")

if __name__ == "__main__":
    print("Testlauf gestartet")


def book_room_in_hotel(bookings: list, guest, room, check_in_date: str, check_out_date: str) -> Booking:
    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
    check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
    num_nights = (check_out - check_in).days
    total_price = num_nights * room.price_per_night

    new_booking_id = max((b.booking_id for b in bookings), default=0) + 1

    booking = Booking(
        booking_id=new_booking_id,
        check_in_date=check_in_date,
        check_out_date=check_out_date,
        is_cancelled=False,
        total_amount=total_price,
        guest_id=guest.guest_id,
        room_id=room.room_id
    )

    booking.add_guest(guest)
    booking.add_room(room)
    bookings.append(booking)

    print(f"Buchung erfolgreich: {guest.first_name} im Zimmer {room.room_number} für {num_nights} Nächte – CHF {total_price:.2f}")
    return booking

