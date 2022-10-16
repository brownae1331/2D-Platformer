import pygame


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()

        self.image = pygame.image.load('Assets/Items/Boxes/Box1/Idle.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.mask.Mask.get_rect(self.mask)
        self.rect.topleft = pos

    def update(self, xShift):
        self.rect.x += xShift
