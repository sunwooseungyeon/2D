from pico2d import *

import game_framework


from pac import Pac # import Boy class from boy.py
from mons1 import Mons1
from mons2 import Mons2
from mons3 import Mons3
from back1 import Back1
from back import Back




name = "collision"

pac = None
mons1 = None
back = None

def create_world():
    global pac, mons1, mons2, mons3, back, back1
    pac = Pac()
    mons1 = Mons1()
    mons2 = Mons2()
    mons3 = Mons3()
    back = Back()
    back1 = Back1()


    pass


def destroy_world():
    global pac, mons1, mons2, mons3, back, back1

    del(pac)
    del(mons1)
    del(mons2)
    del(mons3)
    del(back)
    del(back1)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pac.handle_event(event)



def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

    pass


def update(frame_time):
    pac.update(frame_time)
    mons1.update(frame_time)
    mons2.update(frame_time)
    mons3.update(frame_time)
    #for mons1 in mons1:
       #ball.update(frame_time)

    # fill here
    pass



def draw(frame_time):
    clear_canvas()
    back.draw()
    back1.draw()
    pac.draw()
    mons1.draw()
    mons2.draw()
    mons3.draw()


    #for ball in balls:
        #ball.draw()

    # fill here
    pass

    update_canvas()






