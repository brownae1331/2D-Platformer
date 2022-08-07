import pygame
from game import Game

game = Game()

while game.running:

    game.currentMenu.displayMenu()
    game.gameLoop()

pygame.quit()
