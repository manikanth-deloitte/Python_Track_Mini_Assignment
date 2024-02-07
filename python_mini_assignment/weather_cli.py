import argparse
import requests


def get_weather(api_key, city):
    """
        This function will get the city weather details from
         the public api openweathermap
    """

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    param_payload = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=param_payload)
    weather_data = response.json()

    try:
        if response.status_code == 200:
            current_weather = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            print(f"Weather in {city}:")
            print("--------------------------")
            print(f"Weather Condition: {current_weather}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {weather_data['message']}", response.status_code)
    except Exception as e:
        print(f"Error occurred file fetching weather data: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch the weather information for a city")
    parser.add_argument("city", help="City name")
    parser.add_argument("--api-key", help=" OpenWeatherMap API key", required=True)
    args = parser.parse_args()
    get_weather(args.api_key, args.city)
