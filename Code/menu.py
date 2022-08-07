import pygame
from button import Button


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

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay:
            self.game.checkEvent()
            self.mousePos = pygame.mouse.get_pos()

            for x in range(25):
                for y in range(13):
                    if x / 2 != 0 or x / 2 != 1:
                        self.game.screen.blit(
                            self.background, (x * 64, y * 64))
                    else:
                        self.game.screen.blit(pygame.transform.flip(
                            self.background, False, True), (x * 64, y * 64))

            for button in [self.playButton, self.quitButton]:
                button.update(self.game.screen)

            self.game.screen.blit(self.menuText, self.menuRect)

    def buttonPress(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.playButton.checkForInput(self.mousePos):
                    print("play")
                elif self.quitButton.checkForInput(self.mousePos):
                    print("quit")
