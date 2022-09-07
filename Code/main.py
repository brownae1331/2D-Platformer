import pygame
from game import Game

game = Game()

while game.running:

    game.mainMenu.menuLoop()
    game.gameLoop()
    game.levelEditor.editorLoop()
    game.menu.menuLoop()
pygame.quit()
