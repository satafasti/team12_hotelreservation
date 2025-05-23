from __future__ import annotations

import model
from data_access.base_dal import BaseDAL


class HotelDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_hotel(self, hotel: model.Hotel):
        sql = """
        INSERT INTO Hotel(hotel_id, name, stars, address_id) VALUES (?, ?, ?, ?) #address_id kommt aber von address
        """
        params = (hotel.hotel_id if hotel else None, hotel.name, hotel.stars, hotel.address_id)
        self.execute(sql, params)

    def show_hotels_by_id(self, hotel: model.Hotel):
        sql = """
        SELECT * FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel.hotel_id)
        result = self.fetch_one(sql, params)
        if result:
            hotel_id, name, stars, address_id = result
            return model.Hotel(hotel_id, name, stars, address_id)
        else:
            return None

    def update_hotel(self, hotel: model.Hotel):
        sql = """
        UPDATE Hotel SET name = ? AND stars = ? WHERE hotel_id = ?
        """
        params = (hotel.name, hotel.stars, hotel.hotel_id)
        self.execute(sql, params)

    def delete_hotel(self, hotel: model.Hotel):
        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
        """
        params = (hotel.hotel_id,)
        self.execute(sql, params)