from __future__ import annotations

import model
from data_access.base_dal import BaseDAL


class Room_TypeDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)