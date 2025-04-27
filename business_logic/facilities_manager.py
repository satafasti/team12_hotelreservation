import os

import model
import data_access

class Facilities_Manager():
    def __init__(self) -> None:
        self.__facilities_dal = data_access.FacilitiesDAL()