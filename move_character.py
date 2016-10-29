
from pico2d import *

def handle_events():
    global running
    global x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x = x + 10
            elif event.key == SDLK_LEFT:
                x = x - 10
            elif event.key == SDLK_UP:
                y = y + 10
            elif event.key == SDLK_DOWN:
                y = y - 10
            elif event.key == SDLK_ESCAPE:
                running = False

open_canvas()
back = load_image('back.png')
back1 = load_image('back1.png')
pac = load_image('Pac-Man.png')
mons = load_image('mons.png')

running = True
x = 30
y = 318
z = 350
while(running):
    clear_canvas()
    back.draw(400,300)
    back1.draw(400,300)
    pac.draw(x,y)
    mons.draw(z,318)
    update_canvas()

    delay(0.01)
    handle_events()

close_canvas()
