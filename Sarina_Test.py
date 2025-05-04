############ Model-Layer
#Code wurde verändert!
class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, address_id: int, rooms: list): #address in address_id geändert, da in DB nur ID hinterlegt ist
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
        if not rooms or not isinstance(rooms, list):
            raise ValueError("rooms must be a non-empty list")
        if len(rooms) == 0:
            raise ValueError("at least one room is required")


        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = rooms
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

#Code wurde nicht verändert!
class Room_Type:

    def __init__(self, type_id : int, description : str, max_guests : int):
        if not type_id:
            raise ValueError("type_id must be set")
        if not isinstance(type_id, int):
            raise TypeError("type_id must be a int")
        if not description:
            raise ValueError("description must be set")
        if not isinstance(description, str):
            raise TypeError("description must be a str")
        if not max_guests:
            raise ValueError("max_guests must be set")
        if not isinstance(max_guests, int):
            raise TypeError("max_guests must be a int")

        self.__type_id = type_id
        self.__description = description #z.B. Einzelzimmer
        self.__max_guests = max_guests

    @property
    def type_id(self):
        return self.__type_id


    #@room_type_id.setter => Da Autoincrementation von SQL
    #def type_id(self,new_type_id):
        #self.__type_id = new_type_id

    #@type_id.deleter #anschauen wie korrekt gemacht wird
    #def type_id(self):
        #del self.__type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description):
        self.__description = new_description

    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, new_max_guests):
        self.__max_guests = new_max_guests

#Code wurde verändert!
class Room:
    def __init__(self, room_id : int, room_number : int, price_per_night : float, description: Room_Type): #ID ist in SQL enthalten?
        if not room_id:
            raise ValueError("room_id must be set")
        if not isinstance(room_id, int):
            raise TypeError("room_id must be a int")
        if not room_number:
            raise ValueError("room_number must be set")
        if not isinstance(room_id, int):
            raise TypeError("room_number must be a int")
        if not price_per_night:
            raise ValueError("price_per_night must be set")
        if not isinstance(price_per_night, float):
            raise TypeError("price_per_night must be a float")

        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__description = Room_Type.description #Description von Class room_type soll übergeben werden
        self.__facility_name = [] #Liste für Facilities des Raumes

    @property
    def room_id(self):
        return self.__room_id

    #@room_id.setter => Da Autoincrementation von SQL
    #def room_id(self,new_room_id):
        #self.__room_id = new_room_id

#room_number
    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self,new_room_number):
        self.__room_number = new_room_number

#id_deleter
    #@room_id.deleter #anschauen
    #def room_id(self):
        #del self.__room_id

#price per night
    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, new_price_per_night):
        self.__price_per_night = new_price_per_night

#description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,new_description):
        self.__description = new_description

#facility_name
    @property
    def facility_name(self):
        return self.__facility_name

    @facility_name.setter
    def facility_name(self,new_facility_name):
        self.__facility_name = new_facility_name


############ Logic-Layer

### User-Story 3.1 Als Admin möchte ich neue Hotels zum System hinzufügen.

def create_hotel():
    rooms = []
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

    #Angaben zum Raum
    while True:
        create_new_room = {}
        room_id = input("Enter room ID: ") #new room_id
        if not room_id:
            raise ValueError("room_id must be set")
        if not room_id.isdigit():
            raise TypeError("room_id must be an integer")
        create_new_room["room_id"] = int(room_id)
        room_number = input("Enter room number: ")
        if not room_number:
            raise ValueError("room_number must be set")
        if not room_number.isdigit():
            raise TypeError("room_number must be an integer")
        create_new_room["room_number"] = int(room_number)
        price_per_night = input("Enter price per night for the room: ")
        if not price_per_night:
            raise ValueError("price_per_night must be set")
        try:
            create_new_room["price_per_night"] = float(price_per_night)
        except ValueError:
            raise ValueError("price_per_night must be a float")
        description = input("Enter room type description: ")
        max_guests = input("Enter max guests: ")
        if not max_guests.isdigit():
            raise TypeError("max_guests must be an integer")

        room_type = Room_Type(
            type_id=create_new_room["room_id"],
            description=description,
            max_guests=int(max_guests)
        )

        # Neues Room-Objekt erstellen
        add_new_room = Room(
            room_id=create_new_room["room_id"],
            room_number=create_new_room["room_number"],
            price_per_night=create_new_room["price_per_night"],
            description=room_type
        )
        rooms.append(add_new_room)

        more = input("Add another room? (y/n): ")
        if more.lower() != 'y':
            break

        # Neues Hotel-Objekt erstellen
    add_new_hotel = Hotel(
        hotel_id=create_new_hotel["hotel_id"],
        name=create_new_hotel["name"],
        stars=create_new_hotel["stars"],
        address_id=create_new_address["address_id"], # address_id an das Hotel übergeben
        rooms=rooms
    )
    return create_new_hotel["hotel_id"], add_new_hotel

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