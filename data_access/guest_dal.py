from __future__ import annotations

import model
from data_access.base_dal import Base_DAL


class GuestDAL(Base_DAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_guest(self, guest: model.Guest):
        sql = """
        INSERT INTO Guests(guest_id, first_name, last_name, email, address_id) VALUES (?, ?, ?, ?, ?) #address_id kommt aber von address
        """
        params = (guest.guest_id if guest else None, guest.first_name, guest.last_name, guest.email, guest.address_id)
        self.execute(sql, params)

    def show_guest_by_id(self, guest: model.Guest):
        sql = """
        SELECT * FROM Guests WHERE guest_id = ?
        """
        params = (guest.guest_id,)
        result = self.fetch_one(sql, params)
        if result:
            guest_id, first_name, last_name, email, address_id = result
            return model.Guest(guest_id, first_name, last_name, email, address_id)
        else:
            return None

    def update_guest(self, guest: model.Guest):
        sql = """
        UPDATE Guests SET first_name = ? AND last_name = ? WHERE guest_id = ?
        """
        params = (guest.first_name, guest.last_name, guest.guest_id)
        self.execute(sql, params)

    def delete_guest(self, guest: model.Guest):
        sql = """
        DELETE FROM Guests WHERE guest_id = ?
        """
        params = (guest.guest_id,)
        self.execute(sql, params)
