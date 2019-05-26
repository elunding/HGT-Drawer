import logging
import fire

from logging.config import fileConfig
from gmalthgtparser import HgtParser
from PIL import Image

hgt_file = 'hgt_files/N00W177.hgt'

fileConfig('logging_config.ini')
logger = logging.getLogger(__name__)


class HgtDrawer(object):
    def __init__(self):
        self.hgt_file = hgt_file


    def get_elevation(self):
        with HgtParser(self.hgt_file) as parser:
            for elevation in parser.get_value_iterator():
                print(elevation)

'''
def get_image(self):
    image = Image.new("RGB", (,))
'''


if __name__ == '__main__':
    fire.Fire(HgtDrawer)