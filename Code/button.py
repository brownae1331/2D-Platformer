import pygame


class Button():
    def __init__(self, image, pos, width, height):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(center=pos)

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkForInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
