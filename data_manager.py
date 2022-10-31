import requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.projectName = "flightDeals"
        self.sheetName = "prices"
        self.sheety_API_URL = "https://api.sheety.co/10fce03195300cfd5c84ea323144da6f/" + self.projectName + "/" + self.sheetName

    def get_data(self):
        sheety_response = requests.get(url=self.sheety_API_URL)
        sheety_response.raise_for_status()
        sheety_result = sheety_response.json()
        return sheety_result

