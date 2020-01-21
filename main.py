from pygame import *
from pygame.locals import * 
import sys
from random import randint
from entities import *

init()

class Game:
    clock = time.Clock()

    def __init__(self):
        self.screen = display.set_mode((800, 600))
        display.set_caption('Hola mundo!')

        self.background_color = (150, 150 ,222)

        self.player_group = sprite.Group()
        self.bombs_group = sprite.Group()
        self.all_group = sprite.Group()

        self.robot = Robot(400, 300)
        self.player_group.add(self.robot)

        for i in range(5):
            bomb = Bomb(randint(0, 750), randint(0, 550))
            self.bombs_group.add(bomb)

        self.all_group.add(self.robot, self.bombs_group)

    def gameOver(self):
        quit()
        sys.exit()

    def handleEvents(self):
        for ev in event.get():
            if ev.type == QUIT:
                self.gameOver()

            if ev.type == KEYDOWN:
                if ev.key == K_UP:
                    self.robot.go_up()
                if ev.key == K_DOWN:
                    self.robot.go_down()
                if ev.key == K_LEFT:
                    self.robot.go_left()
                if ev.key == K_RIGHT:
                    self.robot.go_right()

        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.robot.go_up()
        if keys_pressed[K_DOWN]:
            self.robot.go_down()
        if keys_pressed[K_RIGHT]:
            self.robot.go_right()
        if keys_pressed[K_LEFT]:
            self.robot.go_left()


    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)

            self.handleEvents()

            #Controlar si el robot toca una bomba
            if self.robot.comprobarToques(self.bombs_group) == 0:
                self.gameOver()

            self.screen.fill(self.background_color)

            self.all_group.update(dt)
            self.all_group.draw(self.screen)

            display.flip()


if __name__ == '__main__':
    game = Game()
    game.mainloop()
