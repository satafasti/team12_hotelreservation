class Facilities:
    def __init__(
            self,
            facility_id: int,
            facility_name: str,
            ):
        if not facility_id:
            raise ValueError("Facility ID is required")
        if not isinstance(facility_id, int):
            raise TypeError("Facility ID must be an integer")
        if not facility_name:
            raise ValueError("Facility name is required")
        if not isinstance(facility_name, str):
            raise TypeError("Facility name must be a string")
            
        self.__facility_id: int = facility_id
        self.__facility_name: str = facility_name
    
    @property
    def facility_id(self) -> int:
        return self.__facility_id
        
    @property
    def facility_name(self) -> str:
        return self.__facility_name
    
    @facility_name.setter
    def facility_name(self, new_facility_name: str):
        if not new_facility_name:
            raise ValueError("Facility name required")
        if not isinstance(new_facility_name, str):
            raise TypeError("Facility name must be a string")
        self.__facility_name = new_facility_name
