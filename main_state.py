import random
import json
import os

from pico2d import *

import game_framework
import title_state


name = "MainState"

pac = None
mons = None
font = None

class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(400,30)


class Back1:
    def __init__(self):
        self.image = load_image('back1.png')

    def draw(self):
        self.image.draw(400,30)

class Mons1:
    def __init__(self):
        self.image = load_image('mons.png')

    def draw(self):
        self.image.draw(400.30)

class Pac:
    def __init__(self):
        self.x, self.y = 300,318
        self.image == load_image('Pac-Man.png')
