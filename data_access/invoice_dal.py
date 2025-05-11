from __future__ import annotations
from data_access.base_dal import BaseDAL
from model.invoice import Invoice

from typing import Optional, List

class InvoiceDAL(BaseDAL):
    def __init__(self, db_path: str):
        super().__init__(db_path)

    def create_invoice(self, booking_id: int, issue_date: str, total_amount: float) -> int:
        self.connect()
        sql = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount)
        VALUES (?, ?, ?)
        """
        params = (booking_id, issue_date, total_amount)
        self.execute_query(sql, params)
        invoice_id = self.execute("SELECT last_insert_rowid()")[0][0]
        self.disconnect()
        return invoice_id

    def get_invoice_by_id(self, invoice_id: int) -> Optional[Invoice]:
        self.connect()
        sql = "SELECT invoice_id, issue_date FROM Invoice WHERE invoice_id = ?"
        result = self.fetch_one(sql, (invoice_id,))
        self.disconnect()
        if result:
            return Invoice(invoice_id=result[0], issue_date=result[1])
        return None

    def get_invoices_by_booking(self, booking_id: int) -> List[Invoice]:
        self.connect()
        sql = "SELECT invoice_id, issue_date FROM Invoice WHERE booking_id = ?"
        results = self.fetch_all(sql, (booking_id,))
        self.disconnect()
        return [Invoice(invoice_id=row[0], issue_date=row[1]) for row in results]

    def delete_invoice(self, invoice_id: int):
        self.connect()
        sql = "DELETE FROM Invoice WHERE invoice_id = ?"
        self.execute_query(sql, (invoice_id,))
        self.disconnect()
