# This file holds the Tile class which will be used by the level class to place them
import pygame


class Tile(pygame.sprite.Sprite):
    # The tile has to know its position on the screen and its size
    def __init__(self, pos, size, surface):
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect(topleft=pos)

    # Keep the world shift to the x position of all tiles
    def update(self, xShift):
        self.rect.x += xShift
