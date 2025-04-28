

    def get_hotel_details(self):
        return f"Hotel name: {self.__name}, Stars: {self.__stars}"

    def add_room(self, room_id: int, room_number: int, price_per_night: float, type_id: int):
        room = Room(room_id, room_number, price_per_night, type_id)
        self.__rooms.append(room)

    def show_room_details(self):
        print(f"Hotel name: {self.__name}, Stars: {self.__stars}"
        for room in self.__rooms:
            print(room.get_room_details())

    ## unclear if the show_room_details goes here and is correct? because we want to show the hotel details incl. the room details , only the room details will already be covered by the same function in the room class


