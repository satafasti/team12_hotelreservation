import data_access
from model import Room, room
from model.hotel import Hotel

class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()


    def get_hotel_details(self):
        return f"Hotel name: {self.__name}, Stars: {self.__stars}"

    def add_room(self, room_id: int, room_number: int, price_per_night: float, type_id: int):
        room = Room(room_id, room_number, price_per_night, type_id)
        self.__rooms.append(room)

    def remove_room(self, room: Room) -> None:
        from model import Room

        if not room:
            raise   ValueError ("room cannot be None")
        if not isinstance(room, Room):
            raise ValueError ("room must be an instance of Room")
        if room in self.__rooms:
            self.__rooms.remove(room)


    def show_room_details(self):
        print(f"Hotel name: {self.__name}, {self.__stars} Stars")
        for room in self.__rooms:
            print(room.get_room_details())

    ## unclear if the show_room_details goes here and is correct? because we want to show the hotel details incl. the room details , only the room details will already be covered by the same function in the room class


    def add_new_hotel(self, hotel_id: int, name: str, stars: int, address: str) -> Hotel:
        if not name:
            raise ValueError("Hotel name cannot be empty.")
        if not isinstance(name, str):
            raise ValueError("Hotel name must be a str")
        if name not in self.__name: # irgendwie noch nicht ganz so logisch, daher wohl falsch
            self.__name.append(name)
            hotel.name = self
        if not address:
            raise ValueError("Address cannot be empty.")
        if not isinstance(name, str):
            raise ValueError("Address must be a str")
        if address not in self.__address: # irgendwie noch nicht ganz so logisch, daher wohl falsch
            self.__address.append(address)
            hotel.address = self
