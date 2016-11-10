import random

from pico2d import *

class Mons3:

    image = None

    def __init__(self):
        self.x, self.y = 53,483
        if Mons3.image == None:
            Mons3.image = load_image('mons3.png')
        self.dir = 2

    def update(self, frame_time):
        self.x += self.dir
        if self.x >= 750:
            self.dir = -2
        elif self.x <= 53:
            self.dir = 2

    def draw(self):
        self.image.draw(self.x, self.y)

    # fill here
    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
