import pygame
from States.state import State
from States.level import Level
from button import ImageButton
from gamedata import level1


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

    def update(self):
        self.mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.restartButton.checkForInput(self.mousePos):
                    newState = Level(self.game, level1)
                    newState.enterState()
                elif self.levelsButton.checkForInput(self.mousePos):
                    self.exitState()

    def render(self, display):
        display.fill('black')
        display.blit(self.gameOverTxt, self.gameOverRect)

        for button in [self.levelsButton, self.restartButton]:
            button.update(display)
