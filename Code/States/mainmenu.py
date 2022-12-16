import pygame
from button import ImageButton
from States.state import State
from States.levelselect import LevelSelect
from States.leveleditor import LevelEditor


class MainMenu(State):
    def __init__(self, game):
        self.game = game
        self.background = pygame.image.load(
            'Assets/Background/Brown.png')
        self.text = pygame.font.Font("Assets/Fonts/PixelColeco-4vJW.ttf", 100)

        self.menuText = self.text.render('Main Menu', True, '#000000')
        self.menuRect = self.menuText.get_rect(center=(800, 100))

        self.playButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Play.png'), (550, 400), 64, 64)
        self.leaderBoardButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Leaderboard.png'), (700, 400), 64, 64)
        self.levelEditorButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Leveleditor.png'), (850, 400), 64, 64)
        self.quitButton = ImageButton(pygame.image.load(
            'Assets/Menu/Buttons/Close.png'), (1000, 400), 64, 64)

    def update(self, actions):
        self.mousePos = pygame.mouse.get_pos()
        if actions['leftmouse']:
            if self.playButton.checkForInput(self.mousePos):
                newState = LevelSelect(self.game)
                newState.enterState()
            elif self.levelEditorButton.checkForInput(self.mousePos):
                newState = LevelEditor(self.game)
                newState.enterState()
            elif self.quitButton.checkForInput(self.mousePos):
                self.game.running = False

    def render(self, display):
        for x in range(25):
            for y in range(13):
                if x / 2 != 0 or x / 2 != 1:
                    display.blit(
                        self.background, (x * 64, y * 64))
                else:
                    display.blit(pygame.transform.flip(
                        self.background, False, True), (x * 64, y * 64))

        for button in [self.playButton, self.leaderBoardButton, self.levelEditorButton, self.quitButton]:
            button.update(display)

        display.blit(self.menuText, self.menuRect)
