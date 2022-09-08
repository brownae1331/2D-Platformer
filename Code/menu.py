import pygame
from button import TextButton
from settings import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.runMenu = False
        self.menu = pygame.image.load('Assests/Menu/Menu.png')
        self.levelEditorButton = TextButton(
            'Level Editor', 'Assests/Fonts/PixelColeco-4vJW.ttf', (screenWidth-25, 0))

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def menuLoop(self):
        self.game.checkEvent()

        while self.runMenu:
            self.game.checkEvent()
            self.mousePos = pygame.mouse.get_pos()

            self.drawMenu()
            self.blitScreen()
            self.buttonPress()

    def buttonPress(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.levelEditorButton.checkForInput(self.mousePos):
                    self.runMenu = False
                    self.game.levelEditor.runEditor = True

    def drawMenu(self):
        self.game.display.blit(self.menu, (screenWidth - 277, 0))
        self.levelEditorButton.update(self.game.display)
