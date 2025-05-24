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

## Test User Story 1 -> alle Suchkriterien zusammengefasst, Suchfunktion OHNE Suche nach Datum, nur mit boolean room_available in class Room

def search_hotels(city=None, stars=None, guests=None):
    results = []

    for hotels in Hotel: #wir haben keine Liste von Hotels, muss zwingend auf hotel_id referenziert werden?
        if city and hotel.address.city.lower() != city.lower():
            continue
        if stars and hotel.stars < stars:
            continue

        for room in hotel.rooms:
            if guests and room.room_type.max_guests < guests:
                continue
            if not room.room_available:
                continue

            # Sobald ein passender Raum gefunden wurde, reicht es – Hotel ist relevant
            results.append(hotel)
            break  # keine weiteren Zimmer prüfen

    return results


# Eingabe vom Nutzer für Suche  ohne Datum, braucht es für Suche mit Datum Booking = [] eine Liste damit dadurch iteriert werden kann? Wir haben auch für Booking keine Liste
print("Hallo - Bitte geben Sie ihre gewünschten Suchkriterien ein. \nSie könne eine Eingabe auch leer lassen, dann wird sie für die Suche nicht beachtet")

city = input("In Welche Stadt möchten Sie reisen?: ").strip()
stars = input("Wie viele Sterne soll Ihr Hotel mindestens haben?: ").strip()
guests = input("Für viele Personen soll das Zimmer sein?: ").strip()

stars = int(stars) if stars else None
guests = int(guests) if guests else None

results = search_hotels(city, stars, guests)

if not results:
    print("Keine passenden Hotels gefunden.")
else:
    print("\nGefundene Hotels:\n")
    for hotel in results:
        print(f"- Hotelname: {hotel.name}")
        print(f"  Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
        print(f"  Sterne: {hotel.stars}\n")


test_logic

