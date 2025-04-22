class Room:

    def __init__(
            self,
            room_id : int,
            room_number : int,
            room_price_per_night : float,
            type_id : int, #ist in SQL enthalten
            ):

        ##sharp
    
        self.__room_id = room_id
        self.__room_number = room_number
        self.__room_price_per_night = room_price_per_night
        self.__type_id = type_id

    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self,new_room_id):
        self.__room_id = new_room_id

### id brauchen kein setter da autoincrementation von sql

    @room_id.deleter
    def room_id(self):
        del self.__room_id    

### braucht es diese funktion
#### test

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self,new_room_number):
        self.__room_number = new_room_number



    @property
    def room_price_per_night(self):
        return self.__room_price_per_night
     

    @room_price_per_night.setter
    def room_price_per_night(self, new_room_priece_per_night):
        self.__room_price_per_night = new_room_priece_per_night