import pygame as pg
import random
import numpy as np
import cv2
import objects
from constants import *

pg.init()


class World:
    def __init__(self, main):
        self.main = main
        self.player = objects.Player(self, [0, 0])
        self.ground = objects.Ground(150, 50, 200)

    def draw(self):
        for x, y in np.ndenumerate(self.ground.lines[self.player.pos[0]:WWIDTH+self.player.pos[0]]):
            y = y.split(' ')
            pg.draw.line(self.main.surf, (0, 0, 0), (x[0], int(y[0])), (x[0], int(y[1])), 1)

    def update(self):
        self.player.move()


class Main:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pg.Surface(WSIZE)
        self.running = True
        self.world = World(self)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont(None, FSIZE)
        self.input_ = [False, '']
        # self.console = objects.Console(self)

    @staticmethod
    def input(surface):
        pg.key.start_text_input()
        pg.key.set_text_input_rect(surface)

    def input_check(self):
        if self.input_[0] is False: print(self.input_[1])

    def run(self):
        alt = False
        while self.running:
            self.surf.fill((255, 255, 255))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.TEXTINPUT:
                    self.input_[1] = event.text
                elif event.type == pg.TEXTEDITING:
                    self.input_[0] = True
                    self.input_[1] = event.text
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_LALT:
                        alt = True
                    elif event.key == pg.K_F4 and alt:
                        self.running = False
                    elif event.key == pg.K_r:
                        self.screen.fill((128, 255, 128))
                        pg.display.update()
                        self.world.ground.generate(random.randint(0, 999999999999999999))
                    elif event.key == pg.K_KP_ENTER:
                        pg.key.stop_text_input()
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_LALT: alt = False
            self.world.update()
            self.world.draw()
            screen.blit(pg.transform.flip(self.surf, False, True), (0, 0))
            self.clock.tick()
            fps = round(self.clock.get_fps())
            fps = self.font.render(str(fps), False, (0, 0, 0))
            screen.blit(fps, (10, 10))
            pg.display.update()


if __name__ == '__main__':
    screen = pg.display.set_mode(WSIZE)
    main = Main(screen)
    main.run()
    pg.quit()
