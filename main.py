# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from spreadsheet_tools import get_data_from_spreadsheet, put_data_to_spreadsheet
from new_data_manager import get_city_and_id_for_empty_iata
from flight_api_tools import get_iata_code

SHEETY_URL = "https://api.sheety.co/4a0d5dfd46da33d6c8aefcfae9f03882/fDeals/prices"
PUT_URL = "https://api.sheety.co/4a0d5dfd46da33d6c8aefcfae9f03882/fDeals/prices/"

city_iata_id = []

# Get spreadsheet data
google_sheets_data = get_data_from_spreadsheet(SHEETY_URL)
sheet_data = google_sheets_data["prices"]
# print(sheet_data)

# Get empty iata data
city_and_id = get_city_and_id_for_empty_iata(sheet_data)

# If there are any empty IATA cells, fetch the city code
for city in city_and_id:
    city["iataCode"] = get_iata_code(city["city"])
    city_iata_id.append(city)
print(city_iata_id)

# Put the city codes into the spreadsheet
for items in city_iata_id:
    url = f'{SHEETY_URL}/{str(items["id"])}'
    put_data_to_spreadsheet(url, items["iataCode"])

# Get spreadsheet data to send to flight finder
city_flight_info = get_data_from_spreadsheet(SHEETY_URL)
print(city_flight_info)

# Get flight data from Tequila
