import pygame
from button import Button
from settings import *


class Menu:
    def __init__(self, game):
        self.game = game
        self.background = pygame.image.load('Assests/Background/Brown.png')
        self.text = pygame.font.Font("Assests/Fonts/PixelColeco-4vJW.ttf", 100)

        self.menuText = self.text.render('Main Menu', True, '#000000')
        self.menuRect = self.menuText.get_rect(center=(800, 200))

        self.playButton = Button(pygame.image.load(
            'Assests/Menu/Buttons/Play.png'), (800, 400), 64, 64)
        self.quitButton = Button(pygame.image.load(
            'Assests/Menu/Buttons/Close.png'), (800, 600), 64, 64)

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

    def menuLoop(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.checkEvent()
            self.mousePos = pygame.mouse.get_pos()
            self.game.display.fill('black')

            self.displayMenu()
            self.blitScreen()
            self.buttonPress()

    def buttonPress(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playButton.checkForInput(self.mousePos):
                    self.game.playing = True
                    self.runDisplay = False
                elif self.quitButton.checkForInput(self.mousePos):
                    self.game.running = False
                    self.game.playing = False
                    self.runDisplay = False

    def displayMenu(self):
        for x in range(25):
            for y in range(13):
                if x / 2 != 0 or x / 2 != 1:
                    self.game.display.blit(
                        self.background, (x * tileSize, y * tileSize))
                else:
                    self.game.display.blit(pygame.transform.flip(
                        self.background, False, True), (x * tileSize, y * tileSize))

            for button in [self.playButton, self.quitButton]:
                button.update(self.game.display)

            self.game.display.blit(self.menuText, self.menuRect)
