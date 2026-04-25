from datetime import datetime
from zoneinfo import ZoneInfo  # built-in in Python 3.9+

def get_time(city):
    try:
        timezone = ZoneInfo(city)
        city_time = datetime.now(timezone)
        print(f"Current time in {city}: {city_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print("City not found. Use format like: Asia/Dubai or Europe/London")

# User input
city = input("Enter city timezone (e.g., Asia/Dubai): ")
get_time(city) 