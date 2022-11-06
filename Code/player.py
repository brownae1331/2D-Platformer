# This file contains all the code for the player
import pygame
import random
from animation import Animation
from settings import *


class Player(pygame.sprite.Sprite, Animation):
    def __init__(self, pos, game):  # Need to know the postion the player will be placed
        super().__init__()
        self.game = game
        self.time = pygame.time.get_ticks()

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jumpSpeed = -16

        # Player status
        self.onGround = False

        # Player Animation
        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 75
        self.frameIndex = 0
        self.status = 'Idle (32x32).png'
        self.animationSteps = 11  # The player will be in the Idle animation on first frame
        self.getAnimationAssests(
            'Assets/Main Characters/Ninja Frog/', self.status, self.animationSteps, 32, 32)

        # Power Ups
        self.startTime = 0
        self.isInvincible = False
        self.runDoubleJump = False
        self.jumps = 0

        self.image = self.animationList[self.frameIndex]
        self.rect = self.image.get_rect(topleft=pos)

    # This function get the input from the user and moves the player

    def getInput(self):
        keys = pygame.key.get_pressed()

        # When the right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'Run (32x32).png'
            self.animationSteps = 12
        # When the left arrow key is pressed
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'Run (32x32).png'
            self.animationSteps = 12
        # When none of the arrow keys are pressed
        else:
            self.direction.x = 0
            self.status = 'Idle (32x32).png'
            self.animationSteps = 11

        # When the space bar is pressed the player jumps
        if (keys[pygame.K_SPACE] and self.onGround == True) or (keys[pygame.K_SPACE] and self.runDoubleJump == True and self.jumps == 1 and self.direction.y > 0):
            self.direction.y = self.jumpSpeed
            self.jumps += 1

    def applyGravity(self):
        # Gravity is applied to the direction of the player
        self.direction.y += self.gravity
        # The direction is added to the position of the player
        self.rect.y += self.direction.y

    def reverseImage(self):
        if self.direction.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.image.set_colorkey('black')

    def applyPowerUp(self):
        for powerUp in [self.isInvincible, self.runDoubleJump]:
            if powerUp:
                if self.time - self.startTime > 10000:
                    self.isInvincible = False
                    self.runDoubleJump = False

    def powerUp(self):
        powerUpNum = random.randint(1, 2)
        if powerUpNum == 1:
            self.startTime = 0
            self.startTime = pygame.time.get_ticks()
            self.isInvincible = True
        elif powerUpNum == 2:
            self.startTime = 0
            self.startTime = pygame.time.get_ticks()
            self.runDoubleJump = True

    def update(self):
        self.time = pygame.time.get_ticks()
        self.getInput()
        self.getAnimationAssests(
            'Assets/Main Characters/Ninja Frog/', self.status, self.animationSteps, 32, 32)
        self.image = self.animation(self.animationSteps)
        self.reverseImage()
        self.applyPowerUp()
        print(
            f'jumps: {self.jumps}, direction.y: {self.direction.y}, timer {(self.time - self.startTime)}')
