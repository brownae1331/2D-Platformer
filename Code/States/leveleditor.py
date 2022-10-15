import pygame
from settings import *
from States.state import State


class LevelEditor(State):
    def __init__(self, game):
        self.game = game
        self.runEditor = False

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def editorLoop(self):
        self.game.checkEvent()

        while self.runEditor:
            self.game.checkEvent()

            self.drawGrid()
            self.blitScreen()

    def drawGrid(self):
        for x in range(0, screenWidth, tileSize):
            for y in range(0, screenHeight, tileSize):
                rect = pygame.Rect(x, y, tileSize, tileSize)
                pygame.draw.rect(self.game.display, 'white', rect, 1)
