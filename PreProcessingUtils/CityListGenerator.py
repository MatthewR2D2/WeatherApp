import pandas as pd
from BasicWeatherBot import BasicWeatherConditions
from Config import CITY_LIST
import numpy as np


class City_Information_Generator:
    def __init__(self, city_list):
        self.city_frame = pd.read_csv(city_list)

    def get_city_names(self):
        large_cities = []
        for index, row in self.city_frame.iterrows():
            large_cities.append(row['City'])
        return large_cities

    def city_list_information(self, city_names):
        city_infomration = []
        for city in city_names:
            print("Looking for ", city)
            basic_weather = BasicWeatherConditions(city)
            _, _, city_info = basic_weather.process_result()
            name, long, lat = city_info

            city_infomration.append([name, long, lat])
        return city_infomration


if __name__ == '__main__':
    city_gen = City_Information_Generator(CITY_LIST)

    cities = city_gen.get_city_names()
    city_location_info = city_gen.city_list_information(cities)
    print(city_location_info)
    # Save the data for use in other mapping information
    np.savetxt("../Data/MajorCityInfo.csv", city_location_info, delimiter=",", fmt='%s')


