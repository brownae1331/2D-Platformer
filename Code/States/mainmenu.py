import pygame
from button import ImageButton
from settings import *
from States.state import State
from States.level import Level
from gamedata import level1


class MainMenu(State):
    def __init__(self, game):
        self.game = game
        self.background = pygame.image.load('Assets/Background/Brown.png')
        self.text = pygame.font.Font("Assets/Fonts/PixelColeco-4vJW.ttf", 100)

        self.menuText = self.text.render('Main Menu', True, '#000000')
        self.menuRect = self.menuText.get_rect(center=(800, 200))

        self.playButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Play.png'), (800, 400), 64, 64)
        self.quitButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Close.png'), (800, 600), 64, 64)

    def update(self, actions):
        self.mousePos = pygame.mouse.get_pos()
        if actions['mouse']:
            if self.playButton.checkForInput(self.mousePos):
                newState = Level(self.game, level1)
                newState.enterState()
            elif self.quitButton.checkForInput(self.mousePos):
                self.game.running = False
        self.game.resetKeys()

    def render(self, display):
        for x in range(25):
            for y in range(13):
                if x / 2 != 0 or x / 2 != 1:
                    display.blit(
                        self.background, (x * tileSize, y * tileSize))
                else:
                    display.blit(pygame.transform.flip(
                        self.background, False, True), (x * tileSize, y * tileSize))

            for button in [self.playButton, self.quitButton]:
                button.update(display)

            display.blit(self.menuText, self.menuRect)
