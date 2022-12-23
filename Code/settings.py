# This file hold the variables that will be used in all the files
import csv
import pygame

screenWidth = 1536
screenHeight = 704

tileSize = 64  # The size of the tiles


def importCSVLayout(path):
    terrainMap = []
    with open(path) as map:
        level = csv.reader(map, delimiter=',')
        for row in level:
            terrainMap.append(list(row))
        return terrainMap


def exportCVSLayout(layer, layout, level):
    with open(f'CustomLevels/{level}/Level{level}_{layer}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in layout:
            writer.writerow(row)


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
    0: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/TL.png', 'csv': 6},
    1: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/TM.png', 'csv': 7},
    2: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/TR.png', 'csv': 8},
    3: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/ML.png', 'csv': 28},
    4: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/M.png', 'csv': 29},
    5: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/MR.png', 'csv': 30},
    6: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/BL.png', 'csv': 50},
    7: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/BM.png', 'csv': 51},
    8: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/BR.png', 'csv': 52},
    9: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XBL.png', 'csv': 31},
    10: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XBR.png', 'csv': 32},
    11: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XTL.png', 'csv': 9},
    12: {'style': 'terrain', 'menu': 'terrain', 'path': 'Assets/Level Editor/Terrain/XTR.png', 'csv': 10},

    13: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/HL.png', 'csv': 12},
    14: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/HM.png', 'csv': 13},
    15: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/HR.png', 'csv': 14},
    16: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/VB.png', 'csv': 59},
    17: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/VM.png', 'csv': 37},
    18: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/VT.png', 'csv': 15},
    19: {'style': 'terrain', 'menu': 'platform', 'path': 'Assets/Level Editor/Platform/X.png', 'csv': 34},

    21: {'style': 'fruit', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Banana.png', 'csv': 0},
    20: {'style': 'fruit', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Apple.png', 'csv': 1},
    22: {'style': 'fruit', 'menu': 'fruit', 'path': 'Assets/Level Editor/Menu/Pineapple.png', 'csv': 2},

    23: {'style': 'enemy', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Slime.png', 'csv': 1},
    24: {'style': 'enemy', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Chicken.png', 'csv': 0},
    25: {'style': 'enemy', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Rino.png', 'csv': 2},
    26: {'style': 'obstacle', 'menu': 'enemy', 'path': 'Assets/Level Editor/Menu/Spikes.png', 'csv': 0},

    27: {'style': 'crate', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box1.png', 'csv': 6},
    28: {'style': 'crate', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box2.png', 'csv': 6},
    29: {'style': 'crate', 'menu': 'crate', 'path': 'Assets/Level Editor/Menu/Box3.png', 'csv': 6}

}
