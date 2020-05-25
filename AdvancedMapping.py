from BasicMapping import BasicWorldMap
from Config import MAJOR_CITIES_INFO
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.text import Annotation
import seaborn as sns
import numpy as np


class AdvancedMapping(BasicWorldMap):
    def __init__(self):
        BasicWorldMap.__init__(self)
        cities = pd.read_csv(MAJOR_CITIES_INFO)
        self.major_cities = cities.to_numpy()

    def major_city_map_plot(self):
        self.world_map.plot()
        # plt.scatter(long, lat, s=12, c='g')
        for city in self.major_cities:
            name, long, lat = city
            plt.scatter(long, lat, s=6, c='g')
        plt.show()

if __name__ == '__main__':
    # set the default style
    sns.set()
    # define two colors, just to enrich the example
    labels_color_map = {0: '#20b2aa', 1: '#ff7373'}

    amservice = AdvancedMapping()
    amservice.major_city_map_plot()



