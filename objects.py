import pygame as pg
import numpy as np
import math as m
import random
from constants import *


class Ground:
    def __init__(self, medium_height, min_height, max_height):
        self.meh = medium_height
        self.mih = min_height
        self.mah = max_height
        self.lines = np.array(str(self.meh) + ' ' + str(-self.meh))
        self.y = self.meh
        self.ud = random.choice((-1, 1))
        self.size = 5 * self.ud
        # self.lines = np.linspace(self.meh, self.meh, 1000, dtype=np.int32)
        self.generate(random.randint(0, 9999999999999999))

    # def generate(self, seed):
    #     self.lines = np.array(str(self.meh) + ' ' + str(self.mih - self.meh))
    #     random.seed(seed)
    #     rup = random.randint(-30, 30)
    #     rne = random.randint(40, 80)
    #     rmu = random.randint(20, 55)
    #     # det = self.det - 1
    #     for x in np.arange(0, 2000, 1):
    #         # det += 1
    #         ao = m.tanh(m.radians(x // 3 + rup)) * int(rmu) - self.mih + 100
    #         rup += random.randint(-2, 1)
    #         if x % rne:
    #             if random.randint(0, 100) < 8: rup -= random.randint(0, 4)
    #             rne = random.randint(40, 80)
    #             if random.choice((False, False, True)): rmu += random.randint(-3, 3)
    #         self.lines = np.append(self.lines, (str(int(ao)) + ' ' + str(self.mih - int(ao))))

    def generate(self, seed):
        random.seed(seed)
        self.lines = np.array(str(self.meh) + ' ' + str(-self.meh))
        self.y = self.meh
        random.seed(seed)
        self.ud = random.choice((-1, 1))
        self.size = 5 * self.ud
        for _ in range(10):
            random.choice((self.g1, self.g2, self.g3))()

    def g1(self):
        self.size = min(self.size, 20)
        for _ in np.arange(0, 2000, 1):
            self.y += self.size if random.randint(0, 100) > 70 and self.y > self.meh else self.size // 10
            self.size += self.ud
            self.ud = -self.ud if abs(
                self.size) > 20 or self.y + self.size < self.mih and self.ud < 0 or self.y + self.size > self.mah and self.ud > 0 or random.randint(
                0, 20) < self.size else self.ud
            self.lines = np.append(self.lines, (str(self.y) + ' ' + str(-self.y)))

    def g2(self):
        self.size = min(self.size, 8)
        for _ in np.arange(0, 2000, 1):
            chance = random.randint(0, 100)
            if chance > 99:
                self.y += self.size // 2
            elif chance > 80:
                self.y += self.size // 4
            self.size += self.ud
            self.ud = -self.ud if abs(self.size) > 8 or self.y + self.size < self.mih - 8 and self.ud < 0 or\
                                self.y + self.size > self.mah and self.ud > 0 or random.randint(0, 8) < self.size else self.ud
            self.lines = np.append(self.lines, (str(self.y) + ' ' + str(-self.y)))

    def g3(self):
        self.size = min(self.size, 8)
        for _ in np.arange(0, 2000, 1):
            chance = random.randint(0, 100)
            if chance > 99:
                self.y += self.size // 2
            elif chance > 80:
                self.y += self.size // 4
            self.size += self.ud
            self.ud = -self.ud if abs(self.size) > 8 or self.y + self.size < self.mih - 8 and self.ud < 0 or\
                                self.y + self.size > self.mah and self.ud > 0 or random.randint(0, 8) < self.size\
                or abs(self.y - self.meh) > 20 and random.randint(0, 100) > 80 else self.ud
            self.lines = np.append(self.lines, (str(self.y) + ' ' + str(-self.y)))


class Player:
    def __init__(self, world, pos:list):
        self.world = world
        self.pos = pos

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.pos[0] > 0: self.pos[0] -= PMS
        if keys[pg.K_d]: self.pos[0] += PMS


class Console:
    def __init__(self, main):
        self.prg = main
        self.lines = []
        self.surf = pg.Surface((600, 400), pg.SRCALPHA)
        self.surf.fill((0, 0, 0, 128))
        self.asurf = pg.Surface((600, 50), pg.SRCALPHA)
        self.asurf.fill((0, 0, 0, 128))
        self.enterbox = pg.Surface((50, 560))

    def draw(self):
        self.prg.screen.blit(self.surf, (0, 0))
        self.prg.screen.blit(self.enterbox, (550, 20))

    def adraw(self):
        self.prg.screen.blit(self.asurf, (0, 0))

    def input(self):
        self.prg.input(self.enterbox)
