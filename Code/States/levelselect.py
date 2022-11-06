import pygame
from button import ImageButton
from States.state import State


class LevelSelect(State):
    def __init__(self, game):
        self.game = game

        self.levelButtons = []
        for i in range(30):
            self.levelButtons[i] = ImageButton(
                pygame.image.load('Assets/Menu/Levels/' + str(i) + '.png'), (100, 100), 64, 64)

    def update(self, action):
        for i in range(30):
            print('Assets/Menu/Levels/' + str(i + 1) + '.png')

    def render(self, display):
        display.fill('black')

        for button in self.levelButtons:
            button.update(display)
