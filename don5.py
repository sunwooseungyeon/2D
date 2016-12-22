import random

from pico2d import *

class Don5:
    def __init__(self):
        self.x, self.y = 360, 35
        self.image = load_image('don1.png')

    def draw(self):
        self.image.draw(self.x, self.y)




    def update(self, frame_time):
        pass



    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15
