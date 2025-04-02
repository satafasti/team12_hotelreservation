class Room_type:

    def __init__(
            self,
            room_type_id : int,
            description : str, 
            max_guests : int,
            ):
    
        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def room_type_id(self):
        return self.__room_type_id

    @room_type_id.setter
    def room_type_id(self,new_room_type_id):
        self.__room_type_id = new_room_type_id

    @room_type_id.deleter
    def room_type_id(self):
        del self.__room_type_id    


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,new_description):
        self.__description = new_description


    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, new_max_guests):
        self.__max_guests = max_guests
        