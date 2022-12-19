import pygame
from pygame.math import Vector2 as vector
from settings import *
from States.state import State
from editormenu import EditorMenu


class LevelEditor(State):
    def __init__(self, game):
        # main setup
        self.game = game
        self.canvasData = {}

        # navigation
        self.origin = vector()
        self.panActive = False
        self.panOffset = vector()

        # selection
        self.selectionIndex = 0
        self.lastSelectedCell = None

        # menu
        self.menu = EditorMenu()

    def update(self, actions):
        self.moveScreen(actions)
        self.selectionHotkeys(actions)
        self.menuClick(actions)
        self.screenClick(actions)

    def render(self, display):
        display.fill('white')
        pygame.draw.circle(display, 'red', self.origin, 10)
        self.drawLevel(display)
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

    def selectionHotkeys(self, actions):
        if actions['right']:
            self.selectionIndex += 1
        if actions['left']:
            self. selectionIndex -= 1
        self.selectionIndex = max(0, min(self.selectionIndex, 10))

    def menuClick(self, actions):
        if actions['rightmouseclick'] and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            self.selectionIndex = self.menu.click(pygame.mouse.get_pos())

    def screenClick(self, actions):
        if actions['leftmouse'] and not self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            currentCell = self.getCurrentCell()

            if currentCell != self.lastSelectedCell:
                if currentCell in self.canvasData:
                    self.canvasData[currentCell].addId(self.selectionIndex)
                else:
                    self.canvasData[currentCell] = CanvasTile(
                        self.selectionIndex)
                self.lastSelectedCell = currentCell

    def getCurrentCell(self):
        distanceFromOrigin = pygame.mouse.get_pos() - self.origin

        # This prevents all 4 cells around the origin being (0, 0)
        if distanceFromOrigin.x > 0:
            col = int(distanceFromOrigin.x / tileSize)
        else:
            col = int(distanceFromOrigin.x / tileSize) - 1

        if distanceFromOrigin.y > 0:
            row = int(distanceFromOrigin.y / tileSize)
        else:
            row = int(distanceFromOrigin.y / tileSize) - 1

        return col, row

    def drawGrid(self, display):
        cols = screenWidth // tileSize
        rows = screenHeight // tileSize

        # This vector is always close to the left side of the screen to it look like the grid is infinite
        # The origin offset is the point where the lines intersect which it closest to the top left of the screen
        originOffset = vector(
            x=self.origin.x - int(self.origin.x / tileSize) * tileSize,
            y=self.origin.y - int(self.origin.y / tileSize) * tileSize)

        for col in range(cols + 1):
            x = originOffset.x + col * tileSize
            pygame.draw.line(display, 'black', (x, 0), (x, screenHeight))

        for row in range(rows + 1):
            y = originOffset.y + row * tileSize
            pygame.draw.line(display, 'black', (0, y), (screenWidth, y))

    def drawLevel(self, display):
        for cellPos, tile in self.canvasData.items():
            pos = self.origin + pygame.math.Vector2(cellPos) * tileSize

            # terrain
            if tile.hasTerrain:
                surf = terrainTiles['TM']
                display.blit(surf, pos)

            # platform
            if tile.hasPlatform:
                surf = pygame.Surface((tileSize, tileSize))
                surf.fill('brown')
                display.blit(surf, pos)

            # fruit
            if tile.fruit:
                surf = pygame.Surface((tileSize, tileSize))
                surf.fill('red')
                display.blit(surf, pos)

            # enemy
            if tile.enemy:
                surf = pygame.Surface((tileSize, tileSize))
                surf.fill('grey')
                display.blit(surf, pos)


class CanvasTile:
    def __init__(self, tileId):

        # terrain
        self.hasTerrain = False
        self.terrainNeighbors = []

        # platform
        self.hasPlatform = False
        self.platformNeighbors = []

        # fruit
        self.fruit = None

        # enemy
        self.enemy = None

        # objects
        self.objects = []

        self.addId(tileId)

    def addId(self, tileId):
        options = {key: value['style']
                   for key, value in LevelEditorData.items()}
        match options[tileId]:
            case 'terrain': self.hasTerrain = True
            case 'platform': self.hasPlatform = True
            case 'fruit': self.fruit = tileId
            case 'enemy': self.enemy = tileId
