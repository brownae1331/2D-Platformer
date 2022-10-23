# This file hold the variables that will be used in all the files
from csv import reader
import pygame

screenWidth = 1536
screenHeight = 704

tileSize = 64  # The size of the tiles


def importCSVLayout(path):
    terrainMap = []
    with open(path) as map:
        level = reader(map, delimiter=',')
        for row in level:
            terrainMap.append(list(row))
        return terrainMap


def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tileSize)
    tile_num_y = int(surface.get_size()[1] / tileSize)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tileSize
            y = row * tileSize
            new_surf = pygame.Surface(
                (tileSize, tileSize), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0, 0), pygame.Rect(
                x, y, tileSize, tileSize))
            cut_tiles.append(new_surf)

    return cut_tiles
