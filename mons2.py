import random

from pico2d import *

class Mons2:

    image = None

    def __init__(self):
        self.x, self.y = 53,35
        if Mons2.image == None:
            Mons2.image = load_image('mons2.png')
        self.dir = 3

    def update(self, frame_time):
        self.x += self.dir
        if self.x >= 750:
            self.dir = -3
        elif self.x <= 53:
            self.dir = 3

    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
