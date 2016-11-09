import random

from pico2d import *

class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(400, 300)

    # fill here

