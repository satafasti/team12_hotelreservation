import os

import model
import data_access

class FacilitiesManager():
    def __init__(self) -> None:
        self.__facilities_dal = data_access.FacilitiesDAL()