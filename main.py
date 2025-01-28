import os
import re
from apis.geo import get_lat_long
from apis.weather import get_weather


from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

chatmapping = {
    "hello": "Hi There!",
    "city": "Enter the city name:(Required) ",
    "date": "Enter the date [MM-DD-YYYY]:(Required) ", 
    "time": "Enter the time:(Not Required) ",
    "confirmation": "Fetching Weather...", 
    "weather": "The weather in city on date at time is: ",
    "redo": "Do you want to check the weather again?",
    "error": "Invalid input. Please try again.",
    "error_city": "City not found. Please try again."
}

try:
    #greeting
    print(chatmapping["hello"])
    
    #get user input
    city = input(chatmapping["city"])
    date = input(chatmapping["date"])
    
    if not city or not date:
        raise ValueError("City and Date are required fields.")
    elif not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
        raise ValueError("Invalid date format. Please enter date in MM-DD-YYYY format.") 

    
    month, day, year = [int(num) for num in date.split("-")]
    
    #final-date object 
    dateDict = { "month": month, "day": day, "year": year }


    time = input(chatmapping["time"])
    if not time:
        time = "00:00" 
    elif re.match(r"([01]?[0-9]|2[0-3]):[0-5][0-9]", time) is None:
        raise ValueError("Invalid time format. Please enter time in HH:MM format.") 
    
    print("\nFetching city data...")
    lat, lon = get_lat_long(city, api_key)

    print("\nFetching weather data...")
    min_temp, max_temp = get_weather(lat, lon, api_key, year, month, day)

    print(min_temp, max_temp)
    print("Done!")





except ValueError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")



