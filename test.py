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
sheety_response_put = requests.put(url=f"{sheety_API_URL}/{city_info[0]['id']}", json=data)
print(city_info[0])
pprint(sheety_response_put.json())


