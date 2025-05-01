############ Model-Layer
#Code wurde verändert!
class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address_id: int): #address in address_id geändert, da in DB nur ID hinterlegt ist
        if not hotel_id:
            raise ValueError("hotel_id must be set")
        if not isinstance(hotel_id, int):
            raise TypeError("hotel_id must be a int")
        if not name:
            raise ValueError("name must be set")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not address_id:
            raise ValueError("address must be set")
        if not isinstance(address_id, int):
            raise TypeError("address_id must be a int")

        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = []
        self.__address_id = address_id #changed to address_id # single instance of class Address, as of now no backwards link from address -> hotel necessary, to find all hotels in a city loop through existing instances by city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("name must be set")
        if not isinstance(new_name, str):
            raise TypeError("name must be a string")
        self.__name = new_name

    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, new_stars):
        if not isinstance(new_stars, int):
            raise TypeError("new_stars must be a int")
        elif 0 < new_stars <= 5: # neue Schreibweise
            self.__stars = new_stars
        else:
            print("Stars must be a number between 1 and 5.")

    @property # damit auf address_id zugegriffen werden kann
    def address_id(self):
        return self.__address_id

    @address_id.setter
    def address_id(self, new_address_id):
        self.__address_id = new_address_id

############ Logic-Layer

### User-Story 3.1 Als Admin möchte ich neue Hotels zum System hinzufügen.

def create_hotel(): # müsste man wohl noch mit der Class Hotel kombinieren.
    ### Angaben für Hoteladresse
    create_new_address = {}
    address_id = input("Enter Address ID: ") #new address_id falls benötigt
    if not address_id:
        raise ValueError("Address ID must be set")
    if not address_id.isdigit():
        raise ValueError("Address ID must be integer")
    create_new_address["address_id"] = int(address_id)
    street = input("Enter the street of the Hotel: ") #new hotel street
    if not street:
        raise ValueError("street must be set")
    create_new_address["street"] = street
    city = input("Enter the city of the Hotel: ") #new hotel city
    if not city:
        raise ValueError("city must be set")
    create_new_address["city"] = city
    zip_code = input("Enter the zip code of the Hotel: ") #new hotel zip_code
    if not zip_code:
        raise ValueError("zip_code must be set")
    create_new_address["zip_code"] = zip_code

    ### Angaben zum Hotel
    create_new_hotel = {}
    hotel_id = input("Enter Hotel ID: ") #wird das benötigt oder wird ID von SQL generiert?
    if not hotel_id:
        raise ValueError("hotel_id must be set")
    if not hotel_id.isdigit():
        raise TypeError("hotel_id must be an integer")
    create_new_hotel["hotel_id"] = int(hotel_id)
    name = input("Enter Hotel Name: ") #new hotel name
    if not name:
        raise ValueError("name must be set")
    create_new_hotel["name"] = name
    stars = input("Enter Hotel stars: ") #new hotel stars
    if not stars:
        raise ValueError("stars must be set")
    if not stars.isdigit():
        raise TypeError("stars must be an integer")
    create_new_hotel["stars"] = int(stars)

    # Neues Hotel-Objekt erstellen
    add_new_hotel = Hotel(
        hotel_id=create_new_hotel["hotel_id"],
        name=create_new_hotel["name"],
        stars=create_new_hotel["stars"],
        address_id=create_new_address["address_id"] # address_id an das Hotel übergeben
    )
    return create_new_hotel["hotel_id"], add_new_hotel

# müsste nicht noch mind. 1 Raum hinzugefügt werden, da ohne mind. 1 Raum gibt es ja eigentlich kein Hotel?

################################################

### User-Story 3.2 Als Admin möchte ich ein Hotel aus dem System entfernen.

def delete_hotel(hotel):
    hotel_id_input = input("Enter the hotel ID of the hotel you want to remove: ") #kann man darauf zugreifen, wenn mit SQL generiert?
    if not hotel_id_input.isdigit():
        raise ValueError("Hotel ID must be an integer")
    hotel_id_input = int(hotel_id_input) #damit umgewandelt wird von str in int
    if hotel_id_input in hotel:
        del hotel[hotel_id_input]
        print(f"Hotel with ID {hotel_id_input} was deleted.")
    else:
        print("No hotel found with that ID.")

# 3.3. Als Admin möchte ich die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.
def update_hotel_details(hotel):
    hotel_id_input = input("Enter the hotel ID of the hotel you want to update: ")
    if not hotel_id_input.isdigit():
        raise ValueError("Hotel ID must be an integer")
    if hotel_id_input not in hotel:
        print("Hotel not found.")
    hotel_obj = hotel[hotel_id_input] #?

    # Update Name
    new_name = input(f"Enter new name (leave empty to keep '{hotel_obj.name}'): ")
    if new_name:
        hotel_obj.name = new_name
    else:
        print("No new name entered.")

    # Update Stars
    new_stars = input(f"Enter new stars (1–5, current: {hotel_obj.stars}): ")
    if new_stars:
        hotel_obj.stars = int(new_stars)
    else:
        print("No stars were entered.")

    # Update Address ID
    new_address_id = input(f"Enter new address ID (leave empty to keep {hotel_obj.address_id}): ")
    if new_address_id:
        if new_address_id.isdigit():
            hotel_obj.address_id = int(new_address_id)
        else:
            print("Address ID must be a number.")
    print("Hotel updated successfully.")


# 7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.
#Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.
#def calculate_seasonal_price

hotel = {}

############ Presentation-Layer

while True:
    admin_options = int(input("What do you want to do? \n 1 = Add a new Hotel \n 2 = Delete a existing Hotel \n 0 = exit"))

    if admin_options == 1:
        hotel_id, hotel_obj = create_hotel()
        hotel[hotel_id] = hotel_obj
        print(f"Hotel added successfully:")
        print(f"Hotel ID: {hotel_obj.hotel_id}")
        print(f"Name: {hotel_obj.name}")
        print(f"Stars: {hotel_obj.stars}")
        print(f"Address ID: {hotel_obj.address_id}")

    elif admin_options == 2:
        delete_hotel(hotel)

    elif admin_options == 0:
        # Aktuelle Übersicht aller Hotels
        print("Aktuelle Hotels im System:")
        for hotel_id, hotel_obj in hotel.items():
            print(
                f"Hotel ID: {hotel_id}, Name: {hotel_obj.name}, Stars: {hotel_obj.stars}, Address ID: {hotel_obj.address_id}")
        break
    else:
        print("Invalid input.")

### Data-Layer