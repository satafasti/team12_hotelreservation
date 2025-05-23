
from business_logic.hotel_manager import HotelManager


# Eingabe vom Nutzer für Suche ohne Datum, braucht es für Suche mit Datum Booking = [] eine Liste damit dadurch iteriert werden kann? Wir haben auch für Booking keine Liste
print("Hallo - Bitte geben Sie ihre gewünschten Suchkriterien ein. \nSie könne eine Eingabe auch leer lassen, dann wird sie für die Suche nicht beachtet")

city = input("In Welche Stadt möchten Sie reisen?: ").strip()
stars = input("Wie viele Sterne soll Ihr Hotel mindestens haben?: ").strip()
guests = input("Für viele Personen soll das Zimmer sein?: ").strip()

stars = int(stars) if stars else None
guests = int(guests) if guests else None

manager = HotelManager()

results = manager.search_hotels(city, stars, guests)

if not results:
    print("Keine passenden Hotels gefunden.")
else:
    print("\nGefundene Hotels:\n")
    for hotel in results:
        print(f"- Hotelname: {hotel.name}")
        print(f"  Adresse: {hotel.address.street}, {hotel.address.zip_code} {hotel.address.city}")
        print(f"  Sterne: {hotel.stars}\n")
