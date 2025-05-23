#import os
import data_access
from model.room import Room
from model.room_type import Room_Type
from model.facilities import Facilities

class RoomManager:
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDAL()
        self.__description = []
        self.__facility_name = []

    def create_room(self, room_id : int, room_number : int, price_per_night : float, description : Room_Type) -> Room:
        return self.__room_dal.create_new_room(room_id, room_number, price_per_night, description)

    #def get_room_details(self, room: Room): #evtl. irgendwo anders ablegen statt hier => im HotelManager
        #return f"Room ID: {room.room_id}, Room Number: {room.room_number}, Price per Night: {room.price_per_night}, Room Type: {room.description}"

    def add_description(self, room: Room, description: Room_Type):
        if not description:
            raise ValueError("Description cannot be empty")
        if not isinstance(description, Room_Type):
            raise ValueError("Description must be a Room_Type")
        if description not in self.__description:
            self.__description.append(description)
            room.description = self #geht nicht

    def add_facilities(self, room: Room, facility_name: Facilities):
        if not facility_name:
            raise ValueError("Facility cannot be empty")
        if not isinstance(facility_name, Facilities):
            raise ValueError("facility_name must be a Facilities")
        if facility_name not in self.__facility_name:
            self.__facility_name.append(facility_name)
            room.facility_name = self

    def show_room_facilities(rooms):
        print("Zimmerausstattung:")
        for r in rooms:
            print(f" - Zimmer {r.room_number}: {', '.join(r.facility_name)}")


    def is_available(self):
        for room in self.__hotel.rooms:
            if room.room_id == self.room_id and room.room_available == True:
                return True
        return False
