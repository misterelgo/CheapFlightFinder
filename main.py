#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

my_data_manager = DataManager()
sheet_data = my_data_manager.get_data()

city_info = sheet_data["prices"]
for city in city_info:
    if city['iataCode'] == '':
        print("its empty")