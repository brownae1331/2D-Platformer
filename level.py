# This file places the tiles in the shape of the level
import pygame
from tiles import Tile
from settings import tileSize


class Level:
    # The level needs the level data to know what it has to draw and it need the surface that it has to draw on
    def __init__(self, levelData, surface):
        # Set the attribute for the suface the level will be displayed on
        self.displaySurface = surface
        self.setupLevel(levelData)  # Set the attribute for the level data

    # This function is going to draw the level onto the screen
    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()

        # enumerate give the value of whats in each row and give the index of each row
        for rowIndex, row in enumerate(layout):
            # This  give the value of whats in each column and its index
            for colIndex, col in enumerate(row):
                # If there is an X in the level data then a tile is place on the screen
                if col == 'X':
                    # Find the coordinate where the tile needs to be placed
                    x = colIndex * tileSize
                    y = rowIndex * tileSize

                    tile = Tile((x, y), tileSize)
                    self.tiles.add(tile)

    # When the game starts this function is called
    def run(self):
        self.tiles.draw(self.displaySurface)
