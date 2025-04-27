#import os

import model
import data_access

class Room_Manager():
    def __init__(self) -> None:
        self.__room_dal = data_access.RoomDAL()

    def create_room(self, room_id : int, room_number : int, price_per_night : float, description : model.Room_Type) -> model.Room:
        return self.__room_dal.create_new_room(room_id, room_number, price_per_night, description)

    def get_room_details(self, room: Room):
        return f"Room ID: {self.room_id}, Room Number: {self.room_number}, Price per Night: {self.price_per_night}, Room Type: {self.room.description}"

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



#add_facilities
#add_roomtype

#def show_room_details(self):
    #return f"Room number: {self.__room_number}, Price per night: {self.__room_price_per_night}, Type: {self.__type_id}"  # wäre sinnvolller, wenn Name, statt Typ
