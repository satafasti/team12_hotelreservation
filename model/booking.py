class Booking:

    def __init__(
        self,
        booking_id: int,
        check_in_date: str,
        check_out_date: str,
        is_cancelled: bool,
        total_amount: float,
        guest_id: int,
        room_id: int
    ):
        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
        self.__guest_id = guest_id
        self.__room_id = room_id
        self.__invoice = None  # ← Verknüpfung zur Invoice

    @property
    def booking_id(self) -> int:
        return self.__booking_id

    @property
    def check_in_date(self) -> str:
        return self.__check_in_date

    @property
    def check_out_date(self) -> str:
        return self.__check_out_date

    @property
    def is_cancelled(self) -> bool:
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("is_cancelled must be a boolean")
        self.__is_cancelled = value

    @property
    def total_amount(self) -> float:
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, value: float):
        if value < 0:
            raise ValueError("total_amount must be non-negative")
        self.__total_amount = value

    @property
    def guest_id(self) -> int:
        return self.__guest_id

    @property
    def room_id(self) -> int:
        return self.__room_id

    @property
    def invoice(self):
        return self.__invoice

    def assign_invoice(self, invoice: 'Invoice'):
        self.__invoice = invoice
        invoice.add_booking(self)
