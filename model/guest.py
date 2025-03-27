###from model.address import Adresss

class Guest:


    def __init__(
            self,
            guest_id : int,
            first_name : str,
            last_name : str,
            email : str,
            ###address : Address = None,
            ):
    
        self.__guest_id : int = guest_id
        self.__first_name : str = first_name
        self.__last_name : str = last_name
        self.__email : str = email
        ###self.__address : Adress = address

    @property
    def guest_id(self) -> int:
        return self.__guest_id


    @property
    def first_name(self) -> str:
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name : str):
        if not first_name:
            raise valueerror ("first_name required")
        if not isinstance(first_name , str):
             raise TypeError("first_name must be a string")

    @property
    def last_name(self) -> str:
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name : str):
        if not last_name:
            raise valueerror ("last_name required")
        if not isinstance(last_name , str):
             raise TypeError("last_name must be a string")

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email : str):
        if not email:
            raise valueerror ("email required")
        if not isinstance(email , str):
             raise TypeError("email must be a string")


###    @property
###    def adress(self) -> Address:
###        return self.__address

### question foreign key setter function address

###    @address.setter
###   def address(self, address : Address):
###       from model import Address

