import geopandas as gpd
import matplotlib.pyplot as plt
from Config import WORLD_SHAPEFILE, MAJOR_CITIES_INFO
from BasicWeatherBot import BasicWeatherConditions
import pandas as pd
import numpy as np

class BasicWorldMap:
    def __init__(self):
        self.world_map = gpd.read_file(WORLD_SHAPEFILE) # Make sure to have all accompany ESRI files in the same data folder

    def simple_map_plot(self):
        self.world_map.plot()
        plt.show()

    def city_map_plot(self, long, lat):
        self.world_map.plot()
        plt.scatter(long, lat, s=12, c='g')
        plt.show()

    def process_text_temp(self, temp):
        string = "Current Temp = {} C \n Feels Like {} C \n Min {} C Max {} C \n Pressure {} hPa \n Humidity {}%".format(temp[0],
                                                                                                                        temp[1],
                                                                                                                        temp[2],
                                                                                                                        temp[3],
                                                                                                                        temp[4],
                                                                                                                        temp[5])
        return string

    def process_text_weather(self, weather):
        #weather_base_conditions, weather_description, weather_icon, viz, wind_speed, wind_dir
        string = "Current Base Conditions = {}\n Description {}\n Visability {} m \n Wind Speed {} mps \n Wind Dir {}%".format(weather[0],
                                                                                                                        weather[1],
                                                                                                                        weather[3],
                                                                                                                        weather[4],
                                                                                                                        weather[5])
        return string

    def weather_map_plot(self, temp, weather, long, lat):
        self.world_map.plot()
        string_temp = self.process_text_temp(temp)
        string_weather = self.process_text_weather(weather)
        plt.scatter(long, lat, s = 12, c='g')
        plt.figtext(0, 0.05, string_temp, horizontalalignment='left')
        plt.figtext(0.99, 0.05, string_weather, horizontalalignment='right')

        plt.xticks([], [])
        plt.yticks([], [])
        plt.show()


if __name__ == '__main__':
    # Basic usage for wether data
    city_name = input("Enter city name : ")
    basic_weather = BasicWeatherConditions()
    weather = basic_weather.get_weather_report(city_name)
    temp, weather, city_info = basic_weather.process_result(weather)
    name, long, lat = city_info
    # Display World Map
    world_map = BasicWorldMap()
    #world_map.city_map_plot()
    world_map.weather_map_plot(temp, weather, long, lat)
    cities = pd.read_csv(MAJOR_CITIES_INFO)





