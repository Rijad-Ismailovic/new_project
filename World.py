from Tile import *

TILE_SIZE = 32

class World:
    def __init__(self, game):
        self.game = game

    def loadLevel(self, level):
        tiles = []
        x = 0
        y = 0
        with open(f"lvl_{level}.txt", "r") as f:
            for line in f:
                x = 0
                for char in line.strip():
                    if char == "0":
                        pass
                    if char == "1":
                        tiles.append(Tile(self.game, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)))
                    x += 1
                y += 1
        return tiles