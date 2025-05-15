import model
from data_access.base_dal import Base_DAL


class RoomDAL(Base_DAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_room(self, room: model.Room): #room.description kommt aber von Room_Type
        sql = """
        INSERT INTO Room (room_id, room_number, price_per_night, description) VALUES (?, ?, ?, ?)
        """
        params = (room.room_id if room else None, room.room_number, room.price_per_night, room.description)
        self.execute(sql, params)

    def show_room_by_id(self, room: model.Room):
        sql = """
        SELECT * FROM Room WHERE room_id = ?
        """
        params = (room.room_id,)
        result = self.fetch_one(sql, params)
        if result:
            room_id, room_number, price_per_night, description = result
            return model.Room(room_id, room_number, price_per_night, description)
        else:
            return None

    def update_room(self, room: model.Room): #room.description kommt aber von Room_Type
        sql = """
        UPDATE Room SET room_number = ?, price_per_night = ?, description = ? WHERE room_id = ?
        """
        params = (room.room_number, room.price_per_night, room.description)
        self.execute(sql, params)

    def delete_room(self, room: model.Room):
        sql = """
        DELETE FROM Room WHERE room_id = ?
        """
        params = (room.room_id,)
        self.execute(sql, params)


