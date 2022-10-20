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
        self.actions = {"left": False, "right": False,
                        "space": False, "escape": False}
        self.stateStack = []
        self.loadStates()

    def gameLoop(self):
        while self.running:
            self.checkEvent()
            self.render()
            self.update()
            self.clock.tick(60)

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = True
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = True
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = True
                if event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = True

    def resetKeys(self):
        for i in self.actions:
            self.actions[i] = False

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
