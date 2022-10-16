import pygame
from animation import Animation


class Enemy(pygame.sprite.Sprite, Animation):
    def __init__(self, pos):
        super().__init__()

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.gravity = 0.8

        self.onGround = False

        self.lastUpdate = pygame.time.get_ticks()
        self.animationCooldown = 75
        self.frameIndex = 0
        self.status = 'Idle-Run (44x30).png'
        self.animationSteps = 10
        self.getAnimationAssests(
            'Assets/Enemies/Slime/', self.status, self.animationSteps, 44, 30)

        self.image = self.animationList[self.frameIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.mask.Mask.get_rect(self.mask)
        self.rect.midtop = pos

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self, XShift):
        self.getAnimationAssests(
            'Assets/Enemies/Slime/', self.status, self.animationSteps, 44, 30)
        self.image = self.animation(self.animationSteps)
        self.rect.x += XShift
