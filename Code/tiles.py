# This file holds the Tile class which will be used by the level class to place them
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):  # The tile has to know its position on the screen and its size
        super().__init__()
        # The tile is a square so the width and height are the same
        self.image = pygame.image.load('Assests/Terrain/Grass Block.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        # Place the top left of the tile where the position is
        self.rect = self.image.get_rect(topleft=pos)

    # Keep the world shift to the x position of all tiles
    def update(self, xShift):
        self.rect.x += xShift
