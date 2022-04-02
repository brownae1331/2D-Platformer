# Main file which needs to be run to start the game
import pygame
from settings import *  # From settings import everything
from tiles import Tile

pygame.init()

# Set the size of the window that the game will played in
# The variables screenWidth and screenHeight are from the settings file
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Setting the contion for the game loop
done = False
clock = pygame.time.Clock()

tileTest = pygame.sprite.Group(Tile((100, 100), 200))

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If you close the game window the game loop will stop
            done = True

    screen.fill('black')  # Set the background colour
    tileTest.draw(screen)

    clock.tick(60)  # Set the clock speed of the game
    pygame.display.flip()


# If the loop is broken the pygame window will close
pygame.quit()
