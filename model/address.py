class Address:

    def __init__(self, address_id : int, street : str, city : str, zip_code : str):
        if not address_id:
            raise ValueError("Address ID is required")
        if not isinstance(address_id, int):
            raise TypeError("Address ID must be an integer")
        if not street:
            raise ValueError("Street must be provided")
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        if not city:
            raise ValueError("City must be provided")
        if not isinstance(city, str):
            raise TypeError("City must be a string")
    
        self.__address_id : int = address_id
        self.__street : str = street
        self.__city : str = city
        self.__zip_code : str = zip_code

    @property
    def address_id(self) -> int:
        return self.__address_id

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, new_street : str):  #set_street, die methode muss gleich heissen wie der setter selbst, also street.setter muss dann street heissen und nicht set_street
        if not new_street:
            raise ValueError ("street required")
        if not isinstance(new_street , str):
             raise TypeError("street must be a string")
        self.__street = new_street  #Referenzprojekt anschauen um die syntax zu checken, wenn wir einen neuen wert generieren müssen wir diesen am schluss noch einmal speichern

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, new_city : str):
        if not new_city:
            raise ValueError ("city required")
        if not isinstance(new_city , str):
             raise TypeError("city must be a string")
        self.__city = new_city

    @property
    def zip_code(self) -> str:
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, new_zip_code : str):
        if not new_zip_code:
            raise ValueError ("zip_code required")
        if not isinstance(new_zip_code , str):
             raise TypeError("zip must be a string")
        self.__zip_code = new_zip_code


# bei 0-werten prüfen ob wir definieren können was passieren soll? es kanns ein dass ein datensatz leer ist, was passiert dann? IF NOT prüfen ob die okay sind








