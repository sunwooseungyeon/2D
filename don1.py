import random

from pico2d import *

class Don1:
    def __init__(self):
        self.image = load_image('don1.png')

    def draw(self):
        self.image.draw(60, 35)

    def update(self, frame_time):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


