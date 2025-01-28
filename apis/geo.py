import requests

def get_lat_long(city, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data:
            raise Exception("City not found. Please try again.")
        
        lat = data[0]["lat"]
        lon = data[0]["lon"]

        return lat, lon
    else:
        raise Exception("Error fetching data from API")