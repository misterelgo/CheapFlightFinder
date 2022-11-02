#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager



my_data_manager = DataManager()
sheety_data = my_data_manager.get_data()
my_flight_search = FlightSearch()
my_notification_manager = NotificationManager()

city_info = sheety_data["prices"]
for city in range (len(city_info)):
    city_name = city_info[city]['city']
    my_data_manager.put_IATA_code(city_info[city], my_flight_search.get_flight_IATA(city_name))
#pprint(my_data_manager.get_data())

ORIGIN_CITY_IATA = "LON"
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheety_data:
    flight = my_flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

if flight.price < destination["lowestPrice"]:
        my_notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )