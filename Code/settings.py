# This file hold the variables that will be used in all the files
from csv import reader
import pygame

screenWidth = 1536
screenHeight = 704

# This is what the level is going to look like
# The 'X' are tiles
levelMap = [
    '                                                          ',
    '                                                          ',
    '                                                          ',
    '                                                          ',
    '                                                          ',
    '                                                          ',
    '            Z                                             ',
    '                                                          ',
    ' P               E                                        ',
    '                                                          ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
]

tileSize = 64  # The size of the tiles


def importCSVLayout(path):
    terrainMap = []
    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrainMap.append(list(row))
        return terrainMap


def importTilesets(path):
    surface = pygame.image.load(path).convert_alpha()
    tileNumX = int(surface.get_size()[0] / tileSize)
    tileNumY = int(surface.get_size()[1] / tileSize)

    cutTiles = []
    for row in range(tileNumY):
        for col in range(tileNumX):
            x = col * tileSize
            y = row * tileSize
            newSurface = pygame.Surface((tileSize, tileSize))
            newSurface.blit(surface, (0, 0), pygame.Rect(
                x, y, tileSize, tileSize))
            cutTiles.append(newSurface)

    return cutTiles
