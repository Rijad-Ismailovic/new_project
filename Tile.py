import pygame as pg

class Tile:
    def __init__(self, game, rect):
        self.game = game
        self.rect = pg.Rect(rect) 

    def draw(self):
        scrollAdjustedRect = pg.Rect(self.rect.x - self.game.scroll[0], self.rect.y - self.game.scroll[1], self.rect.width, self.rect.height)
        pg.draw.rect(self.game.window, (0, 255, 0), scrollAdjustedRect, 1)

    def toString(self):
        print("x:", self.rect.x, " y:", self.rect.y, " width:", self.rect.width, " height:", self.rect.height)