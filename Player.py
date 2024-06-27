import pygame as pg

from Kunai import *

GRAVITY = 1.5
MAX_VELOCITY = 30

class Player():
    def __init__(self, game):
        self.game = game
        self.x = 300
        self.y = 50
        self.width = 32
        self.height = 32
        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)
        self.position = pg.math.Vector2(0, 0)
        self.speed = 8
        self.vel_y = 0
        self.vel_x = 0
        self.movement = [False, False, False, False ] # up, down, left, right
        self.isJumping = False
        self.kunaiCooldown = 0
        self.cooldowns = []
        self.cooldowns.append(self.kunaiCooldown)


    def update(self):
        self.move()
        self.cooldown()

    def draw(self):
        scrollAdjustedRect = pg.rect.Rect(self.rect.x - self.game.scroll[0], self.rect.y - self.game.scroll[1], self.rect.width, self.rect.height)
        pg.draw.rect(self.game.window, (0, 0, 255), scrollAdjustedRect)

    def move(self):
        key = pg.key.get_pressed()
        dx = 0
        dy = 0

        if key[pg.K_a] or key[pg.K_LEFT]:
            dx -= self.speed
            self.flipped = True
        if key[pg.K_d] or key[pg.K_RIGHT]:
            dx += self.speed
            self.flipped = False
        if (key[pg.K_w] or key[pg.K_UP]) and not self.isJumping:
            self.jump()
        if key[pg.K_q] and not self.kunaiCooldown:
            Kunai(self.game)
            self.kunaiCooldown = 180

        if self.isJumping or self.isAirborn():
            self.vel_y = min(self.vel_y + GRAVITY, MAX_VELOCITY)

        for tile in self.game.tiles:
            if tile.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                if not self.flipped:
                    dx = tile.rect.left - self.rect.right
                else:
                    dx = tile.rect.right - self.rect.left
            if tile.rect.colliderect(self.rect.x, self.rect.y + self.vel_y, self.width, self.height):
                if self.vel_y > 0: # falling
                    dy = tile.rect.top - self.rect.bottom
                    self.vel_y = 0
                    self.isJumping = False
                else: # jumping
                    dy = self.rect.top - tile.rect.bottom
                    self.vel_y = 0
        dy += self.vel_y

        self.rect.x += dx
        self.rect.y += dy

    def cooldown(self):
        if self.kunaiCooldown > 0:
            self.kunaiCooldown -= 1

    def jump(self):
        self.vel_y = 0
        self.vel_y -= 30
        self.isJumping = True

    # HELPER METHODS
    def isOnGround(self):
        for tile in self.game.tiles:
            if self.rect.colliderect(tile.rect):
                if self.rect.bottom == tile.rect.top:
                    return True
        return False
    
    def isAirborn(self):
        for tile in self.game.tiles:
            if self.rect.colliderect(tile.rect):
                return False
        return True