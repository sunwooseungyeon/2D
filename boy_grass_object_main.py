from pico2d import *


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
        self.image = load_image('mons1.png')

    def draw(self):
        self.image.draw(400, 300)


class Pac:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('pac.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.type == SDLK_ESCAPE:
            running = False


# fill here for boy, grass
running = True

def enter():
    pass


def exit():
    pass


def update():
    pass


def draw():
    pass


def main():
    pass


# fill here


