import pygame
from button import ImageButton
from States.state import State
from States.level import Level
from gamedata import *


class LevelSelect(State):
    def __init__(self, game):
        self.game = game
        self.background = pygame.image.load('Assets/Background/Green.png')

        self.backButton = ImageButton(
            pygame.image.load('Assets/Menu/Buttons/Back.png'), (32, 32), 64, 64)
        self.levelButtons = []
        for i in range(30):
            self.levelButtons.append(ImageButton(
                pygame.image.load('Assets/Menu/Levels/' + str(i + 1) + '.png'), ((i % 6) * 100 + 500, (i // 6) * 100 + 150), 64, 64))

    def update(self, actions):
        self.mousePos = pygame.mouse.get_pos()
        if actions['leftmouse']:
            if self.backButton.checkForInput(self.mousePos):
                self.exitState()
            else:
                self.enterLevel()

        elif actions['escape']:
            self.exitState()

    def render(self, display):
        for x in range(25):
            for y in range(13):
                display.blit(self.background, (x * 64, y * 64))

        self.backButton.update(display)
        for button in self.levelButtons:
            button.update(display)

    def enterLevel(self):
        for i in range(30):
            if self.levelButtons[i].checkForInput(self.mousePos):
                newState = Level(self.game, levels[i])
                newState.enterState()
