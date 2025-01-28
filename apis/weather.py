import requests

def get_weather(lat, lon, api_key, year, month, day):
    url = f"https://api.openweathermap.org/data/3.0/onecall/day_summary?lat={lat}&lon={lon}&date={year}-{month}-{day}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature_dict = data["temperature"]
        min_temp = temperature_dict["min"]
        max_temp = temperature_dict["max"]

        return min_temp, max_temp
    elif response.status_code == 400:
        raise Exception("Invalid date format. Please try again.") 
    else:
        raise Exception("Error fetching data from API")