import requests
import time

# Define the API endpoint and your API key
endpoint = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0"
headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY_HERE"
}

# Define the parameters for your flight search
params = {
    "originPlace": "LON",
    "destinationPlace": "PAR",
    "outboundDate": "2023-05-01",
    "inboundDate": "2023-05-08",
    "currency": "USD"
}

# Define a function that sends a request to Skyscanner's API and returns the cheapest price
def get_cheapest_price():
    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()

    # Extract the cheapest price from the response data
    prices = [quote["MinPrice"] for quote in data["Quotes"]]
    cheapest_price = min(prices)

    return cheapest_price

# Define a loop that runs every hour and prints the current cheapest price
while True:
    # Get the current cheapest price
    cheapest_price = get_cheapest_price()

    # Print the current cheapest price
    print(f"Current cheapest price: {cheapest_price}")

    # Wait for an hour before checking again
    time.sleep(3600)
