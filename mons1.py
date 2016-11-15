import random

from pico2d import *

class Mons1:

    image = None

    def __init__(self):
        self.x, self.y = 350,315
        if Mons1.image == None:
            Mons1.image = load_image('mons1.png')
        self.dir = 1

    def update(self, frame_time):
        self.x += self.dir
        if self.x >= 450:
            self.dir = -1
        elif self.x <= 350:
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    # fill here
    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20



