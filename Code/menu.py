import pygame
from settings import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.runMenu = False
        self.menu = pygame.image.load('Assests/Menu/Menu.png')

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def menuLoop(self):
        self.game.checkEvent()

        while self.runMenu:
            self.game.checkEvent()

            self.drawMenu()
            self.blitScreen()

    def drawMenu(self):
        self.game.display.blit(self.menu, (screenWidth - 277, 0))
