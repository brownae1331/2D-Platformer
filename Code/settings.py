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
    0: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/TL.png'},
    1: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/TM.png'},
    2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/TR.png'},
    3: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/ML.png'},
    4: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/M.png'},
    5: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/MR.png'},
    6: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/BL.png'},
    7: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/BM.png'},
    8: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/BR.png'},
    9: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XBL.png'},
    10: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XBR.png'},
    11: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XTL.png'},
    12: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XTR.png'},

    13: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/HL.png'},
    14: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/HM.png'},
    15: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/HR.png'},
    16: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/VB.png'},
    17: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/VM.png'},
    18: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/VT.png'},
    19: {'style': 'terrain', 'type': 'tile', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/X.png'},

    20: {'style': 'fruit', 'type': 'tile', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Apple.png'},
    21: {'style': 'fruit', 'type': 'tile', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Banana.png'},
    22: {'style': 'fruit', 'type': 'tile', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Pineapple.png'},

    23: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Slime.png'},
    24: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Chicken.png'},
    25: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Rino.png'},

    26: {'style': 'crate', 'type': 'tile', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box1.png'},
    27: {'style': 'crate', 'type': 'tile', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box2.png'},
    28: {'style': 'crate', 'type': 'tile', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box3.png'}

}
