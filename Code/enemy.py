import pygame
import spritesheet
from player import Player


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.gravity = 0.8

        self.onGround = False

        self.status = 'Idle-Run (44x30).png'
        self.animationSteps = 10
        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 75
        self.frameIndex = 0
        self.getAnimationAssest(self.status, self.animationSteps)
        self.image = self.animationList[self.frameIndex]

        self.rect = self.image.get_rect(midtop=pos)
        self.mask = pygame.mask.from_surface(self.image)

        self.hit = False

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def getAnimationAssest(self, status, animationSteps):
        self.animationList = []
        spriteSheetImage = pygame.image.load(
            'Assests/Enemies/Slime/' + status).convert_alpha()
        spriteSheet = spritesheet.SpriteSheet(spriteSheetImage)

        for i in range(animationSteps):
            self.animationList.append(
                spriteSheet.getImage(i, 44, 30, 3, 'black'))

    def animation(self):
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate >= self.animationCooldown:
            self.frameIndex += 1
            self.lastUpdate = currentTime
            if self.frameIndex >= self.animationSteps - 1:
                self.frameIndex = 0

        self.image = self.animationList[self.frameIndex]

    def update(self, XShift):
        self.getAnimationAssest(self.status, self.animationSteps)
        self.animation()
        self.rect.x += XShift
