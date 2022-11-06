import pygame
from settings import *
from States.state import State


class LevelEditor(State):
    def __init__(self, game):
        self.game = game

    def update(self, actions):
        pass

    def render(self, display):
        for x in range(0, screenWidth, tileSize):
            for y in range(0, screenHeight, tileSize):
                rect = pygame.Rect(x, y, tileSize, tileSize)
                pygame.draw.rect(display, 'white', rect, 1)
