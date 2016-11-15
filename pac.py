import random

from pico2d import *

class Pac:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, UP_RUN, DOWN_RUN, UP_STAND, DOWN_STAND = 0, 1, 2, 3, 4, 5, 6, 7

    def __init__(self):
        self.x, self.y = 50,318
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.RIGHT_STAND
        if Pac.image == None:
            Pac.image = load_image('Pac-Man.png')


    def update(self, frame_time):
        self.frame = (self.frame + 1) % 1
        if self.state == self.RIGHT_RUN:
            self.x = min(800, self.x + 2)
        if self.state == self.LEFT_RUN:
            self.x = max(0, self.x - 2)
        if self.state == self.UP_RUN:
            self.y = min(800,self.y + 2)
        if self.state == self.DOWN_RUN:
            self.y = max(0, self.y - 2)


    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 13, self.y - 13, self.x + 11, self.y + 11
        pass

    def handle_event(self, event):
        print(event.key, event.type)
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in(self.RIGHT_RUN, self.RIGHT_STAND, self.LEFT_STAND, self.UP_RUN, self.UP_STAND,self.DOWN_RUN, self.DOWN_STAND):
                self.state = self.LEFT_RUN

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
             if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN, self.UP_RUN,self.UP_STAND,self.DOWN_RUN,self.DOWN_STAND):
                 self.state = self.RIGHT_RUN

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.state in (self.RIGHT_STAND,self.LEFT_STAND,self.RIGHT_RUN,self.LEFT_RUN,self.UP_STAND,self.DOWN_RUN, self.DOWN_STAND):
                self.state = self.UP_RUN

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state in (self.RIGHT_STAND, self.RIGHT_RUN, self.LEFT_STAND, self.LEFT_RUN, self.UP_RUN, self.UP_STAND, self.DOWN_STAND):
                self.state = self.DOWN_RUN


        if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.DOWN_RUN,):
                self.state = self.DOWN_STAND

        if (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.UP_RUN,):
                self.state = self.UP_STAND

        if (event.type, event.key)  == (SDL_KEYUP, SDLK_LEFT):
             if self.state in (self.LEFT_RUN,):
                 self.state = self.LEFT_STAND

        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
             if self.state in (self.RIGHT_RUN,):
                 self.state = self.RIGHT_STAND
