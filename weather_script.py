import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch weather data"}

if __name__ == "__main__":
    API_KEY = "f88886a339b7efbb28f769d5ff44d0f9"
    city_name = input("Enter the city name: ")
    weather_data = get_weather(city_name, API_KEY)
    print(weather_data)