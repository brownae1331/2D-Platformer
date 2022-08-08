import pygame
from game import Game

game = Game()

while game.running:

    game.currentMenu.menuLoop()
    game.gameLoop()

pygame.quit()
