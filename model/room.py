## Referenzprojekt Code:
#from __future__ import annotations
#from typing import TYPE_CHECKING

#if TYPE_CHECKING:
    #from model.artist import Artist
    #from model.track import Track

class Room:

    def __init__(self, room_id : int, room_number : int, price_per_night : float, type_id : int): #ID ist in SQL enthalten
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__type_id = type_id

    @property
    def room_id(self):
        return self.__room_id

    #@room_id.setter => Da Autoincrementation von SQL
    #def room_id(self,new_room_id):
        #self.__room_id = new_room_id

    ### braucht es diese funktion
    @room_id.deleter
    def room_id(self):
        del self.__room_id

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self,new_room_number):
        self.__room_number = new_room_number

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, new_price_per_night):
        self.__price_per_night = new_price_per_night