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
                        "space": False, "escape": False, "z": False, "leftmouse": False, "leftmouseclick": False, "middlemouse": False, "middlemouseclick": False, "rightmouseclick": False, "rightmouse": False}
        self.stateStack = []
        self.loadStates()

    def gameLoop(self):
        while self.running:
            self.checkEvent()
            self.render()
            self.update()
            self.clock.tick(60)

    def checkEvent(self):
        self.actions['leftmouseclick'] = False
        self.actions['middlemouseclick'] = False
        self.actions['rightmouseclick'] = False

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
                if event.key == pygame.K_z:
                    self.actions['z'] = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions['leftmouse'] = True
                if event.button == 2:
                    self.actions['middlemouse'] = True
                if event.button == 3:
                    self.actions['rightmouse'] = True

                self.actions['leftmouseclick'] = pygame.mouse.get_pressed()[0]
                self.actions['middlemouseclick'] = pygame.mouse.get_pressed()[
                    1]
                self.actions['rightmouseclick'] = pygame.mouse.get_pressed()[2]

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.actions['left'] = False
                if event.key == pygame.K_RIGHT:
                    self.actions['right'] = False
                if event.key == pygame.K_SPACE:
                    self.actions['space'] = False
                if event.key == pygame.K_ESCAPE:
                    self.actions['escape'] = False
                if event.key == pygame.K_z:
                    self.actions['z'] = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions['leftmouse'] = False
                if event.button == 2:
                    self.actions['middlemouse'] = False
                if event.button == 3:
                    self.actions['rightmouse'] = False

    def resetKeys(self):
        for i in self.actions:
            self.actions[i] = False

    def update(self):
        self.stateStack[-1].update(self.actions)

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
