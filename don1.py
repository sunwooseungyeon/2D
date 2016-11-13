import random

from pico2d import *

class Don1:
    def __init__(self):
        self.image = load_image('don1.png')

    def draw(self):
        self.image.draw(400, 310)
        self.image.draw(430, 310)
