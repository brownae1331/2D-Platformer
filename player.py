# This file contains all the code for the player
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):  # Need to know the postion the player will be placed
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')  # Not permanent colour
        self.rect = self.image.get_rect(topleft=pos)

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)

    # This function get the input from the user and moves the player
    def getInput(self):
        keys = pygame.key.get_pressed()

        # When the right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        # When the left arrow key is pressed
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        # When none of the arrow keys are pressed
        else:
            self.direction.x = 0

    def update(self):
        self.getInput()
        # When the arrow key is held the value of the direction keeps being added to the x value of the player making it move
        # Multiple the direction by 8 so the player is faster. Could change in the future to vary the speed of the player while running
        self.rect.x += self.direction.x * 8
