import pygame


class ImageButton:
    def __init__(self, image, pos, width, height):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect(center=pos)

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkForInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False


class TextButton:
    def __init__(self, textInput, font, pos):
        self.font = pygame.font.Font(font, 50)
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, '#000000')
        self.rect = self.text.get_rect(center=pos)

    def update(self, screen):
        screen.blit(self.text, self.rect)

    def checkForInput(self, pos):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
