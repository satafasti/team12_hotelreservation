from __future__ import annotations

import model
from data_access.base_dal import Base_DAL


class InvoiceDAL(Base_DAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)