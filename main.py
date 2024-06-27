import pygame as pg
import sys, os

from Player import *
from Tile import *
from World import *
from Kunai import *

os.system('cls')

DISPLAY_SIZE = (960, 540)
WINDOW_SIZE = (1920, 1080)


class Game():
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(WINDOW_SIZE)
        self.display = pg.Surface((288, 162))  
        self.clock = pg.time.Clock()
        self.player = None
        self.tiles = []
        self.attacks = []
        self.world = World(self)
        self.scroll = [0, 0]

    def load_level(self): 
        self.tiles.clear()
        self.tiles = self.world.loadLevel(0)

    def draw_level(self): 
        for tile in self.tiles:
            tile.draw()

    def new_game(self):
        self.load_level()
        if self.player == None:
            self.player = Player(self)
            
    def update(self):
        self.player.update()
        pg.display.flip()
    
    def draw(self):
        self.window.fill((0, 0, 0))
        self.draw_level()
        self.player.draw()

        for attack in self.attacks:
            attack.update()
            attack.draw()

        #self.window.blit(pg.transform.scale(self.display, WINDOW_SIZE), (0, 0))

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit() 
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()


    def run(self):
        self.new_game( )
        while True:
            self.check_event()
            self.scroll[0] += ( self.player.rect.x - self.scroll[0] - WINDOW_SIZE[0] / 2 ) / 15
            self.scroll[1] += ( self.player.rect.y - self.scroll[1] - WINDOW_SIZE[1] / 2 - self.player.height / 2 ) / 15

            self.update()
            self.draw()

            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
