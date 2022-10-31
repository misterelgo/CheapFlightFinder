import requests
from pprint import pprint
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_endpoint = "https://api.tequila.kiwi.com"
        self.api_KEY = "Cz5p2UwowjDvS0yK_m4Y1mX1AUXytyZ2"

    def get_flight_IATA(self, city_name):
        location_endpoint = f"{self.api_endpoint}/locations/query"
        headers = {"apikey": self.api_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        pprint(response.json())
        results = response.json()["locations"]
        print(results)
        code = results[0]["code"]
        return code