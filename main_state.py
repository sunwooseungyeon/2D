import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

pac = None
mons = None
back = None
back1 = None
font = None

class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(400,300)

class Back1:
    def __init__(self):
        self.image = load_image('back1.png')

    def draw(self):
        self.image.draw(400,300)

class Pac:
    def __init__(self):
        self.x, self. y = 0, 90
        self.image = load_image('Pac-Man.png')
        self.dir = 1

    def update(self):
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
       pass


class Mons:
    def __init__(self):


def enter():
    global pac, mons
    pac = Pac()
    mons = Mons()

def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events():
    pass

def update():
    pass

def draw():
    pass