import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric' 
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data['message']}")
            return None
    except requests.ConnectionError:
        print("Error: Unable to connect to the weather API.")
        return None

def display_weather(weather_data):
    if weather_data:
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print("\nCurrent Weather:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
    else:
        print("Unable to fetch weather data.")

def main():
    print("Welcome to the Weather App!")
    api_key = input("Enter your OpenWeatherMap API key: ")

    while True:
        location = input("Enter the city or ZIP code for weather information (or 'exit' to quit): ")
        if location.lower() == 'exit':
            break

        weather_data = get_weather(api_key, location)

        if weather_data:
            display_weather(weather_data)

if __name__ == "__main__":
    main()
