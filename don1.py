import random

from pico2d import *

class Don1:
    def __init__(self):
        self.image = load_image('don1.png')

    def draw(self):
        self.image.draw(60, 88)
        self.image.draw(95, 88)
        self.image.draw(130, 88)
        self.image.draw(165, 88)
        self.image.draw(200, 88)
        self.image.draw(400, 310)
        self.image.draw(430, 310)
