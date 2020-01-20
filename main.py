from pygame import *
from pygame.locals import * 
import sys

init()

screen = display.set_mode((800, 600))
display.set_caption('Hola mundo!')
background_color = (30, 46 ,222)

while True:

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

        #... Procesar el resto de eventos
        screen.fill(background_color)

        display.flip()
