import random

from pico2d import *

class Don1:
    def __init__(self):
        self.image = load_image('don1.png')

    def draw(self):
        self.image.draw(60, 35)
        self.image.draw(95, 35)
        self.image.draw(130, 35)



    def update(self, frame_time):
        pass

