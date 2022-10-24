# This file holds the Tile class which will be used by the level class to place them
import pygame
from animation import Animation


class Tile(pygame.sprite.Sprite):
    # The tile has to know its position on the screen and its size
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)

    # Keep the world shift to the x position of all tiles
    def update(self, xShift):
        self.rect.x += xShift


class StaticTile(Tile):
    def __init__(self, pos, size, image):
        super().__init__(pos, size)
        self.image = image


class AnimatedTile(Tile, Animation):
    def __init__(self, pos, size, path, status, steps, width, height):
        super().__init__(pos, size)
        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 75
        self.frameIndex = 0

        self.path = path
        self.status = status
        self.animationSteps = steps
        self.width, self.height = width, height
        self.getAnimationAssests(
            self.path, self.status, self.animationSteps, self.width, self.height)
        self.image = self.animationList[self.frameIndex]

    def update(self, xShift):
        self.rect.x += xShift
        self.getAnimationAssests(
            self.path, self.status, self.animationSteps, self.width, self.height)
        self.image = self.animation(self.animationSteps)


class Crate(StaticTile):
    def __init__(self, pos, size):
        super().__init__(pos, size, pygame.image.load(
            'Assets/Items/Boxes/Box1/Idle.png').convert_alpha())
        offset_y = pos[1] + size
        self.rect = self.image.get_rect(bottomleft=(pos[0], offset_y))


class Fruit(AnimatedTile):
    def __init__(self, pos, size, path, steps, width, height):
        super().__init__(pos, size, path, 'None', steps, width, height)
        center_x = pos[0] + int(size / 2)
        center_y = pos[1] + int(size / 2)
        self.rect = self.image.get_rect(center=(center_x, center_y))


class Checkpoint(StaticTile):
    def __init__(self, pos, size, image):
        super().__init__(pos, size, image)
        offset_y = pos[1] + size
        self.rect = self.image.get_rect(bottomleft=(pos[0], offset_y))
