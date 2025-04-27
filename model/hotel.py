class Hotel:
    def __init__ (self, hotel_id:str, name:str, stars:float):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms =[]

    @property    
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, new_name):
        self.__name == new_name

    @property
    def hotel_id(self):
        return self.__hotel_id
    
    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def set_stars(self, new_stars):
        if new_stars > 0 and new_stars <= 5:
            self.__stars == new_stars
        else:
            print("Stars must be a number between 1 and 5.")


    def get_hotel_details(self):
        return f"Hotel name: {self.__name}, Stars: {self.__stars}"












