import requests

def get_current_weather(api_key, location):
    url = f"http://api.weatherapi.com/v1/current.json"
    params = {
        'key': api_key,
        'q': location,
        'aqi': 'no'  # Set to 'yes' if you want air quality data
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def main(location = 'Ernakulam'):
    # Replace 'your_api_key_here' with your actual WeatherAPI key
    api_key = '1a35e78f85104a46abd50748242612'

    weather_data = get_current_weather(api_key, location)
    print(weather_data)
    return weather_data
# print(weather_data['location'])
# # print(weather_data['current'])
# # print(weather_data['current']['condition']['text'])
