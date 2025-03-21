import requests

def get_gate_listings():
    url = "https://api.gateio.ws/api/v4/spot/currency_pairs"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['id'] for coin in data]
    return []

if __name__ == "__main__":
    listings = get_gate_listings()
    print("Gate.io New Listings:", listings)
