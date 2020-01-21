from pygame import *
from pygame.locals import * 
import sys
from random import randint

init()
FPS = 60

class Bomb(sprite.Sprite):
    pictures = ['bomb_01.png', 'bomb_02.png', 'bomb_03.png', 'bomb_04.png']
    w = 44
    h = 42

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        sprite.Sprite.__init__(self)

        self.rect = Rect(self.x, self.y, self.w, self.h)

        self.frames = []
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
        # self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in self.pictures]

        self.frame_act = 0
        self.num_frames = len(self.frames)

        self.current_time = 0
        self.animation_time = FPS//60

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.frame_act += 1
            if self.frame_act == self.num_frames:
                self.frame_act = 0
            # self.frame_act = (self.frame_act + 1) % self.num_frames

    @property
    def image(self):
        return self.frames[self.frame_act]



class Robot(sprite.Sprite):
    speed = 5
    pictures = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']
    w = 64
    h = 68

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        sprite.Sprite.__init__(self)

        self.rect = Rect(self.x, self.y, self.w, self.h)

        self.frames = []
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
        # self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in self.pictures]

        self.frame_act = 0
        self.num_frames = len(self.frames)

    def change_frame(self):
        self.frame_act += 1
        if self.frame_act == self.num_frames:
            self.frame_act = 0
        # self.frame_act = (self.frame_act + 1) % self.num_frames

    def go_up(self):
        '''
        if self.y > 0:
            self.y -= self.speed
        '''
        self.rect.y = max(0, self.rect.y - self.speed)
        self.change_frame()

    def go_down(self):
        self.rect.y = min(600, self.rect.y + self.speed)
        self.change_frame()

    def go_left(self):
        self.rect.x = max(0, self.rect.x - self.speed)
        self.change_frame()

    def go_right(self):
        self.rect.x = min(800, self.rect.x + self.speed)
        self.change_frame()

    @property
    def image(self):
        return self.frames[self.frame_act]


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

            self.screen.fill(self.background_color)
            '''
            self.screen.blit(self.robot.image, self.robot.position)
            for b in self.bombas:
                b.update(dt)
                self.screen.blit(b.image, b.position)
            '''

            self.all_group.update(dt)
            self.all_group.draw(self.screen)

            display.flip()


if __name__ == '__main__':
    game = Game()
    game.mainloop()
