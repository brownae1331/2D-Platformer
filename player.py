# This file contains all the code for the player
import pygame
import spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):  # Need to know the postion the player will be placed
        super().__init__()

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jumpSpeed = -16

        # Player status
        self.onGround = False

        # Player Animation
        self.status = 'Idle (32x32).png'
        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 75
        self.frameIndex = 0
        self.animationList = []
        self.getAnimationAssest('Idle (32x32).png', 11)
        self.image = self.animationList[0]

        self.rect = self.image.get_rect(topleft=pos)

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

        # When the space bar is pressed the player jumps
        if keys[pygame.K_SPACE] and self.onGround:
            self.direction.y = self.jumpSpeed

    def applyGravity(self):
        # Gravity is applied to the direction of the player
        self.direction.y += self.gravity
        # The direction is added to the position of the player
        self.rect.y += self.direction.y

    def getAnimationAssest(self, status, animationSteps):
        spriteSheetImage = pygame.image.load(
            'Assests/Main Characters/Ninja Frog/' + status).convert_alpha()
        spriteSheet = spritesheet.SpriteSheet(spriteSheetImage)

        for i in range(animationSteps):
            self.animationList.append(
                spriteSheet.getImage(i, 32, 32, 3, 'black'))

    def animation(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.animationCooldown:
            self.frameIndex += 1
            self.lastUpdate = currentTime
            if self.frameIndex >= len(self.animationList):
                self.frameIndex = 0

    def update(self):
        self.getInput()
        self.animation()
