from pprint import pprint
import requests

projectName = "flightDeals"
sheetName = "prices"
sheety_API_URL = f"https://api.sheety.co/10fce03195300cfd5c84ea323144da6f/{projectName}/{sheetName}"
sheety_response = requests.get(url=sheety_API_URL)
sheety_response.raise_for_status()
sheety_result = sheety_response.json()

city_info = sheety_result["prices"]
city_info[0]['iataCode'] = "TESTING"
data = {
  "price": {
	"city": city_info[0]["city"],
	"iataCode": "TESTING",
	"lowestPrice": city_info[0]["lowestPrice"]
  }
}
api_endpoint = "https://api.tequila.kiwi.com"
api_KEY = "Cz5p2UwowjDvS0yK_m4Y1mX1AUXytyZ2"

location_endpoint = f"{api_endpoint}/locations/query"
headers = {"apikey": api_KEY}
query = {"term": "Berlin", "location_types": "city"}
# response = requests.get(url=location_endpoint, headers=headers, params=query)
# response.raise_for_status()
# results = response.json()["locations"]
# code = results[0]["code"]


