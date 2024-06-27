import pygame as pg

import math
from Utils import *

class Kunai:
    def __init__(self, game):
        self.game = game
        self.game.attacks.append(self)
        self.rect = pg.Rect(self.game.player.rect.x, self.game.player.rect.y, 20, 20)
        self.angle = calculateAngle((self.game.player.rect.x, self.game.player.rect.y), pg.mouse.get_pos(), self.game.scroll)
        print(math.degrees(self.angle))
        self.speed = 20
        self.deacceleartion = 0.98
        self.life = 60
        self.vel_x = math.cos(self.angle) * self.speed
        self.vel_y = math.sin(self.angle) * self.speed

    def update(self):
        self.move()
        self.life -= 1
        if self.life == 0:
            self.game.player.rect.x = self.rect.x
            self.game.player.rect.y = self.rect.y

    def draw(self):
        scrollAdjustedRect = pg.rect.Rect(self.rect.x - self.game.scroll[0], self.rect.y - self.game.scroll[1], self.rect.width, self.rect.height)
        pg.draw.rect(self.game.window, (83, 83, 83), scrollAdjustedRect)

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.vel_x *= self.deacceleartion
        self.vel_y *= self.deacceleartion