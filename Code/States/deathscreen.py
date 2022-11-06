import pygame
from button import ImageButton
from States.state import State


class DeathScreen(State):
    def __init__(self, game):
        self.game = game
        self.text = pygame.font.Font("Assets/Fonts/PixelColeco-4vJW.ttf", 100)

        self.gameOverTxt = self.text.render('Game Over', True, 'white')
        self.gameOverRect = self.gameOverTxt.get_rect(center=(800, 200))

        self.restartButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Restart.png'), (800, 400), 64, 64)
        self.levelsButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Levels.png'), (800, 600), 64, 64)

    def update(self, actions):
        self.mousePos = pygame.mouse.get_pos()
        if actions['mouse']:
            if self.restartButton.checkForInput(self.mousePos):
                self.exitState()
            elif self.levelsButton.checkForInput(self.mousePos):
                self.exitState()
        self.game.resetKeys()

    def render(self, display):
        display.fill('black')
        display.blit(self.gameOverTxt, self.gameOverRect)

        for button in [self.levelsButton, self.restartButton]:
            button.update(display)
