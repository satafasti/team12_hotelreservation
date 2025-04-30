###Presentation-Layer

admin_options = int(input("What do you want to do? \n 1. Add a new Hotel \n 2. ..."))

## User-Story 3.1 Als Admin möchte ich neue Hotels zum System hinzufügen.
if admin_options == 1:
    hotel_id = input("Enter Hotel ID: ") #wird das benötigt oder wird ID von SQL generiert?
    if not hotel_id:
        raise ValueError("hotel_id must be set")
    hotel_id = int(hotel_id)

    name = input("Enter Hotel Name: ") #new hotel name
    if not name:
        raise ValueError("name must be set")

    stars = input("Enter Hotel stars: ") #new hotel stars
    if not stars:
        raise ValueError("stars must be set")

    street = input("Enter the street of the Hotel: ") #new hotel street
    if not street:
        raise ValueError("street must be set")

    city = input("Enter the city of the Hotel: ") #new hotel city
    if not city:
        raise ValueError("city must be set")

    zip_code = input("Enter the zip code of the Hotel: ") #new hotel zip_code
    if not zip_code:
        raise ValueError("zip_code must be set")
    print(f"A new hotel was generated with the following attributes: {hotel_id}, {name}, {stars}, {street}, {city}, {zip_code}.")






## User-Story 3.2 Als Admin möchte ich ein Hotel aus dem System entfernen.
#def delete_hotel

## User-Story 3.3. Als Admin möchte die Informationen bestimmter Hotels aktualisieren, z. B. den Namen, die Sterne usw.
#update_hotel_details


### Logic-Layer


# 7. Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann.
#Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.
#def calculate_seasonal_price

### Data-Layer


### Model-Layer