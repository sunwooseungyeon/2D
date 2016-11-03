import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

pac = None
back = None
back1 = None
mons1 = None
font = None



class Back:
    def __init__(self):
        self.image = load_image('back.png')

    def draw(self):
        self.image.draw(400, 300)

class Back1:
    def __init__(self):
        self.image = load_image('back1.png')

    def draw(self):
        self.image.draw(400, 300)

class Mons1:
    def __init__(self):
        self.x , self.y = 350, 315
        self.frame = 0
        self.image = load_image('mons1.png')
        self.dir = 1

    def update(self):
        self.x += self.dir
        if self.x >= 450:
            self.dir = -1
        elif self.x <= 350:
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)


class Pac:

    def __init__(self):
        self.x, self.y = 300, 318
        self.frame = 0
        self.image = load_image('Pac-Man.png')
        self.dir = 1

    def update(self):
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global back,back1,mons1,pac
    back = Back()
    back1 = Back1()
    mons1 = Mons1()
    pac = Pac()
    pass


def exit():
    global back, back1, mons1, pac
    del(back)
    del(back1)
    del(mons1)
    del(pac)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
    pass


def update():
    pac.update()
    mons1.update()
    pass


def draw():
    clear_canvas()
    back.draw()
    back1.draw()
    mons1.draw()
    pac.draw()
    update_canvas()
    pass





