# -----------------------------------
# IMPORTS & PATH FIX
# -----------------------------------
import sys, os
sys.path.append(os.path.abspath("."))

from model.guest import Guest
from model.room import Room
from model.room_type import Room_Type
from model.booking import Booking
from model.invoice import Invoice
from model.facilities import Facilities

from business_logic.booking_manager import book_room_in_hotel, show_all_bookings
from business_logic.room_manager import show_room_facilities
from business_logic.room_type_manager import update_room_type

# -----------------------------------
# TESTDATEN
# -----------------------------------
# Gäste
guest1 = Guest(1, "Max", "Muster", "max@example.com")
guest2 = Guest(2, "Erika", "Beispiel", "erika@example.com")
guests = [guest1, guest2]

# Zimmertypen
type_single = Room_Type(1, "Einzelzimmer", 1)
type_double = Room_Type(2, "Doppelzimmer", 2)
room_types = [type_single, type_double]

# Zimmer
room1 = Room(1, 101, 100.0, type_single)
room2 = Room(2, 102, 150.0, type_double)
room1.facility_name = ["WLAN", "TV"]
room2.facility_name = ["WLAN"]
rooms = [room1, room2]

# Buchungen
bookings = []

# -----------------------------------
# TESTAUSFÜHRUNG: USER STORIES
# -----------------------------------
if __name__ == "__main__":

    # 4 – Zimmer buchen
    print("\n--- USER STORY 4: Zimmer buchen ---")
    book_room_in_hotel(bookings, guest1, room1, "2025-08-01", "2025-08-05")

    # 8 – Alle Buchungen anzeigen
    print("\n--- USER STORY 8: Alle Buchungen anzeigen ---")
    show_all_bookings(bookings, guests, rooms)

    # 9 – Zimmer mit Ausstattung anzeigen
    print("\n--- USER STORY 9: Zimmerausstattung anzeigen ---")
    show_room_facilities(rooms)

    # 10 – Stammdaten ändern
    print("\n--- USER STORY 10: Zimmertyp ändern ---")
    update_room_type(room_types, 1, new_description="Business-Einzelzimmer", new_max_guests=1)
