from data_access.base_dal import BaseDal
import model

class BookingDAL(BaseDal):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_booking(self, booking: model.Booking):
        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            int(booking.is_cancelled),
            booking.total_amount
        )
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid

    def get_booking_by_id(self, booking_id: int):
        sql = "SELECT * FROM Booking WHERE booking_id = ?"
        result = self.fetchone(sql, (booking_id,))
        if result:
            return model.Booking(*result)
        return None

    def update_booking(self, booking: model.Booking):
        sql = """
        UPDATE Booking
        SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ?, is_cancelled = ?, total_amount = ?
        WHERE booking_id = ?
        """
        params = (
            booking.guest_id,
            booking.room_id,
            booking.check_in_date,
            booking.check_out_date,
            int(booking.is_cancelled),
            booking.total_amount,
            booking.booking_id
        )
        self.execute(sql, params)

    def delete_booking(self, booking_id: int):
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        self.execute(sql, (booking_id,))

    def get_all_bookings(self):
        sql = "SELECT * FROM Booking"
        results = self.fetchall(sql)
        return [model.Booking(*row) for row in results]

    def get_bookings_by_guest_id(self, guest_id: int):
        sql = "SELECT * FROM Booking WHERE guest_id = ?"
        results = self.fetchall(sql, (guest_id,))
        return [model.Booking(*row) for row in results]

    def cancel_booking(self, booking_id: int):
        sql = "UPDATE Booking SET is_cancelled = 1 WHERE booking_id = ?"
        self.execute(sql, (booking_id,))
