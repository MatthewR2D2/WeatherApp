# using openweathermap api
import requests
from Config import API_KEY, BASE_URL
from WeatherUtils import process_weather_conditions, process_weather_temperature, process_weather_location


class BasicWeatherConditions:
    def __init__(self):
        self.complete_url = BASE_URL + "appid=" + API_KEY + "&q="

    def get_weather_report(self, city_name):
        request = self.complete_url + city_name
        response = requests.get(request)
        weather_report = response.json()
        return weather_report

    def print_temperature(self, temp):
        print(" Temperature: " +
              str(temp[0]) + ' C' +
              "\n Feels Like: " +
              str(temp[1]) + ' C' +
              "\n Minimum Temperature: " +
              str(temp[2]) + ' C' +
              "\n Maximum Temperature: " +
              str(temp[3]) + ' C' +
              "\n Atmospheric Pressure: " +
              str(temp[4]) + ' hPa' +
              "\n Humidity: " +
              str(temp[5]) + '%')

    def print_basic_conditions(self, weather):
        print(" Weather Conditions: " +
              str(weather[0]) +
              "\n Basic Description: " +
              str(weather[1]) +
              "\n Vizability: " +
              str(weather[2]) +
              "\n Wind Speed = " +
              str(weather[3]) +
              "\n Wind Direction = " +
              str(weather[4]))

    def process_result(self, weather_report):
        # "404" = city is not found
        if weather_report["cod"] != "404":
            # store the value corresponding for current temperature pressure and humidity
            current_temperature, feels_like, min_temerature, max_temperature, current_pressure, current_humidiy = process_weather_temperature(
                weather_report)
            temperature_values = [current_temperature, feels_like, min_temerature, max_temperature, current_pressure,
                                  current_humidiy]
            weather_base_condition, weather_description, weather_icon, vizability, wind_speed, wind_dir = process_weather_conditions(
                weather_report)
            current_weather_conditions = [weather_base_condition, weather_description, weather_icon, vizability,
                                          wind_speed, wind_dir]
            name, long, lat = process_weather_location(weather_report)
            city_info = [name, long, lat]
            return temperature_values, current_weather_conditions, city_info
        else:
            print(" City Not Found ")
            new_name = input("Enter city name : ")
            self.process_result(self.get_weather_report(new_name))

'''
Tester Code
'''
if __name__ == '__main__':
    # Basic usage for wether data
    basic_weather = BasicWeatherConditions()
    city_name = input("Enter city name : ")
    weather = basic_weather.get_weather_report(city_name)
    temp, weather, city_info = basic_weather.process_result(weather)
    print(" The city {} at Long {} and Lat {}".format(city_info[0], city_info[1], city_info[2]))
    basic_weather.print_temperature(temp)
    basic_weather.print_basic_conditions(weather)
