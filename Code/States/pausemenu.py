import pygame
from button import TextButton
from settings import *
from States.state import State
from States.leveleditor import LevelEditor


class PauseMenu(State):
    def __init__(self, game):
        self.game = game
        self.runMenu = False
        self.menu = pygame.image.load('Assests/Menu/Menu.png')
        self.levelEditorButton = TextButton(
            'Level Editor', 'Assests/Fonts/PixelColeco-4vJW.ttf', (screenWidth-138, 80))

    def update(self):
        self.buttonPress()

    def buttonPress(self):
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.levelEditorButton.checkForInput(mousePos):
                    self.exitState()
                    newState = LevelEditor(self.game)
                    newState.enterState()

    def render(self, display):
        display.blit(self.menu, (screenWidth - 277, 0))
        self.levelEditorButton.update(display)
