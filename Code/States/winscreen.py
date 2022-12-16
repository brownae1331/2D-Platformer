import pygame
from button import ImageButton
from States.state import State


class WinScreen(State):
    def __init__(self, game):
        self.game = game
        self.text = pygame.font.Font("Assets/Fonts/PixelColeco-4vJW.ttf", 100)

        self.winTxt = self.text.render('You Win', True, 'black')
        self.winRect = self.winTxt.get_rect(center=(800, 200))

        self.nextButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Next.png'), (800, 400), 64, 64)
        self.levelsButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Levels.png'), (800, 600), 64, 64)

    def update(self, actions):
        self.mousePos = pygame.mouse.get_pos()
        if actions['leftmouse']:
            if self.nextButton.checkForInput(self.mousePos):
                self.exitState()
            elif self.levelsButton.checkForInput(self.mousePos):
                self.exitState()
        self.game.resetKeys()

    def render(self, display):
        display.fill('#d4af37')
        display.blit(self.winTxt, self.winRect)

        for button in [self.nextButton, self.levelsButton]:
            button.update(display)
