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

    def get_room_details(self, room: Room): #evtl. irgendwo anders ablegen statt hier
        return f"Room ID: {room.room_id}, Room Number: {room.room_number}, Price per Night: {room.price_per_night}, Room Type: {room.description}"

    def add_description(self, room: Room, description: Room_Type):
        if not description:
            raise ValueError("Description cannot be empty")
        if not isinstance(description, Room_Type):
            raise ValueError("Description must be a Room_Type")
        if description not in self.__description:
            self.__description.append(description)
            room.description = self

    def add_facilities(self, room: Room, facility_name: Facilities):
        if not facility_name:
            raise ValueError("Facility cannot be empty")
        if not isinstance(facility_name, Facilities):
            raise ValueError("facility_name must be a Facilities")
        if facility_name not in self.__facility_name:
            self.__facility_name.append(facility_name)
            room.facility_name = self





    #def add_track(self, track: Track) -> None:
        #from model import Track

        #if not track:
            #raise ValueError("track is required")
        #if not isinstance(track, Track):
            #raise ValueError("track must be an instance of Track")
        #if track not in self.__tracks:
            #self.__tracks.append(track)
            #track.album = self


    #def read_facilities_room(self, room: model.facilities) -> None:
        #self.__room_dal.read_facilities_by_room(facilities)

    #def read_room(self, room_id : int, room_number : int, price_per_night : float, type_id : model.room_type) -> model.Room:
        #return self.__room_dal.read_room_by_id(room_id)

#class Album_Manager():
    #def __init__(self) -> None:
        #self.__album_dal = data_access.AlbumDAL()

    #def create_album(self, title: str, artist: model.Artist = None) -> model.Album:
        #return self.__album_dal.create_new_album(title, artist)

    #def read_artists_albums(self, artist: model.Artist) -> None:
        #self.__album_dal.read_albums_by_artist(artist)

    #def read_album(self, album_id: int) -> model.Album:
        #return self.__album_dal.read_album_by_id(album_id)
