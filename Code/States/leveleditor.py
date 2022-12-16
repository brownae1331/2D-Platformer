import pygame
from pygame.math import Vector2 as vector
from settings import *
from States.state import State


class LevelEditor(State):
    def __init__(self, game):
        self.game = game

        # navigation
        self.origin = vector()
        self.panActive = False
        self.panOffset = vector()

    def update(self, actions):
        self.moveScreen(actions)

    def render(self, display):
        display.fill('white')
        pygame.draw.circle(display, 'red', self.origin, 10)
        self.drawGrid(display)

    def moveScreen(self, actions):
        # Check middle mouse
        if actions['middlemouseclick']:
            self.panOffset = vector(pygame.mouse.get_pos()) - self.origin

        self.panActive = actions['middlemouse']

        # Move screen
        if self.panActive:
            self.origin = vector(pygame.mouse.get_pos()) - self.panOffset

    def drawGrid(self, display):
        cols = screenWidth // tileSize
        rows = screenHeight // tileSize

        # This vector is always close to the left side of the screen to it look like the grid is infinite
        originOffset = vector(
            x=self.origin.x - int(self.origin.x / tileSize) * tileSize,
            y=self.origin.y - int(self.origin.y / tileSize) * tileSize)

        for col in range(cols + 1):
            x = originOffset.x + col * tileSize
            pygame.draw.line(display, 'black', (x, 0), (x, screenHeight))

        for row in range(rows + 1):
            y = originOffset.y + row * tileSize
            pygame.draw.line(display, 'black', (0, y), (screenWidth, y))
