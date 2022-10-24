import pygame
from tiles import AnimatedTile


class Enemy(AnimatedTile):
    def __init__(self, pos, size, path, status, steps, width, height):
        super().__init__(pos, size, path, status, steps, width, height)
        self.rect.y += size - self.image.get_size()[1]
        self.speed = -2

    def move(self):
        self.rect.x += self.speed

    def reverseImage(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

        # Sets all the black pixels to transparent
        self.image.set_colorkey('black')

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        super().update(shift)
        self.move()
        self.reverseImage()


class Slime(Enemy):
    def __init__(self, pos, size):
        super().__init__(pos, size, 'Assets/Enemies/Slime/',
                         'Idle-Run (44x30).png', 10, 44, 30)
        self.speed = 1
