import pygame
from button import Button


class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('Assests/Background/Brown.png')
        self.text = pygame.font.Font("Assests/Fonts/PixelColeco-4vJW.ttf", 100)

        self.menuText = self.text.render('Main Menu', True, '#000000')
        self.menuRect = self.menuText.get_rect(center=(800, 200))

        self.playButton = Button(pygame.image.load(
            'Assests/Menu/Buttons/Play.png'), (800, 400), 64, 64)
        self.quitButton = Button(pygame.image.load(
            'Assests/Menu/Buttons/Close.png'), (800, 600), 64, 64)

    def displayMenu(self):

        for x in range(25):
            for y in range(13):
                if x / 2 != 0 or x / 2 != 1:
                    self.screen.blit(self.background, (x * 64, y * 64))
                else:
                    self.screen.blit(pygame.transform.flip(
                        self.background, False, True), (x * 64, y * 64))

        for button in [self.playButton, self.quitButton]:
            button.update(self.screen)

        self.screen.blit(self.menuText, self.menuRect)

    def buttonPress(self, mousePos):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playButton.checkForInput(mousePos):
                    return 'play'
                elif self.quitButton.checkForInput(mousePos):
                    return 'exit'
                else:
                    return 'menu'
