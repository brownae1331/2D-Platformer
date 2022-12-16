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
        self.drawMenu(display)

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

    def drawMenu(self, display):

        # Menu Area
        self.menuRect = pygame.Rect(
            screenWidth - 186, screenHeight - 186, 180, 180)
        pygame.draw.rect(display, 'red', self.menuRect)

        # Button Areas
        genericButtonRect = pygame.Rect(
            self.menuRect.topleft, (self.menuRect.width / 2, self.menuRect.height / 2))
        self.tileButtonRect = genericButtonRect.copy().inflate(-5, -5)
        self.coinButtonRect = genericButtonRect.move(
            self.menuRect.width / 2, 0).inflate(-5, -5)
        self.crateButtonRect = genericButtonRect.move(
            0, self.menuRect.width / 2).inflate(-5, -5)
        self.enemyButtonRect = genericButtonRect.move(
            self.menuRect.width / 2, self.menuRect.width / 2).inflate(-5, -5)

        pygame.draw.rect(display, 'green', self.tileButtonRect)
        pygame.draw.rect(display, 'blue', self.coinButtonRect)
        pygame.draw.rect(display, 'yellow', self.crateButtonRect)
        pygame.draw.rect(display, 'purple', self.enemyButtonRect)


class menuButton(pygame.sprite.Sprite):
    def __init__(self, rect, group, items):
        super().__init__(group)
        self.image = pygame.Surface(rect.size)
        self.rect = rect

        self.items = items
        self.index = 0
