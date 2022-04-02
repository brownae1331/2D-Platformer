# This file holds the Tile class which will be used by the level class to place them
import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):  # The tile has the attribute of its posiotion and its size
        super().__init__()
        # The tile is a square so the width and height are the same
        self.image = pygame.Surface((size, size))
        # Place the top left of the tile where the position is
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill('grey')  # Not permanent colour
