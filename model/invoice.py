class Invoice:

    def __init__(
        self,
        invoice_id: int,
        issue_date: str,
        total_amount: float,
        booking_id: int
    ):
        self.__invoice_id = invoice_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount
        self.__booking_id = booking_id

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @property
    def issue_date(self) -> str:
        return self.__issue_date

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        if value < 0:
            raise ValueError("total_amount must be non-negative")
        self.__total_amount = value

    @property
    def booking_id(self) -> int:
        return self.__booking_id


### Diskussion:  Total amount habe ich einmal im Invoice und im Booking, 
###weil eine Rechung kann mehrere Buchungen haben und eine Buchung auch 
### mehrere Zusatzleistungen hat.