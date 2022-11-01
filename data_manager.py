import requests
from flight_data import FlightData
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.projectName = "flightDeals"
        self.sheetName = "prices"
        self.sheety_API_URL = f"https://api.sheety.co/10fce03195300cfd5c84ea323144da6f/{self.projectName}/{self.sheetName}"

    def get_data(self):
        sheety_response = requests.get(url=self.sheety_API_URL)
        sheety_response.raise_for_status()
        sheety_result = sheety_response.json()
        return sheety_result

    def put_IATA_code(self, city_info,  IATA_code):
        self.sheety_IATA_API_URL = f"https://api.sheety.co/10fce03195300cfd5c84ea323144da6f/{self.projectName}/{self.sheetName}/{city_info['id']}"
        self.data = {
            "price": {
                "city": city_info["city"],
                "iataCode": IATA_code,
                "lowestPrice": city_info["lowestPrice"]
            }
        }
        response = requests.put(url=self.sheety_IATA_API_URL, json=self.data)
        #print("response.status_code =", response.status_code)
        return response.json()
