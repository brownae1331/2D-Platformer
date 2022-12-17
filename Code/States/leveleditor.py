import pygame
from pygame.math import Vector2 as vector
from settings import *
from States.state import State


class LevelEditor(State):
    def __init__(self, game):
        self.game = game

        # navigation
        self.origin = vector()
        self.panActive = False
        self.panOffset = vector()

        # selection
        self.selectionIndex = 0

        # menu
        self.menu = Menu()

    def update(self, actions):
        self.moveScreen(actions)
        self.selectionHotkeys(actions)
        self.menuClick(actions)

    def render(self, display):
        display.fill('white')
        pygame.draw.circle(display, 'red', self.origin, 10)
        self.drawGrid(display)
        self.menu.render(self.selectionIndex, display)

    def moveScreen(self, actions):
        # Check middle mouse
        if actions['middlemouseclick']:
            self.panOffset = vector(pygame.mouse.get_pos()) - self.origin

        self.panActive = actions['middlemouse']

        # Move screen
        if self.panActive:
            self.origin = vector(pygame.mouse.get_pos()) - self.panOffset

    def drawGrid(self, display):
        cols = screenWidth // tileSize
        rows = screenHeight // tileSize

        # This vector is always close to the left side of the screen to it look like the grid is infinite
        originOffset = vector(
            x=self.origin.x - int(self.origin.x / tileSize) * tileSize,
            y=self.origin.y - int(self.origin.y / tileSize) * tileSize)

        for col in range(cols + 1):
            x = originOffset.x + col * tileSize
            pygame.draw.line(display, 'black', (x, 0), (x, screenHeight))

        for row in range(rows + 1):
            y = originOffset.y + row * tileSize
            pygame.draw.line(display, 'black', (0, y), (screenWidth, y))

    def selectionHotkeys(self, actions):
        if actions['right']:
            self.selectionIndex += 1
        if actions['left']:
            self. selectionIndex -= 1
        self.selectionIndex = max(0, min(self.selectionIndex, 10))

    def menuClick(self, actions):
        if actions['rightmouseclick'] and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            self.selectionIndex = self.menu.click(pygame.mouse.get_pos())


class Menu:
    def __init__(self):
        self.createData()
        self.drawMenu()

    def render(self, index, display):
        self.buttons.update()
        self.buttons.draw(display)
        self.highlight(index, display)

    def createData(self):
        self.menuSurfs = {}
        for key, value in LevelEditorData.items():
            if value['menu']:
                if not value['menu'] in self.menuSurfs:
                    self.menuSurfs[value['menu']] = [
                        (key, pygame.image.load(value['path']))]
                else:
                    self.menuSurfs[value['menu']].append(
                        (key, pygame.image.load(value['path'])))

    def drawMenu(self):

        # Menu Area
        self.rect = pygame.Rect(
            screenWidth - 186, screenHeight - 186, 180, 180)

        # Button Areas
        genericButtonRect = pygame.Rect(
            self.rect.topleft, (self.rect.width / 2, self.rect.height / 2))
        self.tileButtonRect = genericButtonRect.copy().inflate(-5, -5)
        self.fruitButtonRect = genericButtonRect.move(
            self.rect.width / 2, 0).inflate(-5, -5)
        self.crateButtonRect = genericButtonRect.move(
            0, self.rect.width / 2).inflate(-5, -5)
        self.enemyButtonRect = genericButtonRect.move(
            self.rect.width / 2, self.rect.width / 2).inflate(-5, -5)

        # Create the Buttons
        self.buttons = pygame.sprite.Group()
        MenuButton(self.tileButtonRect, self.buttons,
                   self.menuSurfs['terrain'])
        MenuButton(self.fruitButtonRect, self.buttons, self.menuSurfs['fruit'])
        MenuButton(self.crateButtonRect, self.buttons, self.menuSurfs['crate'])
        MenuButton(self.enemyButtonRect, self.buttons, self.menuSurfs['enemy'])

    def click(self, pos):
        for sprite in self.buttons:
            if sprite.rect.collidepoint(pos):
                sprite.switch()
                return sprite.getId()

    def highlight(self, index, display):
        if LevelEditorData[index]['menu'] == 'terrain':
            pygame.draw.rect(display, '#f5f1de',
                             self.tileButtonRect.inflate(4, 4), 5, 4)
        if LevelEditorData[index]['menu'] == 'fruit':
            pygame.draw.rect(display, '#f5f1de',
                             self.fruitButtonRect.inflate(4, 4), 5, 4)
        if LevelEditorData[index]['menu'] == 'crate':
            pygame.draw.rect(display, '#f5f1de',
                             self.crateButtonRect.inflate(4, 4), 5, 4)
        if LevelEditorData[index]['menu'] == 'enemy':
            pygame.draw.rect(display, '#f5f1de',
                             self.enemyButtonRect.inflate(4, 4), 5, 4)


class MenuButton(pygame.sprite.Sprite):
    def __init__(self, rect, group, items):
        super().__init__(group)
        self.image = pygame.Surface(rect.size)
        self.rect = rect

        self.items = items
        self.index = 0

    def getId(self):
        return self.items[self.index][0]

    def switch(self):
        self.index += 1
        self.index = 0 if self.index >= len(self.items) else self.index

    def update(self):
        self.image.fill('#33323d')
        surf = self.items[self.index][1]

        rect = surf.get_rect(
            center=(self.rect.width / 2, self.rect.height / 2))
        self.image.blit(surf, rect)
