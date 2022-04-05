# Main file which needs to be run to start the game
import pygame
from settings import *  # From settings import everything
from level import Level

pygame.init()

# Set the size of the window that the game will played in
# The variables screenWidth and screenHeight are from the settings fil7e
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Setting the contion for the game loop
done = False
clock = pygame.time.Clock()

level = Level(levelMap, screen)

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If you close the game window the game loop will stop
            done = True

    screen.fill('black')  # Set the background colour
    level.run()  # When the main file is run the level is run

    clock.tick(60)  # Set the clock speed of the game
    pygame.display.flip()


# If the loop is broken the pygame window will close
pygame.quit()
