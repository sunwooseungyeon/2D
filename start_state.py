import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas()
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()


def update():
    global logo_time

    if(logo_time > 1.0):            # 1.0 보다 크면 게임 프레임워크 큇이 실행
        logo_time = 0               #  로고 타임은 0부터 시작해서 로고 타임 0.01씩 증가 한다.
        #game_framework.quit()
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




