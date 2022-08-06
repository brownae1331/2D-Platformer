# Main file which needs to be run to start the game
from re import M
import pygame
from mainmenu import MainMenu
from settings import *  # From settings import everything
from level import Level

pygame.init()

# Set the size of the window that the game will played in
# The variables screenWidth and screenHeight are from the settings fil7e
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Setting the contion for the game loop
done = False
status = 'menu'
clock = pygame.time.Clock()

mainMenu = MainMenu(screen)
level = Level(levelMap, screen)

# Main game loop
while not done:

    mousePos = pygame.mouse.get_pos()

    if status == 'menu':
        mainMenu.displayMenu()
    elif status == 'play':
        level.run()
    elif status == 'exit':
        done = True

    status = mainMenu.buttonPress(mousePos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If you close the game window the game loop will stop
            done = True

    clock.tick(60)  # Set the clock speed of the game
    pygame.display.flip()


# If the loop is broken the pygame window will close
pygame.quit()
