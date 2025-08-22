import requests
import json

def get_weather(city):
    # Using OpenWeatherMap API (you'll need an API key)
    api_key = "your_api_key_here"  # Replace with actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Humidity: {data['main']['humidity']}%")
        
    except requests.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("City not found or invalid API response")

# Example usage (requires valid API key)
# get_weather("London")
