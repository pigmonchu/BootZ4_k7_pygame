from pygame import *
from pygame.locals import * 
import sys

init()

class Robot:
    speed = 5
    images = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image.load('resources/robot_r01.png').convert_alpha()

    def go_up(self):
        '''
        if self.y > 0:
            self.y -= self.speed
        '''
        self.y = max(0, self.y - self.speed)

    def go_down(self):
        self.y = min(600, self.y + self.speed)

    def go_left(self):
        self.x = max(0, self.x - self.speed)

    def go_right(self):
        self.x = min(800, self.x + self.speed)

    def position(self):
        return self.x, self.y

screen = display.set_mode((800, 600))
display.set_caption('Hola mundo!')
background_color = (150, 150 ,222)

robot = Robot(400, 300)

while True:

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                robot.go_up()
            if ev.key == K_DOWN:
                robot.go_down()
            if ev.key == K_LEFT:
                robot.go_left()
            if ev.key == K_RIGHT:
                robot.go_right()

    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        robot.go_up()
    if keys_pressed[K_DOWN]:
        robot.go_down()
    if keys_pressed[K_RIGHT]:
        robot.go_right()
    if keys_pressed[K_LEFT]:
        robot.go_left()

    print(robot.x, robot.y)

    

    screen.fill(background_color)
    screen.blit(robot.image, robot.position())

    display.flip()
