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


LevelEditorData = {
    0: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Menu/Grass Terrain.png'},
    1: {'style': 'platform', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Menu/Platform.png'},

    2: {'style': 'fruit', 'type': 'tile', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Apple.png'},
    3: {'style': 'fruit', 'type': 'tile', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Banana.png'},
    4: {'style': 'fruit', 'type': 'tile', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Pineapple.png'},

    5: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Slime.png'},
    6: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Chicken.png'},
    7: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Rino.png'},

    8: {'style': 'crate', 'type': 'tile', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box1.png'},
    9: {'style': 'crate', 'type': 'tile', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box2.png'},
    10: {'style': 'crate', 'type': 'tile', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box3.png'}

}

terrainTiles = {
    'BL': pygame.image.load('Assets/Level Editor/Terrain/BL.png'),
    'BM': pygame.image.load('Assets/Level Editor/Terrain/BM.png'),
    'BR': pygame.image.load('Assets/Level Editor/Terrain/BR.png'),
    'M': pygame.image.load('Assets/Level Editor/Terrain/M.png'),
    'ML': pygame.image.load('Assets/Level Editor/Terrain/ML.png'),
    'MR': pygame.image.load('Assets/Level Editor/Terrain/MR.png'),
    'TL': pygame.image.load('Assets/Level Editor/Terrain/TL.png'),
    'TM': pygame.image.load('Assets/Level Editor/Terrain/TM.png'),
    'TR': pygame.image.load('Assets/Level Editor/Terrain/TR.png'),
    'XBL': pygame.image.load('Assets/Level Editor/Terrain/XBL.png'),
    'XBR': pygame.image.load('Assets/Level Editor/Terrain/XBR.png'),
    'XTL': pygame.image.load('Assets/Level Editor/Terrain/XTL.png'),
    'XTR': pygame.image.load('Assets/Level Editor/Terrain/XTR.png')
}
