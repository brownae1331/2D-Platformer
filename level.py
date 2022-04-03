# This file places the tiles in the shape of the level
import pygame
from player import Player
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
        self.player = pygame.sprite.GroupSingle()

        # enumerate give the value of whats in each row and give the index of each row
        for rowIndex, row in enumerate(layout):
            # This  give the value of whats in each column and its index
            for colIndex, col in enumerate(row):
                # Find the coordinate where the tile needs to be placed
                x = colIndex * tileSize
                y = rowIndex * tileSize

                # If there is an X in the level data then a tile is place on the screen
                if col == 'X':
                    tile = Tile((x, y), tileSize)
                    self.tiles.add(tile)
                # If there is a P in the level data the plater will be placed there
                if col == 'P':
                    player = Player((x, y))
                    self.player.add(player)

    # When the game starts this function is called
    def run(self):

        # Level tiles
        self.tiles.draw(self.displaySurface)

        # Player
        self.player.update()
        self.player.draw(self.displaySurface)
