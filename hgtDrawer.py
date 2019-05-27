import logging

import numpy as np
import matplotlib.pyplot as plt

from logging.config import fileConfig
from gmalthgtparser import HgtParser


fileConfig('logging_config.ini')
logger = logging.getLogger(__name__)


class HgtDrawer(object):

    def __init__(self, hgt_file, azimuth_angle, altitude_angle):
        self.hgt_file = hgt_file
        self.azimuth_angle = azimuth_angle
        self.altitude_angle = altitude_angle

    def get_elevation(self):
        logger.info("Obteniendo arreglo de elevacion...")
        with HgtParser(self.hgt_file) as parser:
            for elevation in parser.get_sample_iterator(1201, 1201):
                elevation_array = np.array(elevation[4])
        self.get_image(
            elevation_array=elevation_array,
            azimuth_angle=self.azimuth_angle,
            altitude_angle=self.altitude_angle,
        )

    @staticmethod
    def get_image(elevation_array, azimuth_angle, altitude_angle):
        logger.info("Renderizando imagen...")
        x, y = np.gradient(elevation_array)
        pendant = np.pi/2. - np.arctan(np.sqrt(x*x + y*y))
        aspect = np.arctan2(-x, y)

        azimuth_rad = azimuth_angle*np.pi / 180.
        altitude_rad = altitude_angle*np.pi / 180.
        shaded = np.sin(altitude_rad) * np.sin(pendant) + np.cos(altitude_rad) * np.cos(pendant) * np.cos(azimuth_rad - aspect)
        value = 255*(shaded + 1)/2
        plt.imshow(value, cmap='Greys')
        plt.show()


if __name__ == '__main__':
    drawer = HgtDrawer(
        hgt_file='hgt_files/S33W070.hgt',
        azimuth_angle=315,
        altitude_angle=45,
    )
    drawer.get_elevation()
