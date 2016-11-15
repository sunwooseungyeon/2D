import game_framework
from pico2d import *

import title_state


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('kpu_credit.png')
    pass


def exit():
    global image
    del(image)
    close_canvas()

    pass


def update(frame_time):
    global logo_time

    if(logo_time > 2.5):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01
    pass


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass




def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass




