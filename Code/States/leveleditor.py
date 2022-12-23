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

        # save level
        self.level = 1

    def update(self, actions):
        self.moveScreen(actions)
        self.menuClick(actions)
        self.screenClick(actions)
        self.removeTile(actions)
        self.createCVSMap(actions)
        self.changeLevelNum(actions)

    def render(self, display):
        display.fill('white')
        self.drawLevel(display)
        self.drawGrid(display)
        self.menu.render(self.selectionIndex, display)
        self.displayLevelNum(display)

    def moveScreen(self, actions):
        # Check middle mouse
        if actions['middlemouseclick']:
            self.panOffset = vector(pygame.mouse.get_pos()) - self.origin

        self.panActive = actions['middlemouse']

        # Move screen
        if self.panActive:
            self.origin = vector(pygame.mouse.get_pos()) - self.panOffset

    def menuClick(self, actions):
        if actions['rightmouseclick'] and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            newIndex = self.menu.click(
                pygame.mouse.get_pos(), 'right')
            self.selectionIndex = newIndex if newIndex else self.selectionIndex
        elif actions['middlemouseclick'] and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            newIndex = self.menu.click(
                pygame.mouse.get_pos(), 'middle')
            self.selectionIndex = newIndex if newIndex else self.selectionIndex
        elif actions['leftmouseclick'] and self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            newIndex = self.menu.click(
                pygame.mouse.get_pos(), 'left')
            self.selectionIndex = newIndex if newIndex else self.selectionIndex

    def screenClick(self, actions):
        if actions['leftmouse'] and not self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            currentCell = self.getCurrentCell()

            if currentCell != self.lastSelectedCell:
                if currentCell in self.canvasData:
                    self.canvasData[currentCell].addId(self.selectionIndex)
                else:
                    self.canvasData[currentCell] = CanvasTile(
                        self.selectionIndex, LevelEditorData[self.selectionIndex]['csv'])
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
            if tile.terrain or tile.terrain == 0:
                surf = pygame.image.load(
                    LevelEditorData[tile.terrain]['path'])
                display.blit(surf, pos)

            # fruit
            if tile.fruit:
                surf = pygame.image.load(LevelEditorData[tile.fruit]['path'])
                rect = surf.get_rect(
                    center=(pos[0] + tileSize // 2, pos[1] + tileSize // 2))
                display.blit(surf, rect)

            # enemy
            if tile.enemy:
                surf = pygame.image.load(LevelEditorData[tile.enemy]['path'])
                rect = surf.get_rect(
                    midbottom=(pos[0] + tileSize // 2, pos[1] + tileSize))
                display.blit(surf, rect)

            # crate
            if tile.crate:
                surf = pygame.image.load(LevelEditorData[tile.crate]['path'])
                rect = surf.get_rect(
                    center=(pos[0] + tileSize // 2, pos[1] + tileSize // 2))
                display.blit(surf, rect)

            # obstacle
            if tile.obstacle:
                surf = pygame.image.load(
                    LevelEditorData[tile.obstacle]['path'])
                rect = surf.get_rect(
                    midbottom=(pos[0] + tileSize // 2, pos[1] + tileSize))
                display.blit(surf, rect)

    def removeTile(self, actions):
        if actions['rightmouse'] and not self.menu.rect.collidepoint(pygame.mouse.get_pos()):
            if self.canvasData:
                currentCell = self.getCurrentCell()
                if currentCell in self.canvasData:
                    self.canvasData[currentCell].removeId(self.selectionIndex)
                    if self.canvasData[currentCell].isEmpty:
                        del self.canvasData[currentCell]

    def createCVSMap(self, actions):
        if actions['enter']:
            # This is coordinates of a cell that is the most to the left or right
            left = sorted(self.canvasData.keys(),
                          key=lambda tile: tile[0])[0]
            right = sorted(self.canvasData.keys(),
                           key=lambda tile: tile[0])[len(self.canvasData)-1]
            # This is the y coordinate of a cell that is the highest or lowest
            top = sorted(self.canvasData.keys(),
                         key=lambda tile: tile[1])[0][1]
            bottom = sorted(self.canvasData.keys(), key=lambda tile: tile[1])[
                len(self.canvasData)-1][1]

            cols = right[0] - left[0] + 1
            rows = bottom - top + 1

            layers = {
                'crates': [],
                'enemies': [],
                'fruits': [],
                'obstacles': [],
                'terrain': [],
            }

            # create the empty lists
            for key in layers.keys():
                for row in range(rows):
                    r = [-1] * cols
                    layers[key].append(r)

            # Add constraints
            constraints = []
            for row in range(rows):
                r = [-1] * (cols+1)
                constraints.append(r)

            # fill lists
            for tilePos, tile in self.canvasData.items():
                x = tilePos[0] - left[0]
                y = tilePos[1] - top
                if tile.crate:
                    layers['crates'][y][x] = tile.csv
                if tile.enemy:
                    layers['enemies'][y][x] = tile.csv
                if tile.fruit:
                    layers['fruits'][y][x] = tile.csv
                if tile.obstacle:
                    layers['obstacles'][y][x] = tile.csv
                if tile.terrain:
                    layers['terrain'][y][x] = tile.csv
                    if tile.csv == 6:
                        constraints[y-1][x-1] = 3
                    elif tile.csv == 8:
                        constraints[y-1][x+1] = 3
                    elif tile.csv == 28 or tile.csv == 30:
                        constraints[y][x] = 3

            # export contrainsts file
            exportCSVLayout('constraints', constraints, self.level)

            # create files
            for key, value in layers.items():
                exportCSVLayout(key, value, self.level)

            # add start and end
            checkpoints = []
            for row in range(rows):
                r = [-1] * cols
                checkpoints.append(r)

            # the object that is furthest to the left
            checkpoints[left[1]][0] = 0
            # the object that is furthest to the right
            checkpoints[top - right[1]][right[0]-left[0]] = 2
            exportCSVLayout('checkpoints', checkpoints, self.level)

    def displayLevelNum(self, display):
        font = pygame.font.Font('Assets/Fonts/PixelColeco-4vJW.ttf', 50)
        image = font.render(str(self.level), False, '#33323d')
        rect = image.get_rect(topleft=(50, 50))
        display.blit(image, rect)

    def changeLevelNum(self, actions):
        if actions['right']:
            self.level += 1
        if actions['left']:
            self.level -= 1
        self.level = max(1, min(self.level, 30))


class CanvasTile:
    def __init__(self, tileId, csv):

        self.terrain = None
        self.fruit = None
        self.enemy = None
        self.crate = None
        self.obstacle = None

        self.csv = csv

        # objects
        self.objects = []

        self.addId(tileId)
        self.isEmpty = False

    def addId(self, tileId):
        options = {key: value['style']
                   for key, value in LevelEditorData.items()}
        match options[tileId]:
            case 'terrain': self.terrain = tileId
            case 'fruit': self.fruit = tileId
            case 'enemy': self.enemy = tileId
            case 'crate': self.crate = tileId
            case 'obstacle': self.obstacle = tileId

    def removeId(self, tileId):
        options = {key: value['style']
                   for key, value in LevelEditorData.items()}
        match options[tileId]:
            case 'terrain': self.terrain = None
            case 'fruit': self.fruit = None
            case 'enemy': self.enemy = None
            case 'crate': self.crate = None
            case 'obstacle': self.obstacle = None
        self.checkContent()

    def checkContent(self):
        if not self.terrain and not self.fruit and not self.enemy and not self.crate and not self.obstacle:
            self.isEmpty = True
