import pygame
from settings import *
from States.mainmenu import MainMenu


class Game():
    def __init__(self):
        pygame.init()
        self.display = pygame.Surface([screenWidth, screenHeight])
        self.window = pygame.display.set_mode([screenWidth, screenHeight])
        self.clock = pygame.time.Clock()
        self.running = True
        self.stateStack = []
        self.loadStates()

    def gameLoop(self):
        while self.running:
            self.checkEvent()
            self.update()
            self.render()

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.stateStack[-1].update()

    def render(self):
        self.stateStack[-1].render(self.display)
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def loadStates(self):
        self.maimMenu = MainMenu(self)
        self.stateStack.append(self.maimMenu)


game = Game()
while game.running:
    game.gameLoop()
