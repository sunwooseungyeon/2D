import random
import json
import os


from pico2d import *

import game_framework
import title_state

from don1 import Don1
from pac import Pac
from mons1 import Mons1
from mons2 import Mons2
from mons3 import Mons3
from back1 import Back1
from back import Back
from don2 import Don2
from don3 import Don3
from don4 import Don4
from don5 import Don5
from don6 import Don6
from don7 import Don7
from don8 import Don8
from don9 import Don9
from don10 import Don10
from don11 import Don11
from don12 import Don12
from don13 import Don13
from don14 import Don14
from don15 import Don15
from don16 import Don16
from don17 import Don17
from don18 import Don18
from don19 import Don19
from don20 import Don20
from don21 import Don21
from don22 import Don22
from don23 import Don23
from don24 import Don24
from don25 import Don25
from don26 import Don26
from don27 import Don27
from don28 import Don28

name = "collision"

pac = None
mons1 = None
back = None

def create_world():
    global don024, don025, don026, don027, don028,don023, don022, don021, don, don014, don015, don016, don017, don018, don019, don020, don012, don013, pac, mons13, back, back1, don1,mons, don02, don03,don04, don05, don06, don07, don08, don09, don010, don011, mons12

    don024 = [Don24() for i in range(1)]
    don025 = [Don25() for i in range(1)]
    don026 = [Don26() for i in range(1)]
    don027 = [Don27() for i in range(1)]
    don028 = [Don28() for i in range(1)]

    don023 = [Don23() for i in range(1)]
    don022 = [Don22() for i in range(1)]
    don021 = [Don21() for i in range(1)]

    don012 = [Don12() for i in range(1)]
    don013 = [Don13() for i in range(1)]
    don014 = [Don14() for i in range(1)]
    don015 = [Don15() for i in range(1)]
    don016 = [Don16() for i in range(1)]
    don017 = [Don17() for i in range(1)]
    don018 = [Don18() for i in range(1)]
    don019 = [Don19() for i in range(1)]
    don020 = [Don20() for i in range(1)]

    don04 = [Don4() for i in range(1)]
    don05 = [Don5() for i in range(1)]
    don06 = [Don6() for i in range(1)]
    don07 = [Don7() for i in range(1)]
    don08 = [Don8() for i in range(1)]
    don09 = [Don9() for i in range(1)]
    don010 = [Don10() for i in range(1)]
    don011 = [Don11() for i in range(1)]
    don03 = [Don3() for i in range(1)]
    don02 =[Don2() for i in range(1)]
    don = [Don1() for i in range(1)]
    pac = Pac()
    mons = [Mons1() for i in range(1)]
    mons12 = [Mons2() for i in range(1)]
    mons13 = [Mons3() for i in range(1)]
    back = Back()
    back1 = Back1()

    pass


def destroy_world():
    global don024,don025, don026, don027, don028, don023, don021, don014, don015, don016, don017, don018, don019, don020, pac, mons1, back, back1, don02, don03, don04, don05, don06, don07, don08, don09, don010, don011, don012, don013

    del (don024)
    del (don025)
    del (don026)
    del (don027)
    del (don028)

    del(don023)
    del(don021)

    del(don015)
    del(don016)
    del(don017)
    del(don018)
    del(don019)
    del(don020)
    del(don014)
    del(don012)
    del(don013)

    del(don04)
    del(don05)
    del(don06)
    del(don07)
    del(don08)
    del(don09)
    del(don010)
    del(don011)


    del(don03)

    del(don02)

    del(pac)
    del(mons1)
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
                game_framework.push_state(title_state)
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

    for don1 in don:
        don1.update(frame_time)

    for don1 in don:
        if collide(pac, don1):
            don.remove(don1)

    for don2 in don02:
        don2.update(frame_time)

    for don2 in don02:
        if collide(pac,don2):
            don02.remove(don2)

    for don3 in don03:
        don3.update(frame_time)

    for don3 in don03:
        if collide(pac, don3):
            don03.remove(don3)

    for don4 in don04:
        don4.update(frame_time)

    for don4 in don04:
        if collide(pac, don4):
            don04.remove(don4)

    for don5 in don05:
        don5.update(frame_time)

    for don5 in don05:
        if collide(pac, don5):
            don05.remove(don5)

    for don6 in don06:
        don6.update(frame_time)

    for don6 in don06:
        if collide(pac, don6):
            don06.remove(don6)

    for don7 in don07:
        don7.update(frame_time)

    for don7 in don07:
        if collide(pac, don7):
            don07.remove(don7)

    for don8 in don08:
        don8.update(frame_time)

    for don8 in don08:
        if collide(pac, don8):
            don08.remove(don8)

    for don9 in don09:
        don9.update(frame_time)

    for don9 in don09:
        if collide(pac, don9):
            don09.remove(don9)

    for don10 in don010:
        don10.update(frame_time)

    for don10 in don010:
        if collide(pac, don10):
            don010.remove(don10)

    for don11 in don011:
        don11.update(frame_time)

    for don11 in don011:
        if collide(pac, don11):
            don011.remove(don11)

    for don12 in don012:
        don12.update(frame_time)

    for don12 in don012:
        if collide(pac, don12):
            don012.remove(don12)

    for don13 in don013:
        don13.update(frame_time)

    for don13 in don013:
        if collide(pac, don13):
            don013.remove(don13)

    for don14 in don014:
        don14.update(frame_time)

    for don14 in don014:
        if collide(pac, don14):
            don014.remove(don14)

    for don15 in don015:
        don15.update(frame_time)

    for don15 in don015:
        if collide(pac, don15):
            don015.remove(don15)

    for don16 in don016:
        don16.update(frame_time)

    for don16 in don016:
        if collide(pac, don16):
            don016.remove(don16)

    for don17 in don017:
        don17.update(frame_time)

    for don17 in don017:
        if collide(pac, don17):
            don017.remove(don17)

    for don18 in don018:
        don10.update(frame_time)

    for don18 in don018:
        if collide(pac, don18):
            don018.remove(don18)

    for don19 in don019:
        don19.update(frame_time)

    for don19 in don019:
        if collide(pac, don19):
            don019.remove(don19)

    for don20 in don020:
        don20.update(frame_time)

    for don20 in don020:
        if collide(pac, don20):
            don020.remove(don20)

    for don21 in don021:
        don21.update(frame_time)

    for don21 in don021:
        if collide(pac, don21):
            don021.remove(don21)

    for don22 in don022:
        don22.update(frame_time)

    for don22 in don022:
        if collide(pac, don22):
            don022.remove(don22)

    for don23 in don023:
        don23.update(frame_time)

    for don23 in don023:
        if collide(pac, don23):
            don023.remove(don23)

    for don24 in don024:
        don24.update(frame_time)

    for don24 in don024:
        if collide(pac, don24):
            don024.remove(don24)

    for don25 in don025:
        don25.update(frame_time)

    for don25 in don025:
        if collide(pac, don25):
            don025.remove(don25)

    for don26 in don026:
        don26.update(frame_time)

    for don26 in don026:
        if collide(pac, don26):
            don026.remove(don26)

    for don27 in don027:
        don27.update(frame_time)

    for don27 in don027:
        if collide(pac, don27):
            don027.remove(don27)

    for don28 in don028:
        don28.update(frame_time)

    for don28 in don028:
        if collide(pac, don28):
            don028.remove(don28)







    for mons1 in mons:
        mons1.update(frame_time)

    for mons1 in mons:
        if collide(pac, mons1):
            mons.remove(mons1)

    for mons2 in mons12:
        mons2.update(frame_time)

    for mons3 in mons13:
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

    for don1 in don:
        don1.draw()

    for don2 in don02:
        don2.draw()

    for don3 in don03:
        don3.draw()

    for don4 in don04:
        don4.draw()

    for don5 in don05:
        don5.draw()

    for don6 in don06:
        don6.draw()

    for don7 in don07:
        don7.draw()

    for don8 in don08:
        don8.draw()

    for don9 in don09:
        don9.draw()

    for don10 in don010:
        don10.draw()

    for don11 in don011:
        don11.draw()

    for don12 in don012:
        don12.draw()

    for don13 in don013:
        don13.draw()

    for don14 in don014:
        don14.draw()

    for don15 in don015:
        don15.draw()

    for don16 in don016:
        don16.draw()

    for don17 in don017:
        don17.draw()

    for don18 in don018:
        don18.draw()

    for don19 in don019:
        don19.draw()

    for don20 in don020:
        don20.draw()

    for don21 in don021:
        don21.draw()

    for don22 in don022:
        don22.draw()

    for don23 in don023:
        don23.draw()

    for don24 in don024:
        don24.draw()

    for don25 in don025:
        don25.draw()

    for don26 in don026:
        don26.draw()

    for don27 in don027:
        don27.draw()

    for don28 in don028:
        don28.draw()


    for mons1 in mons:
        mons1.draw()

    for mons2 in mons12:
        mons2.draw()

    for mons3 in mons13:
        mons3.draw()


    pac.draw_bb()





    #for ball in balls:
        #ball.draw()

    # fill here
    pass

    update_canvas()






