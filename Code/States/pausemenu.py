import pygame
from button import TextButton
from settings import *
from States.state import State
from States.leveleditor import LevelEditor


class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        self.runMenu = False
        self.menu = pygame.image.load('Assets/Menu/Menu.png')
        self.levelEditorButton = TextButton(
            'Level Editor', 'Assets/Fonts/PixelColeco-4vJW.ttf', (screenWidth-135, 120))
        self.exitButton = TextButton(
            'Exit', 'Assets/Fonts/PixelColeco-4vJW.ttf', (screenWidth-135, 240))
        self.settingsButton = TextButton(
            'settings', 'Assets/Fonts/PixelColeco-4vJW.ttf', (screenWidth-135, 180))

        self.text = pygame.font.Font("Assets/Fonts/PixelColeco-4vJW.ttf", 40)
        self.menuText = self.text.render('Menu', True, 'white')
        self.menuRect = self.menuText.get_rect(center=(screenWidth-135, 50))

    def update(self, actions):
        self.buttonPress()
        if actions["escape"]:
            self.exitState()
        self.game.resetKeys()

    def buttonPress(self):
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.levelEditorButton.checkForInput(mousePos):
                    self.exitState()
                    newState = LevelEditor(self.game)
                    newState.enterState()

    def render(self, display):
        display.blit(self.menu, (screenWidth - 270, 0))
        display.blit(self.menuText, self.menuRect)
        self.levelEditorButton.update(display)
        self.settingsButton.update(display)
        self.exitButton.update(display)
