import sys, os
sys.path.append(os.path.abspath('..'))

from model.hotel import Hotel
from business_logic.booking_manager import book_room_in_hotel

def test_booking():
    # hier dein Code zur Buchung
    ...

from model.address import Address
from model.hotel import Hotel
from model.room import Room
from model.room_type import Room_Type
from model.guest import Guest
from model.booking import Booking
from model.invoice import Invoice
from .model.facilities import Facilities

from business_logic.booking_manager import book_room_in_hotel


# Testdaten anlegen

# Address-Objekte
address1 = Address(1, "Bahnhofstrasse 1", "Zürich", "8001")
address2 = Address(2, "Marktplatz 5", "Basel", "4001")

# Hotel-Objekte
hotel1 = Hotel(1, "Grand Hotel Zürich", 5, address1)
hotel2 = Hotel(2, "City Hotel Basel", 4, address2)

# Room_Type-Objekte
single_room_type = Room_Type(1, "Single Room", 1)
double_room_type = Room_Type(2, "Double Room", 2)

# Room-Objekte
room1 = Room(1, 101, 150.0, single_room_type)
room2 = Room(2, 102, 200.0, double_room_type)

# Facilities-Objekte
facility_wifi = Facilities(1, "WLAN")
facility_tv = Facilities(2, "Fernseher")

# Facilities dem Room hinzufügen
room1.facility_name = ["WLAN", "Fernseher"]
room2.facility_name = ["WLAN"]

# Guest-Objekte
guest1 = Guest(1, "Max", "Muster", "max.muster@example.com")
guest2 = Guest(2, "Erika", "Beispiel", "erika.beispiel@example.com")

# Booking-Objekte
booking1 = Booking(1, "2025-06-01", "2025-06-05", False, 600.0, guest1.guest_id, room1.room_id)
booking2 = Booking(2, "2025-07-10", "2025-07-12", False, 400.0, guest2.guest_id, room2.room_id)

# Invoice-Objekte
invoice1 = Invoice(1, "2025-06-05")
invoice2 = Invoice(2, "2025-07-12")

# Buchungen mit Rechnungen verknüpfen
booking1.add_invoice(invoice1)
booking2.add_invoice(invoice2)

# Gast und Zimmer verknüpfen
booking1.add_guest(guest1)
booking1.add_room(room1)

booking2.add_guest(guest2)
booking2.add_room(room2)

# Alle Hotels, Rooms, Bookings, Guests, Invoices in Listen speichern
hotels = [hotel1, hotel2]
rooms = [room1, room2]
guests = [guest1, guest2]
bookings = [booking1, booking2]
invoices = [invoice1, invoice2]



