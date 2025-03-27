class Address:

    def __init__(
            self,
            address_id : int,
            street : str,
            city : str,
            zip : str,):
    
        self.__address_id : int = address_id
        self.__street : str = street
        self.__city : str = city
        self.__zip : str = zip

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street : str):
        if not street:
            raise valueerror ("street required")
        if not isinstance(street , str):
             raise TypeError("street must be a string")

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city : str):
        if not city:
            raise valueerror ("city required")
        if not isinstance(city , str):
             raise TypeError("city must be a string")

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip : str):
        if not zip:
            raise valueerror ("zip required")
        if not isinstance(zip , str):
             raise TypeError("zip must be a string")

### Question is zip a str or int???




